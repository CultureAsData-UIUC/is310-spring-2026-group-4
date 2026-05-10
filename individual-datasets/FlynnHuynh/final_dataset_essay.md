# How Immigrant Dishes Are Narrated in American Food Media: A Data Essay

**IS310 - Culture As Data | Spring 2026**  
**Flynn Huynh**  
**My Dataset:** `immigrant_dish_dataset_merged.csv`  
**Final submission - May 2026**

---

## I. Introduction: The Question Behind the Data

When you search for an Orange Chicken recipe online, you are unlikely to learn that the dish has no equivalent in China, that it was engineered for American palates by a Taiwanese-born chef at a California fast food chain, or that its ubiquity in Chinese-American restaurants reflects decades of immigrant communities adapting to survive in a market that expected a particular kind of "Chinese food." You will probably just get a recipe.

I intended to built this dataset to make that silence visible, to document, systematically and at scale, how six immigrant-origin dishes are narrated across contemporary American food media. The central question is not whether any individual source is accurate or inaccurate, but more about how narration varies across source types: Do community food blogs frame these dishes differently than recipe aggregators? Does corporate food media engage with immigrant history differently than regional journalism? And what does it mean that the top highest-traffic platforms, the ones most people actually use, are the ones most likely to say nothing at all?

The six dishes I include: **Orange Chicken and Fortune Cookie (Chinese-American), Chicken Parmesan and Spaghetti and Meatballs (Italian-American), Nachos and Mission Burrito (Mexican-American)**. They were selected because I believe they share a particular structure. Each was created by or for immigrant communities navigating American ingredients, American economics, and American tastes. Each has since been absorbed into the American mainstream. And in that absorption, each dish's story was either erased, simplified, appropriated, or in rare cases, reclaimed. The dataset anticipated to track which of those outcomes each source produces.

---

## II. How the Data Was Made

### Phase One: Bespoke Manual Dataset (50 entries)

The first phase involved creating 50 entries entirely by hand, visiting each source, reading it carefully, and making interpretive coding decisions about five qualitative fields: `origin_story_mentioned`, `origin_story_framing`, `cultural_ownership_framing`, `community_credit_given`, and `annotation_notes`. Each dish received eight to nine sources, selected to represent a structured range of source types: community food blogs, mainstream recipe aggregators, food media articles, corporate and brand sources, reference encyclopedias, and a YouTube cooking channel.

To assist with consistent annotation, I built `annotation_helper.py`, a Python script that sends source text excerpts to the Google Gemini API (free tier, `gemini-2.5-flash` model) and returns a structured JSON annotation. The script was deliberately designed as an ***augmentation*** tool, not a replacement for manual review. Every annotation the model returned was read, evaluated, and either accepted or revised. In roughly 15–20% of bespoke entries, the model's output was corrected - most commonly on `cultural_ownership_framing`, where Gemini tended to code corporate sources as `claimed` when `not_mentioned` was more accurate, and on `community_credit_given`, where surface-level naming of a community was sometimes coded as `Partial` when it warranted `No`.

One case is worth describing concretely, as my instructor specifically noted the value of making the human-model disagreement visible. For Bon Appétit's Orange Chicken entry (OC-08), Gemini returned `cultural_ownership_framing: claimed`, reasoning that the source's framing as a Chinese-American comfort food constituted a cultural claim. I disagree since the source made no such claim. It simply presented the dish without any cultural framing whatsoever, and "claiming" implies an active assertion that was entirely absent. The correct coding was `not_mentioned`. This distinction matters in my opinion: a source that actively claims a dish as culturally authentic is doing something meaningfully different from a source that never raises the question. The model conflated presence of a dish's ethnic adjective with active cultural positioning, which are not the same thing.

### Phase Two: Computational Scaling (450 entries)

After Spring Break 2026, the dataset was scaled from 50 to 500 entries using `scale_dataset.py`, a pipeline I built around three components: DuckDuckGo search for automatic URL discovery (via the `ddgs` library, no API key required), BeautifulSoup for web scraping, and the Gemini API again for bulk annotation.

The pipeline worked by executing 48 pre-written search queries - about eight per dish - through DuckDuckGo, collecting up to ten URLs per query (~480 candidate URLs), deduplicating them against the existing dataset, scraping each new URL for relevant text, and sending that text to Gemini for annotation. A checkpoint system (`_scaled_progress.csv` for processed URLs and `_query_checkpoint.txt` for completed queries) made the process fully resumable across sessions - critical because the Gemini free tier enforces a daily cap of 20 requests, meaning the pipeline ran across approximately seven days of interrupted sessions.

