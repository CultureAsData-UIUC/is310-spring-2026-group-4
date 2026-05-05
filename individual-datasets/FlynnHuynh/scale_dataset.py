"""
scale_dataset.py
================
Scales immigrant_dish_dataset.csv from 50 → 500+ entries automatically.

HOW IT WORKS
------------
1. Runs pre-defined search queries through DuckDuckGo (free, no API key)
2. Collects URLs from search results — no manual link-hunting needed
3. Scrapes relevant text from each URL
4. Annotates each entry using Gemini (free tier)
5. Merges new entries with your existing 50 into one final CSV (see OUTPUT).

USAGE
-----
  python3 scale_dataset.py

Paths are relative to this script’s folder; you can run from any working directory.
If you resumed with an old _scaled_progress.csv that used a shorter header, delete it once and restart so the progress file matches the current column list.

OUTPUT
------
  immigrant_dish_dataset_merged.csv — bespoke + scaled rows (written in this folder).
  Your original Individual Inital Dataset CSV is only read, not overwritten.
  _scaled_progress.csv — resumable checkpoint for new rows only.

REQUIREMENTS
------------
  pip install ddgs requests beautifulsoup4 google-generativeai

RUNTIME ESTIMATE (free Gemini tier, 60s/request)
-------------------------------------------------
  ~500 entries = ~8-9 hours total
  The script is fully resumable — Ctrl+C and re-run anytime, already-done entries are skipped.
  Tip: run overnight with:  nohup python scale_dataset.py > log.txt 2>&1 &
"""

import os
import csv
import json
import time
import urllib.robotparser
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
from ddgs import DDGS

# ── CONFIG ────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Hand-curated baseline (read-only)
EXISTING_BESPOKE_CSV = os.path.join(
    BASE_DIR,
    "Individual Inital Dataset_IS310_Flynn Huynh - immigrant_dish_dataset.csv",
)
# Final merged dataset (bespoke + auto-scaled rows)
OUTPUT_CSV = os.path.join(BASE_DIR, "immigrant_dish_dataset_merged.csv")
# Resumable progress for scaled rows only
PROGRESS_CSV = os.path.join(BASE_DIR, "_scaled_progress.csv")
# Saves the last completed query index so restarts skip finished queries
QUERY_CHECKPOINT = os.path.join(BASE_DIR, "_query_checkpoint.txt")
RESULTS_PER_QUERY = 10   # DDG results per search query
MIN_DELAY_SEC  = 62      # seconds between Gemini calls (free tier ~15 req/min)
REQUEST_TIMEOUT = 10
MAX_EXCERPT_CHARS = 3000
MAX_RETRIES = 2
RETRY_WAIT_SEC = 65
SEARCH_DELAY_SEC = 3     # polite delay between DDG searches

# ── SEARCH QUERIES ────────────────────────────────────────────────────────────
# Each tuple: (dish_name, immigrant_community, transformation_type, search_query)
# Pre-defined so you don't have to think about them.
# ~8 queries × 6 dishes × 10 results = ~480 candidate URLs

