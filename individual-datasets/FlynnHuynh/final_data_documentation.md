# Dataset Documentation: How Immigrant Dishes Are Narrated in American Food Media

**IS310 - Culture As Data | Spring 2026**  
**Author:** Flynn Huynh  
**Version:** Final (May 2026) - built upon the initial submission documentation  
**Repository:** `is310-spring-2026-group-4`

---

## Quick Reference

| | |
|---|---|
| **File** | `immigrant_dish_dataset_merged.csv` |
| **Total entries** | 500 |
| **Bespoke (manual)** | 50 |
| **Computationally scaled** | 450 |
| **Fully annotated** | 135 (50 bespoke + 85 scaled) |
| **Dishes covered** | 6 |
| **Immigrant communities** | 3 (Chinese-American, Italian-American, Mexican-American) |
| **Source date range** | 2010–2025 (bespoke entries only; scaled entries lack year) |
| **Annotation tool** | Google Gemini API (`gemini-2.5-flash`, free tier) |
| **URL discovery** | DuckDuckGo Search via `ddgs` library |

---

## What Is This Dataset?

This dataset documents how six immigrant-origin dishes are represented, framed, and narrated across contemporary American food sources. Each entry captures a single source - a recipe site, food media article, corporate page, reference encyclopedia, or YouTube cooking channel - and records structured observations about how that source handles (or avoids) questions of cultural origin, community credit, and cultural ownership.

The dataset was constructed in two phases: a 50-entry bespoke phase built through close manual review of each source, and a 450-entry computational scaling phase using automated URL discovery, web scraping, and LLM-assisted annotation. Both phases are preserved in the merged file.

---

## Column Reference

| Column | Type | Description |
|---|---|---|
| `entry_id` | String | Unique ID in format `DISH_CODE-NUMBER` (e.g., `OC-01`). Dish codes: OC = Orange Chicken, FC = Fortune Cookie, CP = Chicken Parmesan, SM = Spaghetti and Meatballs, NA = Nachos, MB = Mission Burrito |
| `dish_name` | String | Name of the dish |
| `immigrant_community` | String | Immigrant community associated with the dish's origin |
| `transformation_type` | String | Category of Americanization (see below) |
| `source_name` | String | Publication or website name |
| `source_type` | String | Category of source (see below) |
| `author_background` | String | Creator identity when identifiable |
| `year_published` | Integer | Year of publication. **Populated for bespoke entries only (2010–2025); blank for scaled entries** |
| `url` | String | Direct URL to source |
| `scrape_status` | String | `bespoke` / `ok` / `partial_paywall` / `robots_blocked` / `failed` |
| `scraped_excerpt` | String | Text excerpt sent to Gemini for annotation. Empty for bespoke entries and blocked/failed scrapes |
| `origin_story_mentioned` | String | `Yes` / `No` / `Partial` / blank (unannotated) |
| `origin_story_framing` | String | `omitted` / `simplified` / `mythologized` / `detailed_historical` / `corrective` / `contested` / blank |
| `cultural_ownership_framing` | String | `claimed` / `distanced` / `dismissed` / `contested` / `reclaimed` / `not_mentioned` / blank |
| `notable_substitutions` | String | Key ingredient/technique changes from traditional versions. **Populated for bespoke entries only** |
| `community_credit_given` | String | `Yes` / `No` / `Partial` / `N/A` / blank (unannotated) |
| `annotation_notes` | String | Interpretive note explaining coding decisions, or `annotation_failed` / `skipped - [reason]` for unannotated entries |
| `rationale` | String | Single key phrase or structural feature that drove the coding. Populated for scaled annotated entries; blank for bespoke |

---

## Coding Scheme

