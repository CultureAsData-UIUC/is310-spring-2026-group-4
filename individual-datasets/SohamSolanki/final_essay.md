# Protein as Cultural Performance: How a Nutrient Became a Moral Language on TikTok

**IS 310 - Culture As Data | Spring 2026**  
**Soham Solanki**  
**May 15, 2026**  
**Professor LeBlanc**

---

## Introduction

If you open TikTok and search #protein, the first video you scroll to might show a bowl of overnight oats with "32G PROTEIN" written across it in big white text. The next one is probably a man in his kitchen mixing whey powder into iced coffee while a trending song plays softly in the background. After that, a bodybuilder's full day of eating with the macros listed precisely down to the gram: 1670 calories, 126g carbs, 35g fat, 208g protein. Then, eventually, you'll come across a different kind of video. Maybe someone walking through a grocery store, pointing at protein soda and protein pop tarts, asking "that…that isn't weird?" That last video is doing something interesting. It appears under the same hashtag as the protein oats and the protein coffee, but it's not performing protein consumption, it's critiquing it. And somehow it shows up in the same feed, alongside the videos it's critiquing, often sponsored by the same kinds of brands.

This project asks how that whole ecosystem works. Specifically, my research question is: **how does "high protein" content on TikTok frame health not just as physical well-being, but as a visible marker of discipline, productivity, and moral virtue?** Protein on TikTok functions as a moral language. It's the vocabulary through which discipline, virtue, and self-optimization get performed and, increasingly, sold. But the same hashtag ecosystem also contains a growing critique of itself, which complicates any reading of "wellness culture" as one single "thing".

To look deeper into this, I built a dataset of 48 TikTok videos centered on high-protein content and analyzed them using a three-method approach: my own close reading and manual coding, an LLM-based classifier, and a regex-based pattern matcher. Running three independent methods on the same data let me really look at where the categorizations agree (which validates findings) and where they disagree (which surfaces the more interesting cases). The cultural patterns I find in this essay are anchored both in close readings of specific videos and in the computational analysis that supports them.

---

## Background and Framing

The framework I use to read these videos is based on the idea that wellness platforms blur the line between personal preference and commercial interest in ways that make both harder to critique. Wellness content sells products by attaching them to ideas about discipline, virtue, and self-improvement, and those ideas circulate freely across creators and brands until "what I do" and "what I'm being paid to promote" become almost impossible to separate.

Protein is a useful test case because of how positively it's coded culturally, especially in today's digital age. Unlike carbs or fats, which carry mixed associations, protein in the 2020s reads as overwhelmingly virtuous: muscle, strength, fullness, satiety, fitness, discipline. The FDA is pushing protein in kids' diets now more than ever. That positive coding makes it easy to attach to almost anything — pop tarts, coffee, soda, even pasta sauce — and have the new product inherit the moral weight protein already carries. That becomes its own language: if you can frame any food as "high protein," you can effectively market it without much pushback.

TikTok matters specifically because of how the platform shapes wellness content. Short-form video rewards quick visual hooks. Algorithms bring up what already performs well, creating feedback loops where successful framings get amplified. Hashtag communities form around specific genres (what I eat in a day (WIEIAD), meal prep, protein recipes), creating aimless spaces where certain norms become invisible because everyone is performing them. And importantly, the platform itself is a pre-filter. What I see when I search #protein is already shaped by TikTok's recommendations — a fact that's easy to forget but worth flagging up front. 

*A note on what this means for my analysis: I'm not studying "all" protein content, or even all of it on TikTok. I'm studying what the platform's algorithm decided to surface under specific hashtags in early 2026 to a particular user (me). Other users would see different videos. That's a constraint, but it's also part of the cultural phenomenon: the algorithm is how this circulates in the first place.*

---

## Methodology

### Data Collection