I also engineered the script to handle the daily quota exhaustion gracefully: when the API returned a `GenerateRequestsPerDay` error, rather than failing silently, it calculated the exact time until midnight Pacific and paused until the quota reset, then automatically retried the failed entry. This behavior was not in the original script code, but it was patched after I noticed how the first overnight run hit the daily cap at entry OC-134 and proceeded to scrape dozens of URLs it could not annotate.

---

## III. What the Data Contains

The final merged dataset contains **500 entries** across six dishes and three immigrant communities, combining the 50 bespoke manually-coded entries with 450 computationally-generated ones. The dataset spans sources published between 2010 and 2025.

### Distribution by dish and community

| Dish | Community | Total Entries | Fully Annotated |
|---|---|---|---|
| Orange Chicken | Chinese-American | 164 | 24 |
| Fortune Cookie | Chinese-American | 127 | 37 |
| Chicken Parmesan | Italian-American | 88 | 27 |
| Spaghetti and Meatballs | Italian-American | 84 | 29 |
| Nachos | Mexican-American | 29 | 10 |
| Mission Burrito | Mexican-American | 8 | 8 |

The severe imbalance in this distribution - Chinese-American dishes make up 291 of 500 entries (58%), while Mexican-American dishes total only 37 (7%) - is itself a finding about the web, not just about my search queries. I believe that The DuckDuckGo results reflect the actual volume of online content about these dishes. Orange Chicken alone generated 164 entries because the web is saturated with it: restaurant chains, recipe aggregators, food media, and brand marketing have all produced enormous amounts of content about Panda Express's signature dish. Mission Burrito generated only 8 entries, potentially because, despite being a culturally significant dish, it occupies a much narrower slice of English-language food media. The dataset does not merely represent my topic but also represents the topology of food media attention on the web.

### The annotation gap

Of the 450 computationally-scaled entries, only **85 were successfully annotated** (19%). The remainder broke down as follows:

- **188 entries (42%)** were `robots_blocked` - sites that disallow automated scraping via `robots.txt`. Wikipedia, Reddit, homesicktexan.com, and several recipe aggregators fall into this category.
- **45 entries (10%)** returned scrape failures - timeouts, 404 errors, or sites that delivered no usable text.
- **122 entries (27%)** were scraped successfully but Gemini returned a malformed response or exhausted its daily quota before the annotation could complete (`annotation_failed`).

This means the dataset's 500 entries represent three distinct epistemic categories: 50 entries that are fully and manually annotated, 85 that are computationally annotated with Gemini and reviewed in batch, and 365 that are metadata-only records (URL, source name, dish, community, scrape status) with no annotation. All 500 entries are preserved in the dataset because the metadata itself is analytically meaningful - a `robots_blocked` entry from Reddit, for example, tells us something about where these conversations are happening even if we cannot access the content.

---

## IV. What the Data Reveals

All quantitative findings below should be read as patterns drawn primarily from the 135 fully annotated entries (50 bespoke + 85 scaled), not the full 500.

### Finding 1: The mainstream web systematically omits origin stories

Of the 135 fully annotated entries, **81 (60%) have `origin_story_mentioned: No`** - meaning the source failed to provide any sort of historical or cultural context for the dish. Only 46 entries (34%) explicitly mention origin. When framing is coded, `omitted` is the single most common value (83 entries, 61%), meaning that even among sources that do mention something, the treatment is often so thin it barely registers.

This pattern is not evenly distributed across source types. In the bespoke dataset I mentioned in **Phase One** above, where source type distribution was deliberately controlled, the contrast is stark: every Community Food Blog entry (5/5) mentioned the dish's origin, compared to just 1 of 13 Mainstream Recipe Aggregator entries. Both Corporate/Brand entries gave `No`. The pattern suggests that the question of a dish's cultural history is structurally present in community-facing sources and structurally absent in high-traffic mainstream ones. The absence is systematic and should not be treated as random noise.

### Finding 2: Cultural ownership is invisible in the majority of sources

**79 of 135 annotated entries (59%) have `cultural_ownership_framing: not_mentioned`** - meaning the source never raises the question of who the dish culturally belongs to. The second most common value is `claimed` (16 entries), which in this context typically means a source implicitly presents a dish as belonging to a cuisine (e.g., Italian food, Chinese takeout) without acknowledging that it is actually a diaspora invention. Only 13 entries (10%) are coded `reclaimed` - cases where a community member explicitly asserts the dish as a valid part of their own cultural tradition.