SEARCH_QUERIES = [
    # ── ORANGE CHICKEN ────────────────────────────────────────────────────────
    ("Orange Chicken", "Chinese-American", "Pure American Invention",
     "orange chicken chinese american history origin food"),
    ("Orange Chicken", "Chinese-American", "Pure American Invention",
     "orange chicken panda express invention recipe blog"),
    ("Orange Chicken", "Chinese-American", "Pure American Invention",
     "orange chicken recipe community asian food blog"),
    ("Orange Chicken", "Chinese-American", "Pure American Invention",
     "orange chicken authenticity chinese american diaspora food media"),
    ("Orange Chicken", "Chinese-American", "Pure American Invention",
     "how to make orange chicken recipe site:seriouseats.com OR site:bonappetit.com OR site:food52.com"),
    ("Orange Chicken", "Chinese-American", "Pure American Invention",
     "orange chicken recipe allrecipes OR foodnetwork OR tasteofhome"),
    ("Orange Chicken", "Chinese-American", "Pure American Invention",
     "orange chicken youtube cooking channel recipe 2022 2023 2024"),
    ("Orange Chicken", "Chinese-American", "Pure American Invention",
     "orange chicken american invention not chinese food culture"),

    # ── FORTUNE COOKIE ────────────────────────────────────────────────────────
    ("Fortune Cookie", "Chinese-American", "Misattribution (Japanese-American origin)",
     "fortune cookie history japanese american origin misattribution"),
    ("Fortune Cookie", "Chinese-American", "Misattribution (Japanese-American origin)",
     "fortune cookie recipe food blog chinese american"),
    ("Fortune Cookie", "Chinese-American", "Misattribution (Japanese-American origin)",
     "fortune cookie history japanese san francisco world war ii"),
    ("Fortune Cookie", "Chinese-American", "Misattribution (Japanese-American origin)",
     "fortune cookie recipe allrecipes OR tasteofhome OR foodnetwork"),
    ("Fortune Cookie", "Chinese-American", "Misattribution (Japanese-American origin)",
     "fortune cookie origin food52 OR seriouseats OR eater history"),
    ("Fortune Cookie", "Chinese-American", "Misattribution (Japanese-American origin)",
     "homemade fortune cookie recipe community food blog 2022 2023"),
    ("Fortune Cookie", "Chinese-American", "Misattribution (Japanese-American origin)",
     "fortune cookie not actually chinese cultural origin debate"),
    ("Fortune Cookie", "Chinese-American", "Misattribution (Japanese-American origin)",
     "fortune cookie tasteatlas OR smithsonian history food reference"),

    # ── CHICKEN PARMESAN ──────────────────────────────────────────────────────
    ("Chicken Parmesan", "Italian-American", "American Invention (inspired by Italian technique)",
     "chicken parmesan italian american history origin"),
    ("Chicken Parmesan", "Italian-American", "American Invention (inspired by Italian technique)",
     "chicken parmesan recipe community italian american food blog"),
    ("Chicken Parmesan", "Italian-American", "American Invention (inspired by Italian technique)",
     "chicken parmigiana american invention eggplant substitution immigration"),
    ("Chicken Parmesan", "Italian-American", "American Invention (inspired by Italian technique)",
     "chicken parmesan recipe allrecipes OR tasteofhome OR foodnetwork"),
    ("Chicken Parmesan", "Italian-American", "American Invention (inspired by Italian technique)",
     "chicken parmesan seriouseats OR food52 OR bonappetit recipe"),
    ("Chicken Parmesan", "Italian-American", "American Invention (inspired by Italian technique)",
     "chicken parmesan best recipe 2023 2024 site:eater.com OR site:seriouseats.com"),
    ("Chicken Parmesan", "Italian-American", "American Invention (inspired by Italian technique)",
     "chicken parmigiana italian diaspora food culture american adaptation"),
    ("Chicken Parmesan", "Italian-American", "American Invention (inspired by Italian technique)",
     "chicken parmesan tasteatlas OR saveur OR food wine history"),

    # ── SPAGHETTI AND MEATBALLS ───────────────────────────────────────────────
    ("Spaghetti and Meatballs", "Italian-American", "Significant Adaptation",
     "spaghetti meatballs italian american history invention"),
    ("Spaghetti and Meatballs", "Italian-American", "Significant Adaptation",
     "spaghetti meatballs not italian american adaptation recipe blog"),
    ("Spaghetti and Meatballs", "Italian-American", "Significant Adaptation",
     "spaghetti and meatballs recipe allrecipes OR tasteofhome OR foodnetwork"),
    ("Spaghetti and Meatballs", "Italian-American", "Significant Adaptation",
     "spaghetti meatballs italian immigrant community meat affordable"),
    ("Spaghetti and Meatballs", "Italian-American", "Significant Adaptation",
     "spaghetti meatballs recipe seriouseats OR food52 OR bonappetit"),
    ("Spaghetti and Meatballs", "Italian-American", "Significant Adaptation",
     "spaghetti meatballs sunday gravy italian american diaspora food"),
    ("Spaghetti and Meatballs", "Italian-American", "Significant Adaptation",
     "spaghetti meatballs recipe 2022 2023 2024 cooking channel youtube"),
    ("Spaghetti and Meatballs", "Italian-American", "Significant Adaptation",
     "spaghetti and meatballs tasteatlas OR saveur OR food wine"),

    # ── NACHOS ───────────────────────────────────────────────────────────────
    ("Nachos", "Mexican-American", "Border Invention (Tex-Mex)",
     "nachos history ignacio anaya origin tex-mex border"),
    ("Nachos", "Mexican-American", "Border Invention (Tex-Mex)",
     "nachos recipe mexican american community food blog tex mex"),
    ("Nachos", "Mexican-American", "Border Invention (Tex-Mex)",
     "nachos recipe allrecipes OR tasteofhome OR foodnetwork"),
    ("Nachos", "Mexican-American", "Border Invention (Tex-Mex)",
     "nachos piedras negras 1943 american invention cultural origin food"),
    ("Nachos", "Mexican-American", "Border Invention (Tex-Mex)",
     "nachos recipe seriouseats OR food52 OR bonappetit history"),
    ("Nachos", "Mexican-American", "Border Invention (Tex-Mex)",
     "nachos stadium food commercialization frank liberto history"),
    ("Nachos", "Mexican-American", "Border Invention (Tex-Mex)",
     "nachos tex-mex border food culture 2022 2023 2024 food media"),
    ("Nachos", "Mexican-American", "Border Invention (Tex-Mex)",
     "nachos tasteatlas OR saveur OR texas monthly history reference"),

    # ── MISSION BURRITO ───────────────────────────────────────────────────────
    ("Mission Burrito", "Mexican-American", "American Regional Invention (San Francisco)",
     "mission burrito san francisco history origin mexican american"),
    ("Mission Burrito", "Mexican-American", "American Regional Invention (San Francisco)",
     "mission burrito recipe community mexican american food blog"),
    ("Mission Burrito", "Mexican-American", "American Regional Invention (San Francisco)",
     "mission style burrito allrecipes OR tasteofhome OR foodnetwork recipe"),
    ("Mission Burrito", "Mexican-American", "American Regional Invention (San Francisco)",
     "mission burrito chipotle gentrification mission district taqueria"),
    ("Mission Burrito", "Mexican-American", "American Regional Invention (San Francisco)",
     "mission burrito recipe seriouseats OR food52 OR eater history"),
    ("Mission Burrito", "Mexican-American", "American Regional Invention (San Francisco)",
     "mission burrito el faro taqueria 1960s origin san francisco"),
    ("Mission Burrito", "Mexican-American", "American Regional Invention (San Francisco)",
     "mission style burrito food media 2022 2023 2024 rice inside foil"),
    ("Mission Burrito", "Mexican-American", "American Regional Invention (San Francisco)",
     "mission burrito tasteatlas OR saveur OR la times history"),
]