I built this dataset from scratch rather than using an existing one because no existing dataset focuses on the specific intersection of protein, morality, and wellness culture I'm interested in. I manually collected 48 video URLs across February and March 2026 by browsing target hashtags (#ProteinCoffee, #HighProtein, #WhatIEatInADay, #ProteinOats, #FoodIsFuel) and saving videos that appeared to center protein as a moral or aspirational category. I then used the Apify TikTok Scraper to extract metadata — captions, hashtags, view/like/comment/share counts, upload dates — and assigned each video a cultural theme based on my interpretation after watching it. The original dataset includes a free-form "notes" field where I wrote analytical observations during collection. Those notes became a key analytical resource later on.

### Why I Stayed at n = 48

My initial scaling plan targeted 500 videos. I did not scale, and that's a deliberate choice. I intentionally chose depth over volume because quality of analysis can compensate for quantity of data. I decided that spending 15-20 hours scraping more videos would have given me statistical breadth but not interpretive depth. I'd rather have 48 videos I know well than 500 I've barely watched.

### Three-Method Triangulation

After completing the initial dataset, I built three independent classification methods and compared their outputs. Each method approaches the same task, assigning each video to a cultural theme, from a totally different starting point.

**Method 1: Manual coding.** My own cultural theme assignments based on watching each video. This is interpretively rich but slow and not independently verifiable.

**Method 2: LLM-based classification.** Using Claude (Opus 4.7) to read each video's caption and hashtags and assign a category, a tone, and 1-2 sentences explaining the choice. That field turned out to be the single most useful addition because it surfaced differences in the data that I hadn't noticed manually.

**Method 3: Regex and keyword counting.** A rule-based classifier that just matches words and phrases (e.g., if the text contains "protein coffee", label as Protein-Enhanced Coffee). I also used regex to detect "moral language" patterns: protein gram amounts, speed words ("quick," "easy," "5-minute"), guilt-free framing, fuel/optimization language, and ad markers.

I ran all three methods on all 48 videos and computed agreement rates between them. The headline numbers:

| Comparison | Agreement |
|---|---|
| Manual vs. LLM | 41/48 (85.4%) |
| Manual vs. Regex | 41/48 (85.4%) |
| LLM vs. Regex | 41/48 (85.4%) |
| **All three methods agree** | **38/48 (79.2%)** |
| None of them agree | 1/48 (2.1%) |

Three independent methods converge on the same answer for about 79% of the dataset. That's the validation. The remaining 20% is where the more interesting work happens, because that's where the methods are picking up on different things in the same video. I'll be looking at that more in the findings section.

### Restructuring the Category Scheme

Running the LLM classifier surfaced something I hadn't fully seen with my original 9 categories. About 25% of my dataset — 12 videos — aren't actually performing protein consumption. They're satirical videos critiquing the trend, reaction videos to viral recipes, podcast clips on broader nutrition, or educational dietitian content. What I didn't realize was that my original 9 categories had no slot for this kind of "meta" content, so all of it got dumped into the residual "High Protein (General)" category.

Following the feedback I received, I restructured my guidelines into three factors:
- **Function** (what role does protein play?): enhancement, optimization, routine display, moralization, critique, education
- **Genre** (what kind of video is it?): recipe, WIEIAD, meal prep, review/reaction, educational, podcast clip, satire/critique
- **Position** (how does the video relate to protein?): additive (protein added to something else), central (protein-rich food is the meal), or meta (the video is about protein culture rather than consuming it)

I'm keeping both the original 9 categories and the new 3-axis breakdown in my final dataset. The 9-category scheme keeps backward compatibility with my initial submission, while the 3-axis scheme is the primary analytical method I use throughout this essay.

### Trade-offs

One thing I want to address up front: in my initial submission, I described "subjective coding" as a limitation. I don't think that framing was accurate. Interpretive judgment is not a weakness of cultural-data work, it's kind of the whole point. The whole reason I built this dataset rather than auditing an existing one was to make those judgments. What is true is that I'm one student with no second coder, which introduces a consistency challenge. The three-method triangulation is my way of checking my interpretive work against two independent automated baselines.

The other trade-off is that my regex pass turned up a much lower quantification rate than I expected (31% of captions explicitly mention protein gram amounts). The gap is itself a methodological finding: protein gram quantification is mostly visual or spoken in this content, not written. Caption-only analysis undercounts moral language patterns when those patterns are performed visually. I'll look at this in the limitations section.

