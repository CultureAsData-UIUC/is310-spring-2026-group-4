# Extreme Eating as Digital Performance: A Data Essay

IS 310\
Michelle Yi\
14 May 2026

## 1. Introduction: Why Extreme Eating?

Over the past decade, extreme eating content has become one of the internet’s most recognizable forms of online spectacle. Videos focused on eating massive amounts of food, completing calorie challenges, or consuming absurd meals regularly receive millions of views. Creators like ErikTheElectric, Matt Stonie, and Nikocado Avocado have turned eating into entertainment centered around excess.

This project began with a simple observation: extreme eating videos seemed to become more dramatic over time. Earlier videos often focused on straightforward food challenges like eating large quantities of food as quickly as possible. More recent videos rely more heavily on spectacle and exaggerated narratives, with titles such as “I Let AI Control Every Meal for Two Weeks” or “I Ate the Biggest Foods on the Internet for 10 Days.”

The goal of this dataset was not simply to measure how much food creators consume. Instead, the project explores how excess is performed online and how platforms reward spectacle and attention. I was especially interested in how different creators perform excess differently and how those performances changed over time.

The project asks several questions:

* How has extreme eating content changed over time?
* What forms of excess appear most frequently?
* How do creators differently perform spectacle?
* How do platform incentives encourage escalation?
* What changes when this content is turned into data?

Ultimately, this project treats extreme eating as a form of digital performance shaped by algorithms, virality, and audience attention.

---

## 2. How the Data Was Made

### Phase One: Bespoke Manual Dataset

The first phase of the project involved creating a manually annotated dataset of 75 videos collected from three major YouTube creators:

* ErikTheElectric
* Matt Stonie
* Nikocado Avocado

I selected these creators because they represent some of the largest creators in the extreme eating content space, while representing different styles within the genre of content.

Videos were sampled across three rough periods:

* Early – including the first 8 videos on their channel
* Mid – 9 of the videos posted in between early and recent
* Recent – 8 of their latest videos

Each video was manually coded with fields including:

* creator
* video title
* upload date
* period
* food type
* portion size
* views
* likes
* comments
* food quantity
* estimated calories

The manual process involved many interpretive choices. I attempted to estimate calories using video descriptions, nutrition information, and AI tools like ChatGPT when enough information was available. However, many videos did not provide exact quantities, and some foods were too ambiguous to estimate confidently. As a result, the food quantity and calorie fields are incomplete, with some entries intentionally left blank rather than filled with uncertain guesses.

Portion size categories such as “moderate,” “large,” and “extreme” were also interpretive rather than objective. Categorizing the different quantities was the most difficult part, as there is no standardized objective definition of a "large" quantity as compared to an "extreme" one.

### Phase Two: Computational Scaling

After creating the manual dataset, I expanded the project computationally using the YouTube Data API and Python.

I built a script called scale_youtube_dataset.py that automatically collected metadata from videos uploaded by ErikTheElectric, Matt Stonie, and Nikocado Avocado. The script used the Google API Python client library to access channel uploads and retrieve metadata including:

* video titles
* upload dates
* views
* likes
* comments
* descriptions

The script also used keyword-based pattern matching to automate several forms of classification. Food categories were inferred from terms such as “burger,” “pizza,” “ramen,” or “chicken” appearing in video titles. Calorie claims were automatically detected using regular expressions that searched for phrases like “10,000 calories” or “15k calories.” Portion size categories were also estimated automatically based on title keywords and calorie references.

The scaled dataset ultimately expanded to 2,000 total entries.

Unlike the bespoke manual dataset, however, the scaled dataset was intentionally less detailed. Many calorie fields remained blank because reliable estimates could not be generated automatically. Food quantity extraction was also inconsistent because creators use highly variable language in titles and descriptions.

This resulted in many fields having entries like, "mixed/unknown" or being left blank altogether.

---

## 3. What the Data Contains

The final dataset consists of two interconnected datasets:

### Manual Dataset

* 75 manually annotated entries
* Three creators
* Sampling across early, mid, and recent periods
* Detailed calorie estimates and food quantity descriptions

### Scaled Dataset

* 2,000 automatically collected entries
* Metadata collected using the YouTube Data API
* Automated food classification and calorie detection
* Large-scale engagement analysis

---

## 4. What the Data Reveals

### Finding 1: Extreme Eating Content Changed Over Time

One of the clearest patterns in the dataset is that extreme eating content became more narrative-driven over time.

Earlier videos often focused on relatively simple challenge formats:

- “KFC 20 Piece Bucket Eating Challenge”
- “100 Potstickers in 101 Seconds”
- “35 IHOP Pancakes”

More recent videos increasingly rely on spectacle-based narratives:

- “I Let AI Control Every Meal for Two Weeks”
- “I Ate the Biggest Foods on the Internet for 10 Days”
- “I Let Fast Food Companies Control My Diet for a Week”

The spectacle is no longer only the amount of food itself. The challenge premise, storyline, and exaggerated setup become part of the entertainment.

### Finding 2: Different Creators Perform Excess Differently

Although all three creators make extreme eating content, they perform excess in different ways.

Matt Stonie’s videos mainly focus on quantity and speed. Many of his earlier videos involve straightforward competitive eating challenges with simple titles and formats.