# ── SYSTEM PROMPT ─────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """You are a cultural food studies research assistant helping to annotate 
sources about immigrant-origin dishes that have been transformed in American contexts.

For each source text provided, return ONLY a JSON object with these exact keys and 
allowed values:

{
  "origin_story_mentioned": "Yes" | "No" | "Partial",
  "origin_story_framing": "omitted" | "simplified" | "mythologized" | "detailed_historical" | "corrective" | "contested",
  "cultural_ownership_framing": "claimed" | "distanced" | "dismissed" | "contested" | "reclaimed" | "not_mentioned",
  "community_credit_given": "Yes" | "No" | "Partial" | "N/A",
  "annotation_notes": "<1-2 sentence explanation of your coding choices>",
  "rationale": "<1 sentence identifying the key textual evidence that drove your coding>"
}

Definitions:

origin_story_mentioned — Yes: explicitly discusses cultural/historical origin. No: no mention. Partial: vague passing mention.

origin_story_framing: omitted | simplified | mythologized | detailed_historical | corrective | contested

cultural_ownership_framing (how does this source position the dish relative to the immigrant community?):
- claimed: presents dish as native/authentic to a cultural tradition
- distanced: acknowledges American adaptation, presents positively
- dismissed: argues cultural origins are irrelevant
- contested: acknowledges debate about cultural ownership
- reclaimed: community member asserts dish as their own valid tradition
- not_mentioned: cultural ownership never raised

community_credit_given: Yes | No | Partial | N/A