---

## Findings

### Pattern 1: Quantification as Virtue

Across the dataset, videos that perform protein consumption display protein gram amounts with striking precision. The numbers are oddly specific: 20g, 22g, 32g, 46g, 50g, 208g, 250g, and they appear prominently in on-screen text, captions, or voiceover narration. Precision functions as a kind of moral testimony. It's not enough to say "high protein"; the video has to show *exactly how much*, because precision signals discipline, and discipline signals virtue.

The clearest example in my dataset is a "What I Eat in a Day" video. The video opens with two facts placed side by side: *9% body fat* and *208g protein*. Neither is presented as cause or effect, the connection is implied through proximity. The body is the evidence, and the protein number is the methodology. The video then shows five meals throughout the day, each one a finished plate, with the daily macros precisely listed: 1670 calories, 126g carbs, 35g fat, 208g protein. No shopping, no cooking, no cleanup. The labor of producing this body and these meals is rendered invisible. You see the outcomes and not the work put into it.

What's striking is what the comments do. Users say that the meal plan would be near impossible for someone with a 9-5 or a student schedule. But more importantly, no one in the comments questions the goal. The discipline part of it, that 208g of protein and 9% body fat are worth pursuing, is treated as obviously correct. What gets contested is only how practical this schedule is. This is the wellness culture pattern operating in pure form.

My regex pass picked up 15 of 48 videos as containing protein gram amounts in their captions (31%). The actual number is much higher: many of the strongest examples have the numbers on-screen but not in the caption. This gap between caption-detectable patterns and visually performed ones is itself a finding about how cultural-data analysis breaks down when relying on text alone.

### Pattern 2: Protein as Moral Absolution for Pleasure

A recurring move in the dataset is using protein to morally justify foods that would otherwise read as indulgent. Desserts, pastries, breakfast sweets, and "treats" all require protein to be labeled as virtuous. A good way of putting it is: pleasure must be justified through nutrition, and protein serves as that justification.

The cleanest example is a protein brownie bites recipe video. The on-screen text stacks four claims in rapid succession: "5-minute," "delicious," "low-calorie," "4g protein per ball", collapsing speed, pleasure, restraint, and virtue into one blend. Each phrase stops an objection a user might raise about dessert. It's not slow, not bland, and most importantly, not fattening. The video doesn't argue for the dessert. It stops the case against it.

What's most interesting about this video is the gap between the video itself and its comment section. The video presents the food as virtuously sweetened and macro-friendly, with the advertisement of their cookbook positioning the creator as a trustworthy expert. The comments look at safety concerns: users flag the sugar content and warn that uncooked flour can be harmful. The contestation lives in the comments while the video properly maintains a clean, untroubled relationship to its own moral claims. This pattern,  moral confidence on the surface with debate underneath, shows up across multiple videos in my dataset.

This video is also where my three-method triangulation produced its most interesting disagreement. My manual coding labeled it "High Protein (General)." The LLM labeled it "Protein Dessert (Guilt-Free)." The regex labeled it "Routine Performance (Meal Prep)" because the caption contains "#mealprepideas" along with the dessert framing. All three readings are defensible. The video actually is doing meal-prep work, guilt-free dessert work, and high-protein work simultaneously. The fact that no single method could capture all three is not a failure of the methods, it's a finding about the video. It refuses to classify it in one category because it's doing multiple kinds of cultural work at once.

Notably, when the LLM ran across the full dataset, it identified three videos (including this one) as "Protein Dessert (Guilt-Free)" that I had originally coded as "High Protein (General)." My original count for this category was 1; the LLM-corrected count is closer to 4-5. This pattern is more widespread than my initial coding suggested.

### Pattern 3: Commercial Framing as Personal Choice

The third pattern is the wellness-industrial complex itself: commercial intent disguising itself personal preference. Across the dataset, ad-supported content frames products as natural elements of an aspirational lifestyle rather than as items being sold. The discount code is just there to help; the cookbook plug is just sharing what works; the brand tag is just gratitude.