### `transformation_type`
- **Pure American Invention** - dish does not exist in origin country (Orange Chicken)
- **Misattribution (Japanese-American origin)** - culturally attributed to wrong community (Fortune Cookie)
- **American Invention (inspired by Italian technique)** - created by immigrants in US (Chicken Parmesan)
- **Significant Adaptation** - elements exist in origin country but the combined form is American (Spaghetti and Meatballs)
- **Border Invention (Tex-Mex)** - created at US-Mexico border for American customers (Nachos)
- **American Regional Invention (San Francisco)** - created by immigrants in specific US city (Mission Burrito)

### `source_type`
- **Community Food Blog** - authored by member(s) of the immigrant community
- **Mainstream Recipe Aggregator** - high-traffic recipe platforms (AllRecipes, Food Network, NYT Cooking)
- **Food Media** - editorial food publications (Serious Eats, Eater, Bon Appétit, Food & Wine)
- **Food Media/Journalism** - journalism outlets covering food (Smithsonian, NPR)
- **Food Media/Regional** - regional food journalism (SF Chronicle, Texas Monthly, LA Times)
- **Reference/Encyclopedia** - structured reference sources (TasteAtlas, The Food Timeline)
- **Corporate/Brand** - official brand or company websites (Panda Express, Chipotle)
- **YouTube Cooking Channel** - video-format cooking channels

### `origin_story_mentioned`
- **Yes** - source explicitly discusses the dish's cultural or historical origin
- **No** - no mention of origin at all
- **Partial** - vague or passing mention without depth

### `origin_story_framing`
- **omitted** - not discussed
- **simplified** - brief, surface-level mention
- **mythologized** - uncritical romantic narrative that flattens complexity
- **detailed_historical** - engages with immigration history, transformation process, named actors
- **corrective** - actively corrects a common misconception about origin
- **contested** - acknowledges multiple or disputed origin claims exist

### `cultural_ownership_framing`
How does the source position the dish relative to the immigrant community that created it?
- **claimed** - presents dish as native/authentic to a cultural tradition (often without acknowledging its American invention)
- **distanced** - acknowledges the dish is an American adaptation, presents it positively
- **dismissed** - actively argues that cultural origins are irrelevant
- **contested** - acknowledges ongoing debate about who the dish culturally belongs to
- **reclaimed** - a community member asserts the dish as a legitimate part of their own cultural tradition
- **not_mentioned** - cultural ownership is never raised

### `community_credit_given`
- **Yes** - the immigrant community is named and substantively credited (labor, history, context)
- **No** - no credit given; dish treated as cultureless or simply mainstream American
- **Partial** - community mentioned by name but without substantive acknowledgment of their role
- **N/A** - not applicable (e.g., pure reference entry with no narrative framing)

---

## Dataset Distribution

### By dish
| Dish | Community | Total | Fully Annotated | Robots Blocked |
|---|---|---|---|---|
| Orange Chicken | Chinese-American | 164 | 24 | 70 |
| Fortune Cookie | Chinese-American | 127 | 37 | 41 |
| Chicken Parmesan | Italian-American | 88 | 27 | 35 |
| Spaghetti and Meatballs | Italian-American | 84 | 29 | 34 |
| Nachos | Mexican-American | 29 | 10 | 8 |
| Mission Burrito | Mexican-American | 8 | 8 | 0 |

### By source type (all 500 entries)
| Source Type | Count |
|---|---|
| Food Media | 437 |
| Mainstream Recipe Aggregator | 30 |
| Reference/Encyclopedia | 11 |
| YouTube Cooking Channel | 8 |
| Community Food Blog | 5 |
| Food Media/Journalism | 5 |
| Corporate/Brand | 2 |
| Food Media/Regional | 2 |

### Scaled entries by scrape status
| Status | Count | Meaning |
|---|---|---|
| `ok` | 217 | Successfully scraped |
| `robots_blocked` | 188 | Site disallows scraping; entry has metadata only |
| `failed` | 45 | Network/HTTP error; entry has metadata only |

### Of the 217 successfully scraped entries
| Annotation outcome | Count |
|---|---|
| Successfully annotated | 85 |
| `annotation_failed` (Gemini returned malformed/no response) | 122 |
| `skipped` (robots_blocked or failed - not sent to Gemini) | 243 |

