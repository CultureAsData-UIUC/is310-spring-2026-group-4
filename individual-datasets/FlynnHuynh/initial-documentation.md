# How Immigrant Dishes Are Narrated in American Food Media

**IS310 | Individual Dataset — Initial Submission**  
**Author:** Flynn Huynh
**Repository:** `is310-spring-2026-group-4`

---

## What Is This Dataset?

This dataset documents how six chosen immigrant-origin dishes are represented, framed, and narrated across contemporary American food sources (2020–2026). Each entry captures a single source — a recipe site, food media article, corporate page, or reference encyclopedia — and records structured observations about how that source handles (or avoids) questions of cultural origin, authenticity, and community credit.

The dataset contains **50 entries** across six dishes, with source counts ranging from eight to nine per dish.

---

## Cultural Materials and Approach

### The cultural question

When immigrant dishes enter mainstream American food culture, something happens to their stories. Orange Chicken gets sold as "Chinese food" at Panda Express without any acknowledgment that it has no equivalent in China. Fortune cookies appear in every American Chinese restaurant as a symbol of Chinese culture, despite originating in Japanese-American communities in San Francisco. Spaghetti and meatballs is listed in Italian cookbooks as a timeless classic, even though the dish as a combined plate was invented by Italian immigrants in New York when affordable meat became available to them for the first time.

These dishes share a structure: they were created by or for immigrant communities navigating American ingredients, American tastes, and American economics — and then their stories were either erased, simplified, or appropriated as they entered the mainstream. This dataset asks: how is that story (or its absence) distributed across different types of sources today?

### Approach: Create from Scratch

This dataset was created from scratch through close manual review of each source. Rather than downloading an existing food dataset, each of the 50 entries required visiting a source, reading it for cultural framing, and making interpretive coding decisions. The goal was to experience the labor of data creation directly — to understand what gets captured, what gets left out, and how those decisions compound across a dataset.

---

## Dataset Structure

Each row represents **one source about one dish**. The unit of analysis is the source-dish pair, not the dish alone, because the central research question is about how narration varies across source types rather than about the dish itself.

| Column | Description |
|---|---|
| `entry_id` | Unique ID in format DISH_CODE-NUMBER (e.g., OC-01 for Orange Chicken source 1) |
| `dish_name` | Name of the dish |
| `immigrant_community` | Immigrant community associated with the dish's origin |
| `transformation_type` | Category of Americanization (see below) |
| `source_name` | Publication or website name |
| `source_type` | Category of source (Community Food Blog, Mainstream Recipe Aggregator, Corporate/Brand, Food Media, Food Media/Regional, Reference/Encyclopedia, YouTube Cooking Channel) |
| `author_background` | Creator identity when identifiable |
| `year_published` | Year of publication or most recent update |
| `url` | Direct URL to source |
| `origin_story_mentioned` | Whether the source mentions the dish's cultural/historical origin (Yes / No / Partial) |
| `origin_story_framing` | How origin is framed when present (omitted / simplified / mythologized / detailed_historical / corrective / contested) |
| `authenticity_framing` | How the source positions the dish relative to authenticity (claimed / distanced / dismissed / contested / reclaimed / not_mentioned) |
| `notable_substitutions` | Key ingredient or technique changes from traditional versions, when a recipe is present |
| `community_credit_given` | Whether the originating immigrant community is named and credited (Yes / No / Partial / N/A) |
| `annotation_notes` | Free-text interpretive note explaining the coding decisions for that entry |

### Transformation type categories

- **Pure American Invention**: Dish does not exist in the origin country (e.g., Orange Chicken)
- **Significant Adaptation**: Dish elements exist in origin country but the combination or form is American (e.g., Spaghetti and Meatballs)
- **American Regional Invention**: Created by immigrants in a specific American location (e.g., Mission Burrito)
- **Border Invention (Tex-Mex)**: Created at the US-Mexico border, often specifically for American customers (e.g., Nachos)
- **Misattribution**: Dish is culturally attributed to the wrong immigrant community (e.g., Fortune Cookie)

---

## Dish and Source Selection

### Why these six dishes

The six dishes were selected to ensure:

1. **Coverage across transformation types** — The dataset includes a pure American invention (Orange Chicken), a misattribution (Fortune Cookie), American inventions inspired by technique (Chicken Parmesan), a significant adaptation (Spaghetti and Meatballs), a border invention (Nachos), and a regional American invention (Mission Burrito). This variety allows comparison of how different transformation types are narrated.

2. **Three immigrant communities** — Chinese-American, Italian-American, and Mexican-American. These three communities represent different historical waves of immigration, different levels of mainstream food media visibility, and different relationships to the question of authenticity in American food culture.

3. **Documentation availability** — All six dishes have substantial contemporary documentation (2020–2026) across multiple source types, making cross-source comparison possible.

