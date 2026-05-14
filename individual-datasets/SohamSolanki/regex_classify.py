"""
Regex / Keyword-Based Classification Pipeline
==============================================

Method #1 of three for the methodological triangulation suggested by
the instructor:
  1. Regex + keyword counting       (this file)
  2. Regression / BERT model        (shorttext-based, separate file)
  3. LLM classification             (llm_classify.py)

This script replicates the keyword decision tree from the scaling
plan (Phase 2 Method 1) and the moral language patterns (Phase 4)
exactly as proposed, so the comparison against the LLM run is a fair
test of the original plan.

Output: a separate CSV with regex-derived columns, joinable to the
original dataset on `id`. The original data is not touched.

Author: Soham Solanki
Course: IS310 — Culture as Data
"""

import csv
import re
from pathlib import Path


# ---------------------------------------------------------------------------
# Keyword decision tree — replicates the categorize_video() function from
# documentation.md, Phase 2 Method 1. Order matters: more specific patterns
# are checked first to avoid bleed-through (e.g. a WIEIAD that mentions
# protein coffee).
#
# Each entry: (target_category, [keyword_list])
# A video is assigned to the first category whose keyword appears in
# caption + hashtags (lowercased).
# ---------------------------------------------------------------------------
KEYWORD_RULES = [
    ("Routine Performance (WIEIAD)",
        ["what i eat in a day", "wieiad", "whatieatinaday",
         "full day of eating", "fulldayofeating"]),

    ("Routine Performance (Meal Prep)",
        ["meal prep", "mealprep", "mealprepideas", "weeklymealprep",
         "healthymealprep", "highproteinmealprep", "tastymealprep",
         "easymealprep"]),

    ("Protein-Enhanced Coffee",
        ["protein coffee", "proffee", "proteincoffee",
         "proteincoffeerecipe", "protein latte", "javvy"]),

    ("Protein-Enhanced Breakfast",
        ["protein oats", "proteinoats", "baked oats", "bakedoats",
         "proteinoatsrecipe", "proteinbreakfast", "highproteinbreakfast",
         "highproteinbreakfastideas", "overnight oats", "overnightoats"]),

    ("Protein Dessert (Guilt-Free)",
        ["guilt free", "guilt-free", "guiltfree",
         "protein dessert", "lowcaloriedessert", "healthydessert",
         "nobakeprotein", "protein bite", "protein bites",
         "browniebites", "brownieballs", "protein balls", "proteinballs"]),

    ("Fitness Culture (Pre-Workout)",
        ["pre workout", "pre-workout", "preworkout"]),

    ("Fitness Culture (Post-Workout)",
        ["post workout", "post-workout", "postworkout",
         "postworkoutmeal"]),

    ("Food as Fuel/Optimization",
        ["food is fuel", "food as fuel", "fuel for"]),
]
DEFAULT_CATEGORY = "High Protein (General)"


def keyword_classify(caption: str, hashtags: str) -> str:
    text = f"{caption or ''} {hashtags or ''}".lower()
    for category, keywords in KEYWORD_RULES:
        if any(kw in text for kw in keywords):
            return category
    return DEFAULT_CATEGORY


# ---------------------------------------------------------------------------
# Moral language regex patterns — Phase 4 of the scaling plan.
# These extract structured signals from caption text.
# ---------------------------------------------------------------------------

# Match "30g protein", "30 g protein", "Protein: 30g", "30g P", "208g protein"
PROTEIN_GRAMS_PATTERNS = [
    re.compile(r"(\d+)\s*g(?:rams)?\s+(?:of\s+)?protein", re.IGNORECASE),
    re.compile(r"protein\s*:?\s*(\d+)\s*g(?:rams)?\b", re.IGNORECASE),
    re.compile(r"(\d+)\s*g\s+p(?:ro)?\b", re.IGNORECASE),
    re.compile(r"(\d+)\s*g\s*p\s*\|", re.IGNORECASE),  # "31g P |" macro-line format
]

# Speed / efficiency vocabulary
SPEED_WORDS = [
    "minute", "minutes", "quick", "easy", "easiest", "fast",
    "simple", "5-minute", "5 minute", "no fuss", "no bake",
    "no-bake", "low effort",
]