A representative example is the Prozis baked oats video. The video itself is short and quiet. A warm Olivia Dean song plays in the background while the creator silently scoops a chocolate baked oats dessert from a small bowl. There's no voiceover, no urgency, no obvious sell. The on-screen text just shows the final product with "32g protein" displayed.

The commercial layer is in the caption: *"Code FITFOODIEJULES will give you the biggest discount possible and support my content!"* Three of the seven listed ingredients are marked with asterisks pointing back to Prozis. The discount code is threaded through what is otherwise an intimate, personal-feeling moment. Neither layer would be persuasive on its own. A hard sell would feel like an ad, and a purely intimate video wouldn't move product. Together, now there's a way to bring consumption seamlessly into a person's life. 

### Pattern 4: The Discourse Contains Its Own Critique

The most surprising finding in my dataset is that approximately 25% of videos in the #protein hashtag ecosystem aren't performing protein consumption at all. They're meta-content: satirizing the trend, reacting to viral recipes, critiquing the protein-everywhere phenomenon, or educating about nutrition more broadly. Importantly, this content appears *inside* the same hashtags as the protein-consumption content, not outside it. This contains and circulates its own distaste of the content.

The clearest case is a video by a creator who tags Barebells USA (a protein bar company) while complaining about the protein-everywhere trend. The creator is sitting in his house, pointing at protein soda, protein pop tarts, protein seasoning, protein uncrustables. The caption reads: *"Yes protein is important…. But maybe let's all calm down a bit."*, with a #protein.

The contradiction is the entire reading. A video critiquing protein-everywhere trends is itself sponsored by, or at minimum credits, a brand whose entire product line is protein-everywhere. The "calm down" gesture functions as both satire of the trend and a positioning move: Barebells, unlike these other products, is reasonable. The brand gets to be a part of the crowd critique while remaining a participant in the very trend the video flags as out of hand. This is the wellness-industrial complex's most efficient move: it doesn't need to suppress dissent because dissent is itself monetizable.

A related video explicitly labels the trend as "protein propaganda." The word "propaganda" does so much work. It frames the protein discourse not as a nutritional choice but as an *ideology* — something with a coordinated message, a saturation strategy, and audience. The creator repeats "protein" until it becomes absurd: protein coffee, protein refreshers, protein cookies. The rhetorical move shows how protein has become so saturated nowadays, performing what it critiques. The creator's hesitation, "that…that ain't side eye material?", positions the audience as having always known something was off.

What both videos share is that their comment sections are doing sophisticated cultural work. Viewers in the Barebells video predict that *"fiber will become a trend in 30 years"*, theorizing the wellness-trend cycle in real time, naming protein's saturation as a phase that will pass and be replaced by the next nutrient's moment in the spotlight. The audience is, in a sense, doing more analytical work than the creators. They're naming the structure that the creators are participating in.

The existence of this meta-content cluster is what broke my original 9-category scheme. None of those categories had a slot for "video critiquing the discourse that this video is also embedded within." That's why I added the 3-axis breakdown with position: meta as a dimension, to give this cluster its own name. About 25% of the dataset (12 videos) falls into this meta bucket.

---

## Discussion

Pulling these patterns together, what does the protein discourse on TikTok actually look like as a cultural object? 

It's a moral language. Protein lets creators and brands attach the weight of discipline, virtue, and self-optimization to almost any food. The patterns I documented, talking about quantification as virtue, moral absolution for pleasure, and commercial framing as personal preference, describe the mechanics of that attachment.

The wellness-industrial complex framing helps here. The protein conversation blurs personal preference and commercial interest in ways that make both harder to critique. A creator showing you their "favorite" protein coffee is also selling you a brand. A cookbook plug inside a recipe video is both helpful information and marketing. Where personal choice ends and commercial choice begins is really hard to draw, and that's the whole point.

What complicates the picture is that the discourse has matured enough to name itself. About a quarter of my dataset is meta-content, content like critique, satire, reaction, and education. The "protein propaganda" video calls the trend an ideology. Comments theorize the wellness-trend cycle and predict what nutrient will replace protein in thirty years. But the critique doesn't escape the conversation. It appears under the same hashtags, sometimes sponsored by the same brands. It gets multiplied and now monetized. The wellness-industrial complex doesn't need to suppress its critics because absorbing them is more efficient.