Dishes originally considered but excluded include Chicken Tikka Masala (UK-to-US transformation adds complexity that exceeds the scope of this dataset) and New York-Style Bagel (fewer recipe sources with origin framing). These may be added in the scaling phase.

### Why eight sources per dish

The base structure is eight sources per dish, with two dishes receiving a ninth entry to reach the 50-item threshold. The eight core sources were selected to represent a structured range:

- **2 recipe sources from community-adjacent blogs** (e.g., The Woks of Life, Chicano Eats, Lidia's Italy) — these represent voices closest to the originating communities
- **2 mainstream recipe aggregators** (AllRecipes, NYT Cooking, Food Network) — highest-traffic platforms with the broadest reach
- **2 food media articles** (Serious Eats, Eater, Bon Appétit, regional outlets) — editorial sources with varying levels of cultural engagement
- **1 corporate/brand source** (where applicable — Panda Express, Chipotle)
- **1 reference/encyclopedia entry** (TasteAtlas, Smithsonian) — structured reference sources

Two supplementary ninth entries were added to reach the 50-item minimum: a YouTube cooking channel source for Orange Chicken (Made With Lau, OC-09) and an America's Test Kitchen entry for Nachos (NA-09). The YouTube entry also introduces a new source type not otherwise represented in the dataset — video-format community cooking channels — which will be an important category to expand in the scaling phase.

### What was excluded

**Community discussions (Reddit, YouTube comments)**: Originally planned, but excluded from this submission for two reasons. First, coding qualitative sentiment across comment threads requires substantially more entries to be meaningful. Second, consistent anonymization and ethical handling of social media data exceeds what is feasible in a 50-item bespoke dataset; this dimension is better suited to the scaling phase using structured scraping with clear methodology.

**Sources before 2020**: To keep the dataset focused on contemporary narration practices, sources are limited to 2020–2026. Historical framing is captured in the `annotation_notes` field when sources discuss older origins, but the sources themselves are contemporary.

**Non-English sources**: This dataset focuses on how these dishes are narrated in English-language American food media. Spanish-language, Italian-language, or Cantonese-language sources would be valuable for comparison but fall outside the scope of this phase.

---

## Computational Tools Used

### annotation_helper.py

The primary computational tool is `annotation_helper.py`, a Python script that uses the Anthropic Claude API to assist with coding the qualitative fields (`origin_story_mentioned`, `origin_story_framing`, `authenticity_framing`, `community_credit_given`, and `annotation_notes`).

**How it was used**: For each source, relevant text — typically the recipe headnote, article introduction, or reference description — was pasted into the annotation helper. The script sent this text to Claude with a detailed system prompt specifying the coding scheme and category definitions. Claude returned a structured JSON annotation, which was then reviewed, evaluated, and either accepted or revised before being added to the dataset.

This workflow reflects the assignment's intent: computation augmented manual work rather than replacing it. Every entry was still manually reviewed and every annotation was evaluated for accuracy. The script accelerated the consistent application of the coding scheme across 50 entries and helped surface cases where my category definitions were ambiguous.

**Limitations**: 
- The tool depends on the quality of the text excerpt provided. For recipe sources where cultural framing is absent from headnotes, the tool reliably coded `origin_story_mentioned` as No — but couldn't distinguish between deliberate omission and structural absence (i.e., the site simply doesn't include headnotes at all). This distinction was added manually in `annotation_notes`.
- For corporate sources (Panda Express, Chipotle), the promotional framing occasionally caused the model to code `authenticity_framing` as `claimed` when the more accurate coding was `not_mentioned` — the corporate source wasn't claiming authenticity so much as simply not engaging with the question. These cases were corrected manually.
- The tool cannot visit URLs or read visual design cues (photography, layout), which are themselves meaningful data points about how a source positions a dish culturally. This limitation is acknowledged.
- For the YouTube source (Made With Lau, OC-09), the annotation helper was given a text transcript excerpt rather than the video itself. Tone, visual framing, and spoken commentary that doesn't appear in transcripts are meaningful dimensions of how video sources narrate food culture — and are invisible to text-based annotation tools. This is a limitation that becomes more significant if YouTube channels are expanded in the scaling phase.

---

## Interpretive Decisions and Challenges

### The hardest coding decision: `community_credit_given`

Whether community credit is "given" required distinguishing between surface-level naming ("this is a Chinese-American dish") and substantive crediting that acknowledges immigrant labor, historical context, or community contribution. In practice, this distinction proved hard to operationalize consistently. 

For example, TasteAtlas entries typically name the community of origin but provide no cultural depth — these were coded as `Partial` rather than `Yes`. But the line between a "sufficient" and "insufficient" acknowledgment is inherently interpretive, and a different researcher might draw it differently. This is the kind of decision that gets hidden when datasets are downloaded without documentation.

### Tension: food media vs. recipe sources

A pattern emerged immediately: food media articles (Eater, Serious Eats, Bon Appétit) engage far more consistently with origin stories than recipe aggregators (AllRecipes, Food Network). But this may reflect structural differences as much as intentional choices — articles have space for headnotes and cultural context that recipe cards do not. It is difficult to distinguish deliberate erasure from format constraints, and the dataset does not resolve this tension; it documents it.