rationale: the single phrase or structural feature most responsible for your coding.

Return ONLY valid JSON. No preamble, no markdown."""

# ── CSV COLUMNS ───────────────────────────────────────────────────────────────
COLUMNS = [
    "entry_id", "dish_name", "immigrant_community", "transformation_type",
    "source_name", "source_type", "author_background", "year_published", "url",
    "scrape_status", "scraped_excerpt",
    "origin_story_mentioned", "origin_story_framing", "cultural_ownership_framing",
    "notable_substitutions",
    "community_credit_given", "annotation_notes", "rationale",
]

# Columns present in bespoke CSV (different schema — map on merge)
BESPOKE_COLUMNS = [
    "entry_id", "dish_name", "immigrant_community", "transformation_type",
    "source_name", "source_type", "author_background", "year_published", "url",
    "origin_story_mentioned", "origin_story_framing", "cultural_ownership_framing",
    "notable_substitutions", "community_credit_given", "annotation_notes",
]


# ── HELPERS ───────────────────────────────────────────────────────────────────
def normalize_row(row: dict) -> dict:
    """Ensure every COLUMNS key exists (for resumed progress or partial dicts)."""
    return {c: (row.get(c) if row.get(c) is not None else "") for c in COLUMNS}


def load_existing_entries() -> tuple[list[dict], set[str]]:
    """Load bespoke CSV, return (rows_as_output_schema, set_of_existing_urls)."""
    rows, urls = [], set()
    try:
        with open(EXISTING_BESPOKE_CSV, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                # Map bespoke schema → unified COLUMNS
                new_row = {c: "" for c in COLUMNS}
                for col in BESPOKE_COLUMNS:
                    if col in row:
                        new_row[col] = row[col]
                # Legacy column name in older CSVs
                if "cultural_ownership_framing" in row and not str(
                    new_row.get("cultural_ownership_framing", "")
                ).strip():
                    new_row["cultural_ownership_framing"] = row.get(
                        "cultural_ownership_framing", ""
                    )
                new_row["scrape_status"] = "bespoke"
                new_row["scraped_excerpt"] = ""
                new_row["rationale"] = ""
                rows.append(new_row)
                urls.add(row.get("url", "").strip())
    except FileNotFoundError:
        print(
            f"[warn] {os.path.basename(EXISTING_BESPOKE_CSV)} not found — starting fresh."
        )
    return rows, urls


_robots_cache: dict = {}

def can_scrape(url: str) -> bool:
    parsed = urlparse(url)
    base = f"{parsed.scheme}://{parsed.netloc}"
    if base not in _robots_cache:
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(f"{base}/robots.txt")
        try:
            rp.read()
            _robots_cache[base] = rp
        except Exception:
            _robots_cache[base] = None
    rp = _robots_cache[base]
    return rp is None or rp.can_fetch("*", url)


HEADERS = {"User-Agent": "Mozilla/5.0 (academic research; IS310 UIUC course project)"}

def scrape(url: str) -> tuple[str, str]:
    """Returns (status, excerpt). Status: ok | robots_blocked | partial_paywall | failed"""
    if not can_scrape(url):
        return "robots_blocked", ""
    try:
        r = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        r.raise_for_status()
    except Exception as e:
        return "failed", ""

    soup = BeautifulSoup(r.text, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()

    excerpt = ""
    for sel in ["[class*='headnote']", "[class*='intro']", "[class*='summary']",
                "div.recipe-summary", "div.tasty-recipes-description"]:
        el = soup.select_one(sel)
        if el and len(el.get_text(strip=True)) > 80:
            excerpt = el.get_text(" ", strip=True)
            break

    if not excerpt:
        main = soup.find("main") or soup.find("article") or soup.find("body")
        if main:
            paras = [p.get_text(" ", strip=True)
                     for p in main.find_all("p") if len(p.get_text(strip=True)) > 80]
            excerpt = " ".join(paras[:4])

    if not excerpt:
        meta = soup.find("meta", {"name": "description"})
        if meta:
            excerpt = meta.get("content", "")

    paywall = ["subscribe to read", "sign in to read", "create a free account",
               "already a subscriber", "unlimited access"]
    status = "partial_paywall" if (
        any(s in r.text.lower() for s in paywall) and len(excerpt) < 300
    ) else "ok"

    return status, excerpt[:MAX_EXCERPT_CHARS]


def infer_metadata(url: str, dish_name: str) -> dict:
    """Best-effort source_name, source_type, author_background from URL."""
    domain = urlparse(url).netloc.replace("www.", "")
    domain_map = {
        "seriouseats.com":   ("Serious Eats",          "Food Media",                   "Non-Community Food Writer"),
        "eater.com":         ("Eater",                 "Food Media",                   "Non-Community Food Writer/Journalist"),
        "bonappetit.com":    ("Bon Appétit",            "Food Media",                   "Non-Community Food Writer"),
        "food52.com":        ("Food52",                 "Food Media",                   "Non-Community Food Writer"),
        "allrecipes.com":    ("AllRecipes",             "Mainstream Recipe Aggregator", "Unknown/Community"),
        "foodnetwork.com":   ("Food Network",           "Mainstream Recipe Aggregator", "Non-Community Food Writer"),
        "tasteofhome.com":   ("Taste of Home",          "Mainstream Recipe Aggregator", "Unknown/Community"),
        "cooking.nytimes.com":("NYT Cooking",           "Mainstream Recipe Aggregator", "Non-Community Food Writer"),
        "nytimes.com":       ("New York Times",         "Food Media",                   "Non-Community Food Writer/Journalist"),
        "tasteatlas.com":    ("TasteAtlas",             "Reference/Encyclopedia",       "Unknown/Editorial"),
        "thewoksoflife.com": ("The Woks of Life",       "Community Food Blog",          "Community Member"),
        "lidiasitaly.com":   ("Lidia's Italy",          "Community Food Blog",          "Community Member (Italian-American chef)"),
        "chicanoeats.com":   ("Chicano Eats",           "Community Food Blog",          "Community Member"),
        "redhousespice.com": ("Red House Spice",        "Community Food Blog",          "Community Member"),
        "smithsonianmag.com":("Smithsonian Magazine",   "Food Media/Journalism",        "Academic/Journalist"),
        "foodtimeline.org":  ("The Food Timeline",      "Reference/Encyclopedia",       "Academic/Journalist"),
        "foodandwine.com":   ("Food & Wine",            "Food Media",                   "Non-Community Food Writer"),
        "saveur.com":        ("Saveur",                 "Food Media",                   "Non-Community Food Writer"),
        "americastestkitchen.com": ("America's Test Kitchen", "Food Media",             "Non-Community Food Writer"),
        "texasmonthly.com":  ("Texas Monthly",          "Food Media/Regional",          "Non-Community Food Writer/Journalist"),
        "sfchronicle.com":   ("San Francisco Chronicle","Food Media/Regional",          "Non-Community Food Writer/Journalist"),
        "latimes.com":       ("Los Angeles Times",      "Food Media/Regional",          "Non-Community Food Writer/Journalist"),
        "youtube.com":       ("YouTube",                "YouTube Cooking Channel",      "Unknown"),
        "npr.org":           ("NPR",                    "Food Media/Journalism",        "Academic/Journalist"),
        "theguardian.com":   ("The Guardian",           "Food Media",                   "Non-Community Food Writer/Journalist"),
        "chipotle.com":      ("Chipotle Official Website", "Corporate/Brand",           "Corporate/Anonymous"),
        "pandaexpress.com":  ("Panda Express Official Website", "Corporate/Brand",      "Corporate/Anonymous"),
    }
    source_name, source_type, author_bg = domain_map.get(
        domain, (domain, "Food Media", "Unknown"))
    return {"source_name": source_name, "source_type": source_type,
            "author_background": author_bg}


def annotate(model, excerpt: str, row: dict) -> dict:
    dish_info = (
        f"{row['dish_name']}, {row['immigrant_community']}, "
        f"{row['transformation_type']}, source: {row['source_name']} "
        f"({row['source_type']}, {row['author_background']})"
    )
    msg = f'Dish context: {dish_info}\n\nSource text:\n"""\n{excerpt}\n"""\n\nReturn JSON annotation.'
    response = model.generate_content(msg, generation_config={"max_output_tokens": 600})
    raw = response.text.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()
    return json.loads(raw)


EMPTY_ANNOTATION = {
    "origin_story_mentioned": "", "origin_story_framing": "",
    "cultural_ownership_framing": "", "community_credit_given": "",
    "annotation_notes": "annotation_failed", "rationale": "",
}


# ── MAIN ──────────────────────────────────────────────────────────────────────
def main():
    print("=" * 60)
    print("Immigrant Dish Dataset — Auto-Scale to 500+")
    print("=" * 60)

    # Load existing bespoke entries
    bespoke_rows, existing_urls = load_existing_entries()
    print(f"Loaded {len(bespoke_rows)} existing bespoke entries.")

    # Load already-scaled entries (for resumability)
    scaled_urls: set[str] = set()
    scaled_rows: list[dict] = []
    try:
        with open(PROGRESS_CSV, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                scaled_rows.append(row)
                scaled_urls.add(row.get("url", "").strip())
        print(f"Resuming — {len(scaled_rows)} new entries already processed.")
    except FileNotFoundError:
        pass

    all_known_urls = existing_urls | scaled_urls

    # Load query checkpoint — skip queries already completed on a previous run
    start_query_idx = 0
    try:
        with open(QUERY_CHECKPOINT) as f:
            start_query_idx = int(f.read().strip())
        print(f"Resuming from query {start_query_idx + 1}/{len(SEARCH_QUERIES)} "
              f"(skipping {start_query_idx} already-completed queries).")
    except (FileNotFoundError, ValueError):
        pass

    # Set up Gemini
    # api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
    # if not api_key:
    api_key = input("Enter your Gemini API key: ").strip()
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash", system_instruction=SYSTEM_PROMPT)

    # Open progress file for appending
    progress_file = open(PROGRESS_CSV, "a", newline="", encoding="utf-8")
    progress_writer = csv.DictWriter(progress_file, fieldnames=COLUMNS)
    if not scaled_rows:
        progress_writer.writeheader()

    last_gemini_call = 0.0
    new_count = len(scaled_rows)
    target = 500 - len(bespoke_rows)  # how many new entries we need

    print(f"\nTarget: {target} new entries (to reach 500 total)")
    print(f"Running {len(SEARCH_QUERIES)} search queries × {RESULTS_PER_QUERY} results each...\n")

    ddg = DDGS()

    for q_idx, (dish, community, transform, query) in enumerate(SEARCH_QUERIES, 1):
        if q_idx - 1 < start_query_idx:
            continue  # already done on a previous run
        if new_count >= target:
            print(f"\nTarget of {target} new entries reached. Stopping search.")
            break

        print(f"[Query {q_idx}/{len(SEARCH_QUERIES)}] {dish}: \"{query[:60]}...\"")
        time.sleep(SEARCH_DELAY_SEC)

        try:
            results = list(ddg.text(query, max_results=RESULTS_PER_QUERY))
        except Exception as e:
            print(f"  DDG search failed: {e} — skipping query.")
            continue

        # Save which query we just finished so restarts can skip it
        with open(QUERY_CHECKPOINT, "w") as f:
            f.write(str(q_idx))

        for result in results:
            if new_count >= target:
                break

            url = result.get("href", "").strip()
            if not url or url in all_known_urls:
                continue

            # Infer entry_id
            dish_code = {
                "Orange Chicken": "OC", "Fortune Cookie": "FC",
                "Chicken Parmesan": "CP", "Spaghetti and Meatballs": "SM",
                "Nachos": "NA", "Mission Burrito": "MB",
            }.get(dish, "XX")
            entry_id = f"{dish_code}-{len(bespoke_rows) + new_count + 1:03d}"

            meta = infer_metadata(url, dish)

            print(f"  [{entry_id}] {meta['source_name']} — scraping...")
            scrape_status, excerpt = scrape(url)
            print(f"           status={scrape_status}, excerpt_len={len(excerpt)}")

            row = {
                "entry_id": entry_id,
                "dish_name": dish,
                "immigrant_community": community,
                "transformation_type": transform,
                "source_name": meta["source_name"],
                "source_type": meta["source_type"],
                "author_background": meta["author_background"],
                "year_published": "",   # filled manually or from scrape
                "url": url,
                "scrape_status": scrape_status,
                "scraped_excerpt": excerpt,
                "origin_story_mentioned": "",
                "origin_story_framing": "",
                "cultural_ownership_framing": "",
                "notable_substitutions": "",
                "community_credit_given": "",
                "annotation_notes": "",
                "rationale": "",
            }

            annotation = EMPTY_ANNOTATION.copy()
            if excerpt and scrape_status in ("ok", "partial_paywall"):
                elapsed = time.monotonic() - last_gemini_call
                if elapsed < MIN_DELAY_SEC:
                    wait = MIN_DELAY_SEC - elapsed
                    print(f"           Rate limit: waiting {wait:.0f}s...")
                    time.sleep(wait)

                print("           Annotating with Gemini...")
                last_gemini_call = time.monotonic()

                for attempt in range(MAX_RETRIES + 1):
                    try:
                        annotation = annotate(model, excerpt, row)
                        break
                    except json.JSONDecodeError:
                        print("           JSON parse error.")
                        break
                    except Exception as e:
                        err = str(e)
                        is_daily_quota = (
                            "PerDay" in err or "per_day" in err.lower()
                            or "GenerateRequestsPerDay" in err
                        )
                        is_rate_limit = (
                            "429" in err
                            or "quota" in err.lower()
                            or "rate" in err.lower()
                        )
                        if is_daily_quota:
                            import datetime, zoneinfo
                            pt = zoneinfo.ZoneInfo("America/Los_Angeles")
                            now_pt = datetime.datetime.now(pt)
                            midnight_pt = (now_pt + datetime.timedelta(days=1)).replace(
                                hour=0, minute=2, second=0, microsecond=0
                            )
                            wait_sec = (midnight_pt - now_pt).total_seconds()
                            print(f"           Daily quota exhausted.")
                            print(f"           Sleeping until {midnight_pt.strftime('%H:%M PT')} "
                                  f"({wait_sec/3600:.1f} hrs)... script will resume automatically.")
                            time.sleep(wait_sec)
                            last_gemini_call = 0.0
                            print("           Quota reset — retrying annotation...")
                        elif is_rate_limit:
                            if attempt < MAX_RETRIES:
                                print(f"           Per-minute rate limit, retrying in {RETRY_WAIT_SEC}s...")
                                time.sleep(RETRY_WAIT_SEC)
                                last_gemini_call = time.monotonic()
                            else:
                                print(f"           Gemini error after retries: {e}")
                        else:
                            print(f"           Gemini error: {e}")
                            break
            else:
                annotation["annotation_notes"] = f"skipped — {scrape_status}"

            row.update(annotation)
            out_row = normalize_row(row)
            print(f"           origin={annotation.get('origin_story_mentioned')} | "
                  f"ownership={annotation.get('cultural_ownership_framing')} | "
                  f"credit={annotation.get('community_credit_given')}")

            progress_writer.writerow(out_row)
            progress_file.flush()
            all_known_urls.add(url)
            scaled_rows.append(out_row)
            new_count += 1

    progress_file.close()

    # ── MERGE AND WRITE FINAL CSV ─────────────────────────────────────────────
    print(
        f"\nMerging {len(bespoke_rows)} bespoke + {len(scaled_rows)} new entries → "
        f"{os.path.basename(OUTPUT_CSV)}"
    )
    all_rows = [normalize_row(r) for r in bespoke_rows] + [
        normalize_row(r) for r in scaled_rows
    ]
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"\nFinal dataset: {len(all_rows)} entries saved to {os.path.basename(OUTPUT_CSV)}")
    print(f"  Bespoke entries:    {len(bespoke_rows)}")
    print(f"  Scaled new entries: {len(scaled_rows)}")
    failed = sum(1 for r in scaled_rows if "failed" in r.get("scrape_status",""))
    blocked = sum(1 for r in scaled_rows if r.get("scrape_status") == "robots_blocked")
    print(f"  Failed scrapes:     {failed} (manual fill recommended)")
    print(f"  Robots blocked:     {blocked}")
    print(f"\nDone! Output: {OUTPUT_CSV}")


if __name__ == "__main__":
    main()