# Guilt-free framing
GUILT_FREE_PATTERNS = [
    "guilt free", "guilt-free", "guiltfree",
    "without wrecking", "crush sweet cravings",
    "during a cut", "low calorie", "lowcalorie",
]

# Fuel / optimization framing
FUEL_PATTERNS = [
    "fuel", "optimize", "optimization", "lock in",
    "macros", "gains", "shred", "bulking", "cutting",
    "calorie deficit", "caloriedeficit",
]

# Brand / ad markers
AD_MARKERS = [
    "#ad", "partner", "partnership", "code ", "discount",
    "link in bio", "cookbook", "ebook", "use code",
    "biggest discount",
]


def extract_protein_grams(text: str) -> list[int]:
    """Return all protein gram amounts mentioned (deduped, sorted)."""
    found = set()
    for pattern in PROTEIN_GRAMS_PATTERNS:
        for match in pattern.findall(text):
            try:
                found.add(int(match))
            except (ValueError, TypeError):
                pass
    return sorted(found)


def count_keyword_hits(text: str, keywords: list[str]) -> int:
    """Count distinct keywords from `keywords` that appear in `text`."""
    text_lower = text.lower()
    return sum(1 for kw in keywords if kw in text_lower)


def has_any(text: str, patterns: list[str]) -> bool:
    text_lower = text.lower()
    return any(p in text_lower for p in patterns)


def analyze_moral_language(caption: str, hashtags: str) -> dict:
    text = f"{caption or ''} {hashtags or ''}"
    grams = extract_protein_grams(text)
    return {
        "regex_protein_grams": ";".join(str(g) for g in grams),
        "regex_protein_grams_max": max(grams) if grams else "",
        "regex_protein_grams_count": len(grams),
        "regex_speed_marker_count": count_keyword_hits(text, SPEED_WORDS),
        "regex_guilt_free": has_any(text, GUILT_FREE_PATTERNS),
        "regex_fuel_language": has_any(text, FUEL_PATTERNS),
        "regex_ad_markers": has_any(text, AD_MARKERS),
    }


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------

OUTPUT_COLUMNS = [
    "id",
    "manual_category",
    "regex_category",
    "agreement_regex_vs_manual",
    "caption_length",
    "hashtag_count",
    "regex_protein_grams",
    "regex_protein_grams_max",
    "regex_protein_grams_count",
    "regex_speed_marker_count",
    "regex_guilt_free",
    "regex_fuel_language",
    "regex_ad_markers",
]


def main():
    src = Path("/mnt/user-data/uploads/FINAL_tiktok_protein_dataset.csv")
    dst = Path("/mnt/user-data/outputs/tiktok_protein_regex_classifications.csv")
    dst.parent.mkdir(parents=True, exist_ok=True)

    with src.open("r", newline="") as f:
        rows = list(csv.reader(f))

    header = rows[0]
    idx = {col: header.index(col) for col in
           ["id", "caption", "hashtags", "cultural_theme"]}

    out_rows = [OUTPUT_COLUMNS]
    for row in rows[1:]:
        vid = row[idx["id"]]
        caption = row[idx["caption"]] or ""
        hashtags = row[idx["hashtags"]] or ""
        manual_cat = row[idx["cultural_theme"]]

        regex_cat = keyword_classify(caption, hashtags)
        moral = analyze_moral_language(caption, hashtags)

        # Hashtag count: split on comma, strip, filter non-empty
        hashtag_list = [h.strip() for h in hashtags.split(",") if h.strip()]

        out_rows.append([
            vid,
            manual_cat,
            regex_cat,
            "yes" if regex_cat == manual_cat else "no",
            len(caption),
            len(hashtag_list),
            moral["regex_protein_grams"],
            moral["regex_protein_grams_max"],
            moral["regex_protein_grams_count"],
            moral["regex_speed_marker_count"],
            "yes" if moral["regex_guilt_free"] else "no",
            "yes" if moral["regex_fuel_language"] else "no",
            "yes" if moral["regex_ad_markers"] else "no",
        ])

    with dst.open("w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerows(out_rows)

    print(f"Wrote {len(out_rows) - 1} rows × {len(OUTPUT_COLUMNS)} cols to:")
    print(f"  {dst}")
    return out_rows


if __name__ == "__main__":
    main()
