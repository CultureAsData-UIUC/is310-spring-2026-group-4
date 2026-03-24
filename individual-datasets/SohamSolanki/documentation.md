# Protein as Cultural Performance: Dataset Documentation
### Soham Solanki (ssolan24)

## Project Overview

This dataset examines how protein consumption is constructed, performed, and circulated on TikTok as a marker of discipline, morality, and self-optimization. By analyzing nearly 50 short-form videos focused on protein-enhanced foods and routines, this project investigates how a single nutrient becomes a symbolic ingredient used to moralize food choices, aestheticize daily routines, and signal participation in contemporary wellness and fitness cultures.

**Research Question:** How does "high protein" content on TikTok frame health not merely as physical well-being, but as a visible marker of discipline, productivity, and moral virtue?

---

## 1. Cultural Materials & Rationale

### What I're Working With

**Primary Materials:** 49 TikTok videos collected between February-March 2026, all explicitly centering protein consumption as part of healthy habits or wellness routines.

**Why TikTok?** TikTok's algorithmic promotion and short-form video format create unique conditions for wellness content:
- Platform aesthetics demand quick, visually engaging content
- Hashtag cultures create discursive communities (#ProteinCoffee, #HighProtein)
- "Realness" must be performed within highly edited constraints
- Commercial and personal content blur together

**Why Protein?** Protein has emerged as the moral nutrient of the 2020s, associated with discipline, optimization, and "clean eating" in ways that transcend its nutritional function. Unlike other macronutrients (carbs, fats), protein carries overwhelmingly positive cultural associations, making it an ideal lens for studying  eating and food as an artifact.

### Approach: From Scratch Collection

I built this dataset **from scratch** rather than auditing an existing dataset for several reasons:

1. **Specificity of Research Questions:** Existing TikTok datasets don't focus on the specific intersection of protein, morality, and wellness culture I'am examining.

2. **Need for Cultural Categorization:** My analysis requires categorizing videos by cultural theme (e.g., "Protein as Fuel" vs. "Guilt-Free Desserts" vs. "Routine Performance"), which can't be extracted from existing metadata alone.

3. **Visual & Tonal Analysis:** Understanding how protein is *performed* (editing styles, aesthetic choices, tonal framing) requires watching each video and making interpretive judgments that automated collection can't capture.

4. **Platform-Specific Discourse:** I needed to capture the vernacular language, visual codes, and performative norms specific to TikTok's protein culture—nuances that emerge only through close engagement with the content.

5. **No real datasets exist for this**: This is a unique project and a project with this level of detail in the data simply does not exist.

---

## 2. Computational Tools & Methods

### Collection Tools

**Phase 1: URL Collection (Manual)**
- Manually browsed TikTok using target hashtags (#ProteinCoffee, #HighProtein, #WhatIEatInADay, #ProteinOats, #FoodIsFuel)
- Used Chrome Tab Groups extension to organize 50 videos by category
- Exported tab data as TXT file for processing

**Phase 2: Metadata Extraction (Semi-Automated)**
- **Apify TikTok Scraper** (free tool)
  - **What it helped with:** Automatically extracted engagement metrics (views, likes, comments, shares), full captions, hashtags, creator usernames, upload dates, music/audio metadata
  - **Time saved:** ~4 hours of manual data entry
  - **Limitations:** 
    - Cannot capture visual aesthetics or tonal qualities
    - Cannot categorize by cultural theme (requires human interpretation)
    - Occasional missing data for videos with privacy settings
    - No access to comment content (only counts)

**Phase 3: Data Processing (Python Scripts)**
- Custom Python script to parse Apify CSV output
- Google Sheets + Gemini to format engagement numbers (924000 → 924K)
- Extracted and cleaned hashtag lists
- Auto-categorized videos by theme based on keywords in captions/hashtags
- Exported to structured CSV format

### What Automation Could Not Do

**Critical Human Labor:**
1. **Cultural Theme Categorization:** Distinguishing between "Protein Dessert (Guilt-Free)" and "Protein-Enhanced Breakfast" requires understanding cultural context, not just keywords.

2. **Tonal Analysis:** Identifying whether a video is "aspirational," "instructional," "satirical," or "relatable" requires watching and interpreting.

3. **Visual Coding:** Noting minimalist aesthetics, gym culture signaling, meal prep containers, editing styles—all require human observation.

4. **Authenticity Assessment:** Judging whether content "feels personal" vs "influencer-like" vs "ad-supported" involves subjective interpretation of performance, the details are not always in the caption.

5. **Pattern Recognition:** Noticing contradictions like "heavily edited but feels very personal" emerges from comparative viewing, not automated analysis.

**Tools Used:**
- Apify TikTok Scraper (metadata extraction)
- Python (csv, json, re libraries for data processing)
- Chrome Tab Groups (organization during collection)
- Google Sheets (manual note-taking and review)
- Claude (for script writing and markdown editing)

---

## 3. Dataset Structure & Decisions

### Data Fields

The final dataset contains **17 fields** per video:

| Field | Type | Source | Purpose |
|-------|------|--------|---------|
| `id` | String | Generated | Unique identifier (tiktok_[video_id]) |
| `submittedVideoUrl` | URL | Manual | Direct link to TikTok video |
| `video_id` | String | Apify | TikTok's internal video ID |
| `creator` | String | Apify | Username (@sofia.bebej, etc.) |
| `caption` | Text | Apify | Full video caption text |
| `hashtags` | String (comma-separated) | Apify | All hashtags used |
| `cultural_theme` | Categorical | Manual | My interpretive categorization |
| `views` | String | Apify | View count (formatted as 924K, 1.2M) |
| `likes` | String | Apify | Like count |
| `comments` | Integer | Apify | Comment count |
| `shares` | Integer | Apify | Share count |
| `upload_date` | Date (YYYY-MM-DD) | Apify | Original posting date |
| `platform` | String | Static | Always "TikTok" |
| `notes` | Text | Manual | Analytical observations |

### Cultural Theme Categories

I developed **9 cultural theme categories** based on how protein functions within the content:

1. **Protein-Enhanced Coffee** (5 videos) - Coffee drinks with added protein powder
2. **Protein-Enhanced Breakfast** (6 videos) - Traditional breakfast foods modified to increase protein
3. **Protein Dessert (Guilt-Free)** (1 video) - Desserts framed as virtuous through protein addition
4. **Routine Performance (WIEIAD)** (5 videos) - "What I Eat in a Day" full routine displays
5. **Routine Performance (Meal Prep)** (3 videos) - Batch cooking and organization displays
6. **Food as Fuel/Optimization** (1 video) - Explicit framing of food as performance fuel
7. **Fitness Culture (Pre-Workout)** (5 videos) - Protein tied to gym performance
8. **Fitness Culture (Post-Workout)** (3 videos) - Recovery-focused protein content
9. **High Protein (General)** (20 videos) - Protein-focused but not fitting other categories

**Rationale for Categories:**
- Captures different *functions* protein serves (enhancement, justification, optimization, routine)
- Reflects platform-specific genres (WIEIAD, meal prep, fitness content)
- Distinguishes between protein as *additive* (coffee, desserts) vs. protein as *central* (fitness meals)

## 4. Interpretive Challenges & Decisions

### Challenge 1: Distinguishing "Influencer" from "Personal" Content

**The Problem:** Almost all TikTok wellness content is performative to some degree. How do I categorize what "feels" personal vs commercial?

**My Decision:** I created a spectrum in my notes:
- **"Influencer content"** = polished editing, brand codes/partnerships visible, cookbook/product links
- **"Personal content"** = lower production value, shows imperfections (leftovers, messy kitchens), no obvious monetization
- **"Ad-supported"** = explicit brand mentions, #ad, partnership tags

**Why This Matters:** The commercialization of wellness affects how morality gets constructed, when "good eating" becomes a product to sell.

### Challenge 2: Auto-Categorization Accuracy

**The Problem:** The Python script auto-categorized videos by keyword matching (e.g., "protein coffee" → Protein-Enhanced Coffee), but this missed nuances.

**Example Issue:** A video about "what I eat in a day" that heavily features protein coffee was categorized as WIEIAD, not Protein-Enhanced Coffee.

**My Decision:** I manually reviewed and adjusted ~15% of auto-categories during the note-taking phase.

**Lesson Learned:** Cultural categories require interpretive labor. Keywords provide a starting point, but human judgment is essential.

### Challenge 3: Engagement Metrics as "Success"

**The Problem:** The scraper collected views, likes, comments, shares, but what do these numbers mean culturally?

**My Decision:** I're treating engagement as *one signal* of cultural resonance, not the only measure of importance. A video with lower views but highly contested comment section might be more culturally significant than a viral recipe.

**Future Analysis:** I plan to analyze *types* of engagement (ratio of comments to likes might indicate controversy vs. approval).

### Challenge 4: Temporal Dynamics

**The Problem:** TikTok content is fragile. Videos can be deleted, made private, or go viral post-collection.

**My Decision:** 
- I captured all data at a single point in time (March 2026)
- I noted upload dates to understand when content was created vs. when it circulated
- I saved full captions and URLs for future reference

**Limitation:** I can't track how these videos' engagement changes over time or how they get remixed/dueted/stitched. I also cannot download all of these videos, as storage is limited on my laptop and in the cloud. I also get rate-limited, which further lengthens the process.

---

## 5. Patterns & Emerging Questions

### Pattern 1: Quantification as Virtue

**Observation:** Nearly every video specifies exact protein grams (20g, 30g, 50g, 150g, 208g, 250g).

**Cultural Meaning:** Precision = discipline = moral goodness. Quantification makes virtue *measurable* and *achievable*.

**Quote from Notes:** 
> "Shows proportions for each... easy-to-follow recipe"
> "Macros during a busy workday"

**Question for Analysis:** Does higher protein specificity correlate with higher engagement?

### Pattern 2: Speed as Moral Efficiency

**Observation:** Frequent use of "5-minute," "easiest," "quick and easy," "under 5 minutes"

**Cultural Meaning:** Efficiency signals discipline. Achieving protein goals quickly = self-optimization.

**Quote from Notes:**
> "Advertises as 5-minute prep time"
> "easiest high protein iced coffee in under 5 minutes"

**Question for Analysis:** How does time-saving rhetoric intersect with the labor of meal prep?

### Pattern 3: The "Realistic" Performance

**Observation:** Videos claim to be "realistic" while being heavily edited.

**Cultural Meaning:** Authenticity itself becomes a performance. "Realness" is signaled through specific cues (leftovers, busy schedules) even in polished content.

**Quote from Notes:**
> "More realistic because she shows leftovers and more mention of drinks"
> "Heavily edited but feels very personal"

**Tension:** Can wellness content ever escape performance? Is there "authentic" protein consumption on TikTok?

### Pattern 4: Protein Makes Desserts Moral

**Observation:** Desserts/sweets require protein to be "guilt-free"

**Cultural Meaning:** Pleasure must be *ustified through nutrition. Protein serves as moral absolution.

**Quote from Notes:**
> "Advertises as... low calorie, and 4g of protein per protein bite"

> "Next time you're craving something sweet during a cut... high protein dessert"

**Question:** What does this reveal about contemporary anxieties around pleasure and discipline?

### Pattern 5: Commercial Framing as "Choice"

**Observation:** Ad-supported content (Javvy Coffee, PBfit, Prozis) frames products as personal preference.

**Cultural Meaning:** Consumption becomes identity. Brand partnerships are naturalized as lifestyle choices.

**Quote from Notes:**
> "Influencer content, likely ad-supported"

> "Code FITFOODIEJULES will give you the biggest discount"

**Tension:** Where does personal wellness end and commercial wellness begin?

---

## 6. What This Dataset Captures (& What It Doesn't)

### What I Have

- ✅ **Protein as Moral Good:** Evidence of how protein functions as virtue signal
- ✅ **Platform Aesthetics:** Documentation of TikTok-specific visual/editing norms
- ✅ **Optimization Rhetoric:** Language of efficiency, fuel, performance
- ✅ **Commercial Wellness:** Tracking of ad-supported vs. organic content
- ✅ **Performance of Authenticity:** Notes on "realistic" vs. "influencer" framing
- ✅ **Genre Diversity:** Coffee enhancements, meal prep, WIEIAD, fitness content
- ✅ **Engagement Patterns:** Quantitative data on views, likes, comments, shares

### What I're Missing

- ❌ **Comment Section Discourse:** I have comment *counts* but not comment *content* (where pushback/debate happens)
- ❌ **Duet/Stitch Chains:** I don't track how videos respond to each other
- ❌ **Creator Demographics:** No systematic data on creator age, race, gender, class (though some observable)
- ❌ **Temporal Dynamics:** Snapshot in time, can't track viral spread or engagement changes
- ❌ **Non-English Content:** Language limitation excludes global protein discourse
- ❌ **Deleted/Private Content:** Only captures publicly available videos at collection time

### Why These Limitations Matter

The comment section is where contestation happens—where people debate authenticity, question necessity, push back on wellness culture. Future work should incorporate this.

Duet/stitch culture is how TikTok creates dialogue.  My dataset captures individual videos but misses the conversational network.

---

## 7. Methodological Reflections

### What Worked Well

1. **Hybrid Approach:** Combining automated metadata extraction (Apify) with manual interpretive work gave me both scale and depth.

2. **Iterative Categorization:** Starting with keyword-based auto-categories then manually adjusting allowed me to refine the analytical framework while collecting.

3. **Rich Note-Taking:** Writing analytical observations during collection (not after) helped me notice patterns and contradictions in real-time.

4. **Structured Flexibility:** Having pre-defined fields (caption, hashtags, engagement) while leaving "notes" open-ended balanced consistency with interpretive richness.

### What I'd Do Differently

1. **Pilot Categories First:** I developed the 9 cultural themes somewhat organically. A more systematic pilot (watching 10 videos, developing codes, then collecting) would have been cleaner.

2. **Capture Comment Samples:** Even grabbing top 5-10 comments per video would give more qualitative pushback data.

3. **Track Creator Follower Counts:** This would help distinguish "influencer" vs "regular person" more objectively.

4. **Note Video Length:** Duration might correlate with content type (quick recipes vs. full WIEIAD).

---

## 8. Data Quality & Reliability

### Strengths

- **Complete Metadata:** All 49 videos have full caption, hashtag, and engagement data
- **Consistent Categorization:** Single researcher coded all videos (no inter-rater reliability issues)
- **Transparent Decisions:** Notes field documents interpretive choices in real-time
- **Verifiable:** All URLs link to original content (though content may change/delete over time)

### Limitations

- **Sample Bias:** I collected from specific hashtags (#ProteinCoffee, #HighProtein), which may favor certain content types over others
- **Temporal Snapshot:** March 2026 collection captures only current trends, not historical evolution
- **Engagement Volatility:** View/like counts can change after collection
- **Subjective Coding:** "Influencer" vs "personal" judgments reflect researcher interpretation

### Validity Considerations

**Internal Validity:** My cultural themes are internally consistent, each category captures a distinct function of protein in content.

**External Validity:** My sample may not represent all TikTok protein content, but it does capture dominant genres and tropes within the #HighProtein hashtag ecosystem.


## Next Steps: Scaling & Expansion Plan

### Current State: 49 Carefully Curated Videos
- Rich analytical notes
- Cultural theme categorization
- Visual/tonal assessment
- Commercial awareness

### Goal: Scale to 500-1,000+ Videos

**Primary Approach: Option 1 - Automated Scaling**

I will scale My dataset computationally while attempting to preserve the interpretive depth of My initial collection.


## Scaling Strategy

### Phase 1: Automated Collection (Target: 500 videos)

**Method: TikTok Research API**
- Apply for academic research API access (requires IRB approval)
- Query by hashtags: #HighProtein, #ProteinRecipes, #WhatIEatInADay, #ProteinCoffee, #MealPrep, #ProteinOats, #FoodIsFuel, #GymFood
- Collect all videos from past 6 months (Sept 2025 - March 2026)
- Extract: video_id, creator, caption, hashtags, views, likes, comments, shares, upload_date

**Fallback Method: Apify at Scale**
- If Research API unavailable, use Apify with batch URL collection
- Requires manual URL gathering via TikTok search + automated scraping

**Timeline:** 2 weeks for collection + processing

### Phase 2: Automated Categorization

**Challenge:** The 9 cultural themes require interpretive judgment. How do I automate this?

**Method 1: Keyword-Based Classification (Baseline)**

Create decision tree based on caption/hashtag keywords:

```python
def categorize_video(caption, hashtags):
    text = (caption + " " + hashtags).lower()
    
    if "protein coffee" in text or "proffee" in text:
        return "Protein-Enhanced Coffee"
    elif "protein oats" in text or "baked oats" in text:
        return "Protein-Enhanced Breakfast"
    elif "what i eat in a day" in text or "wieiad" in text:
        return "Routine Performance (WIEIAD)"
    elif "meal prep" in text:
        return "Routine Performance (Meal Prep)"
    # ... etc
    else:
        return "High Protein (General)"
```

- **Expected Accuracy:** ~70% based on My pilot data
- **Limitation:** Misses nuance (e.g., a WIEIAD video featuring protein coffee gets mis-categorized)

**Method 2: LLM-Based Classification (Advanced)**

Use Claude API to classify based on caption:

```python
prompt = f"""
Categorize this TikTok video caption into ONE of these themes:
1. Protein-Enhanced Coffee
2. Protein-Enhanced Breakfast  
3. Protein Dessert (Guilt-Free)
4. Routine Performance (WIEIAD)
5. Routine Performance (Meal Prep)
6. Food as Fuel/Optimization
7. Fitness Culture (Pre-Workout)
8. Fitness Culture (Post-Workout)
9. High Protein (General)

Caption: {caption}
Hashtags: {hashtags}

Return only the category name.
"""
```

**Expected Accuracy:** ~85-90% (based on LLM performance on similar tasks)
**Limitation:** Expensive at scale ($0.01-0.02 per classification × 500 videos = $5-10)
**Advantage:** Can handle nuance better than keyword matching

**My Decision:** Use Method 1 (keywords) for first pass, then manually review a random 10% sample to assess accuracy. If accuracy < 75%, switch to Method 2 (LLM).

### Phase 3: Automated Sentiment/Tone Analysis

**Challenge:** The notes capture tone ("aspirational," "instructional," "satirical"). Can I automate this?

**Method: Sentiment Analysis on Captions**

Use existing sentiment analysis tools (VADER, TextBlob) to score:
- **Positivity:** How upbeat is the language?
- **Instructional markers:** Presence of imperative verbs, step-by-step language
- **Aspiration markers:** Future tense, transformation language ("will," "can," "achieve")

**Example Implementation:**
```python
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_tone(caption):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(caption)
    
    # Check for instructional language
    instructional_words = ['try', 'make', 'add', 'mix', 'combine', 'follow']
    is_instructional = any(word in caption.lower() for word in instructional_words)
    
    # Check for aspiration language
    aspiration_words = ['will', 'can', 'achieve', 'goal', 'journey', 'transform']
    is_aspirational = any(word in caption.lower() for word in aspiration_words)
    
    return {
        'sentiment_score': sentiment['compound'],
        'is_instructional': is_instructional,
        'is_aspirational': is_aspirational
    }
```

**Limitation:** This captures surface-level tone, not the performative contradiction I noted (e.g., "heavily edited but feels personal"). That requires visual analysis, which is beyond current scope.

### Phase 4: Pattern Matching for Moral Language

**Goal:** Automatically detect the moral language patterns I identified:
- Quantification ("30g protein")
- Speed/efficiency ("5 minutes," "easy," "quick")
- Guilt-free framing
- Fuel/optimization language

**Method: Regular Expressions + Keyword Counting**

```python
import re

def extract_moral_language(caption):
    # Quantification pattern
    protein_amounts = re.findall(r'(\d+)\s*g\s*protein', caption.lower())
    
    # Speed markers
    speed_words = ['minute', 'quick', 'easy', 'fast', 'simple']
    speed_count = sum(1 for word in speed_words if word in caption.lower())
    
    # Moral markers
    guilt_free = 'guilt free' in caption.lower() or 'guilt-free' in caption.lower()
    fuel_language = 'fuel' in caption.lower() or 'optimize' in caption.lower()
    
    return {
        'protein_grams_mentioned': protein_amounts,
        'speed_markers': speed_count,
        'guilt_free_framing': guilt_free,
        'fuel_optimization': fuel_language
    }
```

**Expected Output:** New columns in dataset:
- `protein_amount_g` (integer or list)
- `speed_marker_count` (integer)
- `guilt_free` (boolean)
- `fuel_language` (boolean)

**Advantage:** Fully automatable, objective
**Limitation:** Misses context (e.g., "not guilt-free" would be flagged as guilt-free)

---

## What Changes at Scale?

### 1. Loss of Visual/Aesthetic Analysis

**What I Lose:**
- "Heavily edited and influencer-like"
- "Minimalist white kitchen"
- "Shows meal prep containers"
- "Before/after transformation"

**Why It Matters:** Visual aesthetics are *how* morality gets performed on TikTok. Losing this means I can't analyze the **performance** of protein culture, only the **discourse**.

**Potential Solution (Future Work):** 
- Computer vision to detect objects (meal prep containers, protein powder tubs)
- Scene classification (kitchen vs. gym setting)
- Editing tempo analysis (cuts per second)
- **But this requires video downloads + significant computational resources**

### 2. Loss of Contradictions & Nuance

**What I Lose:**
- "Heavily edited but feels very personal"
- "Seems more aesthetic than realistic"
- Recognition of performative authenticity

**Why It Matters:** The interesting analytical work is often in the tensions and *contradictions*, which automated analysis smooths over.

**Trade-off:** I would gain volume (500 videos) but lose depth (rich interpretation). This is the main challenge of scaling qualitative research.

### 3. Gain: Pattern Confirmation

**What I Gain:**
- Statistical validation of patterns observed in n=49
- Ability to test hypotheses (Does speed language correlate with engagement?)
- Identification of dominant vs. marginal trends
- Temporal analysis (Are protein coffee videos increasing over time?)

**Example Research Questions I Can Answer at Scale:**
- What % of high-protein content is ad-supported?
- Does quantification (mentioning specific protein grams) predict higher engagement?
- Are WIEIAD videos more likely to use aspiration language than recipe videos?
- How has protein discourse shifted from Sept 2025 to March 2026?

### 4. Sampling Strategy Shift

**Current Approach (n=49):** Purposive sampling - I selected diverse examples across categories

**Scaled Approach (n=500):** Systematic sampling - I collect all videos matching hashtag criteria within timeframe

**Implication:** I move from "representative diversity" to "population capture" (within hashtag ecosystems). Different research questions become answerable.

---

## Technical Challenges Anticipated

### Challenge 1: API Rate Limits

**Problem:** TikTok Research API limits requests to ~1000/day. Collecting 500 videos with full metadata might require multiple days.

**Solution:** 
- Batch requests efficiently
- Cache results to avoid re-querying
- Implement exponential backoff for rate limit errors

### Challenge 2: Data Storage & Processing

**Problem:** 500 videos × 17 fields × rich text captions = large dataset (~5-10 MB CSV)

**Solution:**
- Use the ``pandas`` library and Python for efficient data manipulation
- Store in SQLite database if CSV becomes too large and out of control

### Challenge 3: Categorization Errors

**Problem:** Keyword-based categorization will inevitably have errors. How do I measure accuracy?

**Solution:**
- Manually code a random 10% sample (50 videos)
- Calculate inter-rater reliability between human coding and automated coding
- If accuracy < 75%, revise keyword rules or switch to LLM classification
- Document misclassification patterns for later discussion

### Challenge 4: Missing Data

**Problem:** Not all videos have complete metadata (deleted videos, private accounts, geo-restricted content)

**Solution:**
- Track missing data rates by field
- Decide on threshold (e.g., exclude videos missing >3 core fields)
- Document exclusion criteria transparently

### Challenge 5: Ethical Considerations at Scale

**Problem:** Collecting 500 videos means analyzing content from hundreds of creators who didn't consent to research.

**Solution:**
- Only collect public content (no private accounts)
- Anonymize creators in publications (use generic IDs, not usernames)
- Focus on discourse patterns, not individual creators
- Store data securely (not in public GitHub repo)
- Consider reaching out to creators with large followings if directly quoting

---

## Interpretive Decisions That Could be Automated

### What I Think I Can Automate (with acceptable accuracy):

1. ✅ **Cultural Theme Categorization** - LLM-based classification should achieve ~85% accuracy
2. ✅ **Moral Language Detection** - Regex patterns for quantification, speed, guilt-free framing
3. ✅ **Ad-Supported Content** - Keyword and hashtag detection for brand names, codes, partnerships
4. ✅ **Hashtag Analysis** - Automated extraction and frequency counting
5. ✅ **Engagement Trends** - Statistical analysis of views/likes/comments patterns

### What I Know I Can't Automate (without significant loss):

1. ❌ **Visual Aesthetics** - "Minimalist kitchen," "heavily edited," "meal prep containers"
2. ❌ **Performative Contradictions** - "Edited but feels personal," "aesthetic yet realistic"
3. ❌ **Tonal Subtlety** - Distinguishing aspirational from instructional from relatable
4. ❌ **Cultural Context** - Understanding why certain framings resonate
5. ❌ **Critical Interpretation** - Recognizing what's culturally significant vs. statistically common

### My Strategy: Mixed Methods at Scale

**Computational Analysis (n=500):**
- Categorical distributions
- Engagement patterns
- etc.

**Close Reading (n=49):**
- Visual/aesthetic analysis
- Performative contradictions
- Cultural significance
- Interpretive depth

**Integration:**
Use computational findings to identify patterns, then return to close reading of exemplary cases to interpret those patterns.

---

## Timeline & Milestones

### Week 1-2 (Post-Spring Break): Data Collection
- Apply for TikTok Research API access (or set up Apify batch processing)
- Collect 500 videos matching hashtag criteria
- Extract metadata and store in structured format

### Week 3: Automated Analysis Pipeline
- Implement keyword-based categorization
- Test accuracy on pilot sample (My existing 49 videos)
- Revise classification rules or switch to LLM if needed
- Run moral language pattern matching

### Week 4: Validation & Quality Check
- Manually code 10% random sample (50 videos)
- Calculate accuracy metrics
- Identify systematic misclassifications
- Document limitations

### Week 5: Statistical Analysis
- Engagement pattern analysis
- Temporal trends
- Correlation tests (quantification × engagement, speed language × shares, etc.)
- Category comparisons

### Week 6: Integration & Interpretation
- Synthesize computational findings with close reading insights
- Identify unique cases for deep analysis
- Write up findings


## Expected Outcomes

### Quantitative Findings I Expect

1. **Confirmation of Quantification Pattern:** I predict >60% of videos will mention specific protein amounts
2. **Speed Language Ubiquity:** I predict >40% will use efficiency/speed framing
3. **Ad-Supported Content:** I predict 20-30% will have brand partnerships/codes
4. **Engagement Hierarchy:** I hypothesize WIEIAD content gets more comments (contestation) than recipe content

### Qualitative Insights I Hope to Gain

1. **Temporal Evolution:** Has protein discourse shifted over 6 months? New sub-genres emerging?
2. **Outliers:** What does *low-engagement* high-protein content look like? What failed to resonate?
3. **Diversity:** Are there marginalized voices/approaches I missed in My initial purposive sample?

### Methodological Lessons

1. **Limits of Automation:** Where does computational analysis break down? What gets lost?
2. **Value of Scale:** What patterns only become visible at n=500 that were invisible at n=49?
3. **Mixed Methods Model:** How can I productively combine close reading + distant reading?