---

## Key Findings (from fully annotated entries, n=135)

| Field | Most common value | Count | % |
|---|---|---|---|
| `origin_story_mentioned` | No | 81 | 60% |
| `origin_story_framing` | omitted | 83 | 61% |
| `cultural_ownership_framing` | not_mentioned | 79 | 59% |
| `community_credit_given` | N/A | 47 | 35% |

Community Food Blogs: 100% mention origin (5/5), 80% give full community credit (4/5)  
Mainstream Recipe Aggregators: 8% mention origin (1/13), 0% give full community credit (0/13)  
Corporate/Brand sources: 0% mention origin (0/2), 0% give full community credit (0/2)

---

## Computational Tools

### `annotation_helper.py`
Interactive command-line tool for annotating individual source excerpts. Uses Gemini API (`gemini-2.5-flash`) with a structured system prompt defining the coding scheme. Used for all 50 bespoke entries. Enforces 60-second rate limiting between requests to respect free-tier quota.

**Key design choice:** `authenticity_framing` was renamed to `cultural_ownership_framing` in response to my instructor feedback that "authenticity" may prompt the model to evaluate culinary accuracy rather than the research question of community attribution. The revised prompt asks specifically how the source positions the dish relative to the immigrant community that created it.

### `scale_dataset.py`
Batch pipeline for automated dataset scaling. Executes pre-written DuckDuckGo search queries, collects URLs, scrapes text with BeautifulSoup (respecting `robots.txt`), annotates with Gemini, and writes results to a progress checkpoint file. The final merged dataset is produced by combining the bespoke CSV with the scaled progress CSV.

Features: resumable via `_scaled_progress.csv` (URL-level) and `_query_checkpoint.txt` (query-level); automatic detection and handling of daily quota exhaustion (sleeps until midnight PT, then resumes); per-minute rate limit retry logic.

---

## Known Limitations

1. **Annotation gap**: Only 135 of 500 entries are fully annotated. The remaining 365 are metadata-only records. Analysis of framing fields should be confined to the 135 annotated entries.

2. **`notable_substitutions` not carried forward at scale**: This field documents ingredient changes from traditional versions and is populated for bespoke entries only. Quantitative ingredient analysis is not possible at scale with current data.

3. **`year_published` missing for scaled entries**: Temporal analysis is not possible with the current dataset.

4. **Source type skew in scaled data**: DuckDuckGo results are dominated by Food Media articles. The controlled source type diversity of the bespoke phase is not preserved in the scaled data.

5. **Dish and community imbalance**: Chinese-American dishes (291 entries) are dramatically overrepresented relative to Mexican-American dishes (37 entries). This reflects web content volume, not research design intent.

6. **No community member input**: The coding scheme was defined without input from the communities whose food histories are being tracked. The interpretive categories reflect one researcher's positionality.

---

## Files in This Folder

```
FlynnHuynh/
|- immigrant_dish_dataset_merged.csv   <- final merged dataset
|- final-data-essay.md                 <- scholarly essay
|- final-documentation.md              <- this file
|- annotation_helper.py                <- interactive annotation tool from Phase One(Gemini)
|- Individual Inital Dataset_IS310_Flynn Huynh - immigrant_dish_dataset.csv        
|- scale_dataset.py                    <- batch scaling pipeline
|- instructor_feedback.md (preserved)  <- instructor's comment for Phase One
|_ initial-documentation.md            <- initial submission documentation (preserved)
```

---

## How to Use This Dataset

**For qualitative analysis of framing**: work with the 135 fully annotated entries (filter where `origin_story_mentioned` is not blank and `annotation_notes` does not contain `annotation_failed`).

**For source coverage analysis**: all 500 entries are usable - URL, source name, dish, community, and scrape status are populated for every entry.

**For bespoke-phase analysis only**: filter `scrape_status == "bespoke"` for the 50 manually coded entries with full field population including `notable_substitutions`.