Nikocado Avocado’s videos emphasize emotional spectacle, interpersonal drama, and transgressive excess. The food often becomes part of a larger performative narrative.

ErikTheElectric’s videos increasingly frame excess through endurance, discipline, and survival-style challenge formats.

This suggests that “extreme eating” is not one singular genre, but a broader category containing multiple performance styles.

### Finding 3: Engagement Patterns Differ Across Creators

I created graphs using the data, to see how average views changed over time, with each creator. These graphs revealed that view trends differed significantly across the three creators.

ErikTheElectric experienced dramatic growth after 2022, particularly during videos centered around narrative spectacle such as AI-controlled diets, multi-day challenges, and “entire menu” concepts.

Nikocado Avocado also showed major growth over time, although his engagement fluctuated more heavily.

In contrast, Matt Stonie’s average views peaked around 2018–2019 before gradually declining in later years.

These differences suggest that platforms do not reward all forms of excess equally. Earlier competitive eating formats centered primarily on quantity and speed may have become less novel over time, while narrative-driven and emotionally exaggerated formats appear to align more closely with newer platform incentives and audience expectations.

### Finding 4: Platform Spectacle Rewards Quantification

Titles across the dataset increasingly emphasize numbers and exaggeration:

- “10,000 Calories”
- “Entire Menu”
- “World’s Biggest”
- “25 Happy Meals”

Large calorie totals and quantified spectacle function as attention-grabbing devices optimized for visibility on recommendation-based platforms.

---

## 5. What the Data Conceals

Although the dataset captures important patterns, it also conceals many dimensions of extreme eating culture.

### Calorie Estimation Is Interpretive

Many calorie totals in the manual dataset are estimates rather than verified measurements. Some creators exaggerate calorie totals for entertainment purposes, while others omit exact quantities entirely.

This means calorie estimates should not be interpreted as precise nutritional measurements.

### Quantity Does Not Equal Consumption

The dataset cannot fully verify whether all food shown on screen was actually consumed. Videos may involve editing, omitted footage, or partial consumption.

The dataset therefore tracks performed consumption rather than guaranteed consumption.

### Incomplete Fields Reflect Data Limitations

A major limitation of the dataset is that many food quantity and calorie fields remain incomplete. This reflects the difficulty of turning highly edited video performances into measurable numerical data. Some videos clearly advertise calorie totals or exact item counts, while others only visually display food without giving reliable measurements.

Leaving these fields blank was an intentional choice when estimation became too speculative.

### Automated Classification Flattens Nuance

The scaled dataset relies heavily on keyword classification.

For example, a video containing the word “spicy” may be automatically classified as transgressive excess even if the central spectacle is actually quantity or caloric density.

Similarly, “burger” videos can range from relatively small meals to extremely excessive challenge formats.

Automation simplifies these distinctions.

### Audience Interpretation Is Missing

I initially considered coding audience comments as “concerned” versus “encouraging,” but this quickly became difficult and ethically complicated. Tone, irony, sarcasm, and performance are difficult to classify reliably.

As a result, audience interpretation remains only partially visible through engagement metrics rather than detailed qualitative comment analysis.

## 6. Computation, Scale, and What Changed

The manual dataset allowed for more interpretive decisions, but many fields still remained incomplete because creators often did not provide exact calorie totals or food quantities.

The scaled dataset prioritized quantity over detail. Using the YouTube Data API allowed me to collect nearly 2,000 entries quickly, but many classifications became broader and less precise.

This process showed how computational methods shape the kinds of patterns and conclusions that become visible in a dataset.

---

## 7. Ethics and Privacy

All videos included in the dataset were publicly available YouTube uploads created by public-facing content creators.

The dataset does not include:

* private user information
* deleted/private content
* personal audience identifiers
* scraped usernames from comments

One ethical issue that emerged during the project involved the relationship between entertainment and health.

Extreme eating content is connected to topics like body image, dieting, fitness culture, and online performance. Although this project analyzes these videos as a form of digital spectacle, it does not attempt to diagnose creators or make assumptions about their personal health.

Another ethical concern involves platform algorithms. This project raises questions about whether recommendation systems encourage creators to make increasingly extreme content in order to attract more attention and views.

---

## 8. Lessons Learned

The biggest lesson I learned is that creating data changes how you understand a topic.

Before making the dataset, I mostly viewed extreme eating videos as exaggerated entertainment. While collecting and organizing the data, however, I started noticing patterns in how creators perform spectacle differently online.

I also learned that scaling introduces tradeoffs. The scaled dataset made it easier to see larger engagement trends, but automation also made the classifications broader and less accurate.

Finally, this project showed me that datasets are interpretive. The categories I chose affected what became visible in the data, meaning different choices could have led to different conclusions.

---

## 9. Conclusion

Extreme eating content is not just about food. It is also a form of online performance shaped by spectacle, algorithms, virality, and audience attention.

Across nearly 2,000 entries, this project shows how creators increasingly turned eating into exaggerated online entertainment. Earlier videos focused more on quantity, while more recent videos relied more heavily on dramatic narratives and spectacle.

The project also showed that scaling changes interpretation. The manual dataset allowed for more detailed observations, while the scaled dataset made broader engagement trends easier to see but simplified many details.

Overall, this project demonstrated that datasets are not neutral. The way data is collected, categorized, and scaled affects the kinds of patterns and conclusions that become visible.