The `reclaimed` coding is disproportionately concentrated in Community Food Blog and YouTube sources. This is consistent with the finding from the bespoke phase that community-produced media is doing different cultural work than mainstream aggregators. A recipe on The Woks of Life or Chicano Eats frames a dish as an expression of a living tradition. A recipe on AllRecipes presents it as a set of instructions with no author and no history.

### Finding 3: The Fortune Cookie is the most annotated dish at scale - and the most contested

Fortune Cookie generated 37 fully annotated entries, the most of any dish, with the widest distribution across `cultural_ownership_framing` values. This is likely because the Fortune Cookie's origin story - its misattribution to Chinese culture despite Japanese-American origins, and the role of WWII Japanese internment in cementing that misattribution - is itself so well-documented that even sources that engage superficially with the dish's history tend to produce enough text to annotate. The misattribution is its own attractor for media attention.

What is striking is that even among the 37 annotated Fortune Cookie entries, 24 (65%) have `cultural_ownership_framing: not_mentioned` or `claimed` - meaning they either ignore the question entirely or implicitly reinforce the Chinese attribution. Only 5 entries are coded `corrective` or `contested`. To my understanding, the web is saturated with Fortune Cookie content that does not acknowledge the Japanese-American origin. At scale, the misattribution is being reproduced far more than it is being corrected.

### Finding 4: Community credit is withheld even when origin is mentioned

Of the 135 annotated entries, 37 (27%) have `community_credit_given: No`. Crucially, this is not the same population as the entries that don't mention origin at all. Several entries mention that a dish has cultural origins without actually crediting the community: they note that Orange Chicken is "Chinese-American" without naming immigrants, acknowledging labor, or connecting the dish to the specific communities that developed it. This is what `Partial` (16 entries) captures. Naming a community and crediting a community are different acts, and the dataset is designed to distinguish them.

### Finding 5: Scale exposed web topology as a variable

The most unexpected finding from my scaling phase was that the distribution of entries across dishes and communities is not a reflection of my research design - it is a reflection of the web itself. I had intended to collect roughly proportional coverage across all six dishes. Instead, Orange Chicken and Fortune Cookie together account for 291 of 500 entries (58%), simply because DuckDuckGo returns dramatically more results for these dishes than for Mission Burrito or Nachos. The web has produced far more food media content about Chinese-American dishes at fast food chains than about Mexican-American regional cuisine.

This finding has methodological implications for any researcher using automated web collection to study food culture: the corpus you retrieve is not a neutral sample of "food media." It is very likely to be shaped by SEO (Search Engine Optimization), by corporate marketing budgets, or by which communities have had access to publishing platforms, and by which dishes have been made legible to mainstream audiences. The dataset's imbalance (besides could be due to my flaw in collection strategy) can be treated as data about the food media ecosystem.

---

## V. What the Data Conceals

### The annotation gap also shows a structural limitation

The most significant limitation is that only 135 of 500 entries are fully annotated. The 365 metadata-only entries cannot contribute to qualitative analysis of framing. This gap is a direct consequence of two constraints: the Gemini free tier's daily quota of 20 requests, and the widespread use of `robots.txt` restrictions by major food media sites. I believe that scaling annotation to the full 500 entries would be significantly improved with either a paid API access or a different annotation strategy.

### The `notable_substitutions` field was not carried forward at scale

The bespoke dataset included a `notable_substitutions` column documenting ingredient changes from traditional versions - one of the most concrete data points in the initial design. This field was not annotatable by Gemini from scraped text alone (it requires recipe-specific ingredient analysis) and was therefore left blank in all scaled entries. The qualitative richness of tracking, say, how the ratio of cheese to eggplant changes across Chicken Parmesan recipes is present in the bespoke phase but absent at scale. This is an honest loss.

### Source type skew in the scaled data

The scaled dataset is dominated by `Food Media` (437 of 500 entries), because DuckDuckGo's results for food-related queries overwhelmingly return article and blog URLs rather than recipe card pages or corporate sites. The controlled source type diversity of the bespoke phase (deliberately including aggregators, corporate sources, encyclopedias, and community blogs) was not preserved in the automated scaling. The scaled dataset is better understood as a corpus of food media writing about these dishes than as a representative sample of all source types.