### What the data can and cannot say

This dataset can describe how different source types frame immigrant-origin dishes. It cannot explain why those framings exist — whether they reflect editorial policy, SEO optimization, author background, or audience expectations. That explanatory layer would require different methods (interviews, editorial research) beyond the scope of this phase.

---

## Patterns and Questions That Emerged

Working through 50 entries manually made several patterns visible:

**Community food blogs consistently provide the richest historical framing.** Sources like The Woks of Life, Chicano Eats, and Lidia's Italy were the most likely to name immigrant communities, explain transformation processes, and reclaim the dish as a valid diaspora tradition. This is not surprising, but the consistency is notable.

**YouTube community channels behave more like community blogs than recipe aggregators.** The single YouTube entry in this dataset (Made With Lau, OC-09) matched community food blogs in depth of cultural framing and community credit — suggesting that video-format immigrant creators occupy a similar cultural role to written community bloggers. This warrants expanding YouTube coverage in the scaling phase.

**Mainstream recipe aggregators systematically omit cultural context.** AllRecipes and Food Network entries almost never mention origin stories. The result is that the highest-traffic sources — the ones most people encounter — strip these dishes of their immigrant histories.

**Corporate sources appropriate community identity without substantive acknowledgment.** Panda Express and Chipotle both claim cultural connections (Chinese food heritage; Mission-style burritos) through branding while omitting the immigrant communities that created those traditions. This is documented but not evaluable as intentional without further research.

**The Fortune Cookie is the most contested entry in the dataset.** Because the misattribution is itself the cultural story, sources that engage with it at all tend to engage deeply. Sources that omit it are omitting more than a footnote — they are reinforcing a factual error.

**"Authenticity" is almost never engaged with substantively in recipe aggregators.** The word does not appear; neither does its absence get marked. Authenticity debates, which are active in food media and community discussions, are structurally invisible in recipe-format sources.

---

## Next Steps: Scaling Plan

### How to generate more data computationally

After Spring Break, this dataset will be scaled from 50 items to 500–1,000+ using a combination of approaches:

**Option 1 (primary): Scale up via web scraping and LLM-assisted annotation**

The most natural extension is to expand the source coverage for each dish and add more dishes (targeting 15–20 total, including Indian-American and Jewish-American dishes). The `annotation_helper.py` script is already structured to accept source text and return coded JSON — the scaling phase will wrap this in an automated pipeline:

1. **Web scraping with BeautifulSoup**: For recipe aggregators and food media sites that permit scraping (verified against `robots.txt`), Python scripts will extract recipe headnotes, article introductions, and metadata automatically.
2. **LLM-assisted bulk annotation**: The annotation helper's prompt and coding scheme will be applied programmatically to scraped text, generating draft annotations for human review.
3. **Batch API calls**: The Anthropic Batch API can process many annotation requests simultaneously at lower cost, enabling 500+ items within the API tier.

**Option 2 (supplementary): Merge with existing food datasets**

The [Epicurious Recipes dataset (Kaggle)](https://www.kaggle.com/datasets/hugodarwood/epirecipes) contains ~20,000 recipes from Epicurious with ingredient lists and categories. For the dishes in this dataset, that corpus could be queried to analyze how ingredient substitutions (e.g., mozzarella quantity, meat type in meatballs) vary across a large recipe corpus — adding a quantitative dimension to the qualitative framing analysis.

### What will change when scaling

**What changes**: At 500+ items, individual review of every entry is no longer feasible. The interpretive labor of deciding whether a source "gives community credit" — which was done manually for 50 entries — must be either operationalized into rules precise enough for an LLM to apply consistently, or relaxed into a coarser coding scheme. This is the central challenge: the categories that were most analytically interesting in the bespoke phase are also the hardest to automate reliably.

**What to automate**: `origin_story_mentioned` (Yes/No/Partial) and `source_type` are the most automatable fields — they depend on structural features (does this text mention origin?) that LLMs handle well. `author_background` can be partially automated by scraping byline information and matching against known community bloggers.

**What to keep manual**: `authenticity_framing` and `community_credit_given` require contextual judgment that is more error-prone to automate. The scaling plan will use LLM annotations for these fields as draft annotations that are reviewed in batches rather than individually.

**Anticipated technical challenges**:
- Paywalls on NYT Cooking, Bon Appétit, and some Eater content limit automated scraping
- `robots.txt` compliance rules out some high-traffic sources (AllRecipes disallows many scrapers)
- LLM annotation consistency may drift across large batches; prompt calibration will require testing
- Adding new communities (Indian-American, Jewish-American) requires new source research before automation can begin
- Expanding YouTube coverage will require working with video transcripts (via YouTube's auto-caption API) rather than written text, adding a preprocessing step before annotation can be applied