The methodological side of this project produced its own argument. The 79% three-way convergence across my classification methods validates most of my coding. But the 10 videos where the methods disagreed were the same ones that most needed close reading, cases where the content was doing several kinds of cultural work at once. 

And lastly, contestation tends to live in the comments rather than in the videos themselves. The videos perform clean moral surfaces while audiences below contest safety, accessibility, and the trend itself. The cultural work of TikTok happens in the interaction between video and audience, not the video alone. The comment side of that interaction is the most significant thing missing from my overall analysis.

---

## Limitations and Future Directions

**Caption-only analysis undercounts visual patterns.** My regex method picked up explicit protein-gram quantification in 31% of captions. The actual prevalence in the videos is much higher: the numbers are often on-screen text rather than written in captions. Any computational analysis of TikTok content built on text alone will systematically undercount moral language patterns that are performed visually.

**The comment content is missing.** Apify provides comment counts but not the comments themselves. My close readings repeatedly surfaced the comment section as the place where contestation actually happens. Future iterations of this project would benefit from a separate scraping pipeline that captures top comments per video.

**Single-researcher limitation.** I coded all 48 videos myself, which means the interpretive judgments are internally consistent but not externally validated. The three-method triangulation provides a partial check on this, but a multi-coder version of the project would offer different and complementary kinds of validation.

**Algorithmic pre-filtering.** What I collected is what TikTok decided to surface to me when I searched these hashtags. A different user in a different location with a different view history would have seen different videos. The dataset captures a piece of the protein discourse but not "the" protein discourse in any general sense.

**Sample size.** 48 videos is enough for the kind of close-reading work I've done here, but not enough to make strong statistical claims about distributions across the wider ecosystem. The patterns I describe are real in my dataset but the prevalence numbers should be treated as suggestive rather than definitive.

**No video files.** I worked from metadata and captions, which means I can't do any image-level analysis (object detection, scene classification, editing tempo analysis). A future iteration could extract three representative frames per video and run object detection on those static images. This would unlock visual pattern detection without the cost of full video downloads.

Future directions for this work would include: comment content extraction, a fourth classification method (likely a regression or BERT model using the `shorttext` library) for a more complete comparison, a targeted scrape of 50-100 additional videos to balance under-represented categories, and comparing protein discourse across different sub-community hashtags (#ProteinCoffee vs. #WIEIAD vs. #MealPrep) to see whether things shift.

---

## Conclusion

I started this project trying to understand how protein got attached to so many different cultural meanings on TikTok, with things like discipline, virtue, efficiency, self-optimization. What I found is that protein functions as a moral language. It's the vocabulary through which a particular version of wellness culture gets performed. The patterns I documented, like quantification as virtue and commercial framing as personal preference, are the specific techniques through which that language gets deployed across content types.

What I didn't expect was the meta-content. About a quarter of my dataset wasn't performing protein consumption; it was critiquing, satirizing, or theorizing the discourse it appeared within. The critique didn't escape the ecosystem. Rather, it appeared under the same hashtags, sometimes credited to the same brands. The wellness industrial complex absorbed its own disagreements rather than suppressing it. That's an arguably significant finding, maybe the most significant.

Methodologically, this project taught me that cultural categorization resists clean automation, and that the disagreement between methods is where the cultural work shines. The 79% convergence across my three classification methods validates most of my interpretive coding. The 20% where they diverge marks the videos that most rewarded close reading.

What this project contributes is small but specific: a methodologically triangulated cultural-data analysis of how a single nutrient came to do this much moral work in 2026, and a model for how the limits of automation can themselves be turned into findings about the content being analyzed. Protein didn't become a moral language because of any quality of protein. It became a moral language because the cultural infrastructure of wellness: TikTok algorithms, brand partnerships, hashtag communities, the ideology that runs through all of it, needed something to attach to, and protein was available. Next decade, it'll probably be fiber.