### Year of publication is missing for most scaled entries

The `year_published` field is populated for all 50 bespoke entries (range: 2010–2025) but blank for almost all 450 scaled entries, because extracting publication dates reliably from scraped HTML is technically complex and was deprioritized. Temporal analysis - whether framing of immigrant-origin dishes has changed over time, for example - is therefore not possible with the current dataset.

### What is absent entirely

The dataset does not include community discussions (Reddit, YouTube comments), non-English sources, or paywalled content from outlets like The New Yorker or some Bon Appétit long-form pieces. These are meaningful exclusions: community discussions are where authenticity debates are most active and contested, and non-English sources would reveal how the same dishes are framed by the communities that created them rather than by American food media about them. The dataset captures American English-language food media narration, which is one important slice of a much larger cultural conversation.

---

## VI. Computation, Scale, and What Changed Between Them

The shift from 50 to 500 entries changed the dataset in ways that go beyond simple volume. In the bespoke phase, every coding decision was mine: I read each source, applied my understanding of the coding scheme, and wrote annotation notes that reflect my interpretive judgment. At scale, the majority of annotations were produced by Gemini from scraped text excerpts of variable quality, reviewed by me only in batch rather than entry-by-entry. The interpretive labor was distributed - partially to the model, partially to the scraper that determined what text the model received, and partially to the search queries that determined which URLs were even considered.

This distribution of labor is not neutral for me. The model applies the coding scheme consistently in narrow cases (a source that never mentions cultural origin gets `No` reliably) but inconsistently in ambiguous ones (the distinction between `distanced` and `not_mentioned` for a corporate source requires contextual judgment the model does not reliably have). The scraper extracts headnotes and article introductions, which are the most likely places for cultural framing to appear - but some sources put their most interesting framing in the body of an article that the scraper never reached. **The search queries were written by me** to find culturally engaged sources, which means they may have overrepresented sources that discuss origin and underrepresented purely recipe-focused ones.

The lesson for me is that computational scaling is not inherently bad. It is that scaling changes what you are measuring. The bespoke dataset measured how carefully chosen sources across deliberately varied types frame immigrant-origin dishes. The scaled dataset measures how the food media web - as retrieved by DuckDuckGo and scraped by BeautifulSoup - distributes framing practices across a larger and less controlled corpus. Both are valid research objects. They are not the same research object.

---

## VII. Ethics and Privacy

All sources in this dataset are publicly available on the web. No private communications, password-protected content, or anonymized personal data were collected. The dataset does not include named individuals other than public figures (chefs, food writers, corporate figures) already named in public sources.

The `robots.txt` file for each scraped domain was checked before scraping, and sites that disallow automated access were not scraped - they appear in the dataset with `scrape_status: robots_blocked` and no scraped content. This choice imposed a significant analytical cost (188 blocked entries, including Wikipedia and Reddit) but reflects a principled commitment to respecting the access policies that sites have published.

One ethical consideration worth naming explicitly: this dataset is about immigrant communities and their cultural labor, but the dataset itself was built without input from those communities. The coding categories - what counts as "community credit," what counts as "reclaimed" - were defined by me, a college-level newbie researcher who is not a member of the Chinese-American, Italian-American, or Mexican-American communities whose food histories are being tracked. The interpretive categories necessarily reflect my own positionality. A more robust version of this project would involve community members in the design of the coding scheme and the validation of the annotations.

---

## VIII. Situating the Work in Scholarship

This project sits at the intersection of two scholarly conversations: the emerging field of food studies as cultural analysis, and the methodological literature on computational approaches to cultural data.

Within food studies, the foundational question of how immigrant food gets narrated - and by whom - has been explored by Jennifer 8. Lee in *The Fortune Cookie Chronicles* (2008), which provided the historical grounding for this dataset's Fortune Cookie entries, and by Gustavo Arellano in *Taco USA* (2012), which traced the transformation of Mexican food in America with particular attention to the political economy of culinary authenticity. Both scholars use qualitative, narrative methods; this dataset attempts to operationalize some of their central insights into structured, scalable data.

The direct methodological touchstone is Wróblewska et al.'s TASTEset (2022), a Named Entity Recognition benchmark dataset built from 700 annotated recipes. TASTEset demonstrates that computational tools can extract structured information from recipe text at scale - food products, quantities, cooking processes - but treats recipes as purely technical documents, stripping away every dimension of cultural context. This dataset is in some ways a complement to TASTEset: where TASTEset asks *what is in* a recipe, this dataset asks *what story surrounds* it. The two projects together illustrate a distinction that recurs throughout food computing research: the difference between food as ingredient data and food as cultural artifact.

The methodological choices in this project - using LLM-assisted annotation with mandatory human review, preserving the bespoke manual dataset alongside the computational scaling, documenting annotation failures honestly - reflect principles from the "responsible datasets" literature in the digital humanities. As Gebru et al. argue in the "Datasheets for Datasets" framework (2021), datasets should document their composition, collection process, intended uses, and limitations with the same care given to the data itself. This essay is an attempt to honor that commitment and respecting the coursework's requirements for an "ethical dataset" that we learned throughout the semester.

---

## IX. Lessons Learned

The main takeaway for me is: **manual data creation is irreplaceable at the beginning.** The 50-entry bespoke phase was where the research question became real. It is where I discovered that `community_credit_given` was the hardest field to code consistently, that recipe aggregators and food media articles are structurally different research objects even when they cover the same dish, and that the Fortune Cookie is a special case because its misattribution is itself the cultural story. None of these insights would have been available if I had started with automated collection.

In addition, **computational scaling reveals things you cannot see at small scale.** The web topology finding - that Chinese-American dishes are massively overrepresented in food media relative to Mexican-American ones - was not visible in 50 carefully selected entries. It only emerged when I let the algorithm retrieve whatever the web actually produced. That finding is analytically interesting and would have been invisible without scaling.

I also think it's worth mentioning that **the free-tier rate limit is a real research and technical constraint.** Twenty Gemini requests per day, spread across seven days of interrupted sessions on my local laptop, meant that the scaling phase took longer and produced more annotation gaps than planned. This constraint shaped the dataset in ways that are documented but not fully remediable: the annotation gap between bespoke and scaled entries is permanent given the resources available. Future work would require either paid API access or a different annotation strategy (open-source models via Ollama, for example, have no daily cap and run locally).

Lastly, **the column rename mattered.** Changing `authenticity_framing` to `cultural_ownership_framing` - prompted by instructor feedback that the model might be interpreting "authenticity" in terms of copyright or culinary accuracy rather than cultural belonging - produced measurably different annotations. The revised prompt, which asked how a source positions the dish *relative to the immigrant community that created it*, was more precisely aligned with the research question. Prompt language is data design.

---

## X. Conclusion

After five hundred entries, six dishes, three communities, and one semester learning and coding, the central finding of this dataset I believe is relatively straightforward. It is that the vast majority of English-language American food media about immigrant-origin dishes does not engage with their cultural histories. Sixty percent of annotated sources mention no origin story. Fifty-nine percent never raise the question of cultural ownership. The highest-traffic platforms - AllRecipes, Food Network, corporate brand pages - are almost universally silent on these dimensions. The sources that do engage - community food blogs, regional journalism, some food media longform - are a small fraction of what the web produces and a small fraction of what people read.

This is not a scandal. It is a structural thing. Recipe aggregators are not in the business of cultural history; they are in the business of traffic. Corporate sites are in the business of brand identity. The silence about immigrant labor and community credit is not malicious - it is the default outcome of a media ecosystem optimized for engagement rather than attribution. What this dataset makes visible is that default: the way that even celebratory food media can erase the communities that made the food, simply by presenting recipes as if they appeared out of nowhere.

The dataset is incomplete, imbalanced, and in some places poorly annotated. It is also, I think, a genuine contribution to understanding how the stories of immigrant food get told and untold in contemporary American media. If given time and effort, the next phase of this work would go deeper on each dish - more sources, more annotation, community voices included - rather than broader. The questions this dataset opens are more interesting than the ones it closes and I'm satisfied the semester project ended this way.

---

## References

Arellano, Gustavo. *Taco USA: How Mexican Food Conquered America*. Scribner, 2012.

Gebru, Timnit, et al. "Datasheets for Datasets." *Communications of the ACM* 64, no. 12 (2021): 86–92.

Lee, Jennifer 8. *The Fortune Cookie Chronicles: Adventures in the World of Chinese Food*. Twelve, 2008.

Wróblewska, Ania, et al. "TASTEset - Recipe Dataset and Food Entities Recognition Benchmark." arXiv preprint arXiv:2204.07775 (2022). https://arxiv.org/abs/2204.07775