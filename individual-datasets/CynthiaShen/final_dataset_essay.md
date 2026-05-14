# Cooking for One, Watched by Many: A Data Essay on Single-Serving Meal Content on TikTok

**IS310 - Culture As Data | Spring 2026**
**Cynthia Shen**
**Dataset:** `single_serving_tiktok_dataset_v2.json`

---

## I. Introduction: Why Single-Serving?

There is something quietly telling about the phrase "cooking for one." It implies both a practical problem (how do you scale a recipe down?) and a social condition: a person eating alone, managing a household on their own, navigating the ordinary rhythms of solo life. On TikTok, this phrase has become a genre. Search "cooking for one" or "single serving meal" and you will find thousands of videos: creators demonstrating portioned-down pasta dishes, rice bowls adapted for one, desserts baked in a single ramekin. Some frame this as convenience; others frame it as self-care; others simply cook, without commentary, for an audience of strangers.

This dataset was built to examine that genre systematically. Over the course of this semester, I manually collected and annotated 60 TikTok posts featuring single-serving meal content, then computationally augmented those entries with four additional annotation fields. The central questions driving this work are: How do creators frame the act of cooking for one? What cultural patterns emerge in the types of food, the styles of presentation, and the implied audiences for this content? And what does it mean to try to capture those patterns as structured data?

This essay tells the story of how the dataset was made, what it reveals, and, just as importantly, what it conceals.

---

## II. The Platform as Research Site

TikTok is not a neutral container for content. Its design, specifically the "For You Page" (FYP), an algorithmically personalized feed, shapes what content gets made, who sees it, and how creators adapt their style to survive on the platform. As Schellewald (2023) argues in his ethnographic study of young adult TikTok users, the app's affordances configure engagement in ways that are distinct from prior social media platforms: rather than following people you know, users primarily interact with an algorithm that surfaces content based on inferred interests. This content-centric rather than network-centric design means that a creator making single-serving cooking videos is not just addressing their followers; they are producing content that must compete for algorithmic attention against an infinite feed.

This context matters for understanding the dataset. The 60 videos I collected were not discovered through a random sample of TikTok content. They were surfaced through specific search terms ("single serving meal," "cooking for one," "dinner for one," and "easy meal for one") and through TikTok's own recommendation system. The dataset therefore reflects not just what creators make, but what TikTok's algorithm makes visible when a user signals interest in solo cooking content. As I will discuss, the platform's affordances shaped the dataset in ways I could not fully control.

The short-form video format itself also structures what kinds of cooking content can be represented. A video averaging 45 seconds (the median length in this dataset) cannot teach a complex technique or tell a long story. It must compress the cooking process into what is visually legible and emotionally compelling within that window. This compression is itself a cultural artifact: it reflects assumptions about audience attention, about what counts as "easy," and about what a meal worth making in one portion looks like.

---

## III. How the Data Was Made

### Phase 1: Manual Collection

The first phase involved manually collecting and annotating 60 TikTok posts. Each video was found through the search terms listed above and reviewed directly on the platform. For each entry, I recorded ten fields: a unique identifier, the video title and creator handle, a URL, the dish type, a three-level convenience emphasis score (explicit, implicit, or none), the creator's presentation style (face on camera, hands only, voiceover, or text only), the video's length in seconds, the visible like count, and an open notes field.

Several of these fields required interpretive decisions that were not always straightforward. Classifying `convenience_emphasis` as "implicit," where the cooking process appears simplified but convenience is never explicitly stated, required me to read visual cues: the number of ingredients on screen, the pace of cuts, whether the creator's narration emphasized speed. There is no objective threshold for "implicit." That category is a judgment call, made differently by different annotators.

The `dish_type` field presented a different kind of challenge. Because I recorded dish names descriptively as they appeared in each video's title or caption rather than forcing them into a controlled vocabulary, the same category of food ended up with wildly inconsistent labels across entries. Lasagna appears as `Iasagne` in T023 (a phonetic spelling the creator used in their caption) and `Skillet Lasagna` in T033. Sushi is recorded as simply `Sushi` in T019, `sushi` in T053, and `Spicy 'Tuna' Sushi Bake in vegan version` in T034. Mac and cheese appears in three different forms across T003, T004, and T037. At first this felt like a data quality problem. But I came to think it was actually the right call: a creator who titles their video "Tini's viral mac and cheese" is doing something meaningfully different from one who just says "mac and cheese," and collapsing those into a single standardized label would erase information about how creators brand and position their content. The `summarize_dataset.py` script handles this tension by applying broad classification categories only at the summary stage, leaving the raw labels intact in the dataset itself.

The `creator_presentation` field presented a similar challenge. Many videos combine presentation modes: a creator might narrate over footage of their hands cooking, or appear briefly on camera before switching to a hands-only shot. In these cases, I had to determine a dominant mode, which meant making a simplifying decision that flattened genuine complexity in how creators appear in their own content.

Building `cli_data_entry.py`, a command-line data entry tool with structured field validation, helped reduce inconsistencies during data entry. And `summarize_dataset.py`, the analysis script I wrote alongside the dataset, demonstrated that computation can augment even bespoke manual work: the script's parsing functions handled engagement metric formats like "30.8k likes" and duration formats like "1min02s," turning inconsistently formatted raw entries into analyzable numbers.

### Phase 2: Computational Augmentation

After the initial 60-entry dataset was complete, I augmented it with four additional fields using Claude (Anthropic's AI assistant) as an annotation tool. The new fields were `source_search_term` (which of the four original search terms most likely surfaced the video), `lifestyle_context` (the implied life situation of the intended viewer: living alone, student life, meal prep, or general), `health_framing` (whether the video foregrounds health or nutrition goals), and `food_cultural_origin` (a broad classification of the dish's cultural background).

This approach was chosen in response to instructor feedback noting that scaling "is not so much in the number of videos but in the complexity of the annotations." Rather than attempting to automate collection of hundreds of additional videos, a technically difficult task given TikTok's resistance to scraping, I deepened the existing dataset's analytical dimensions.

The process was not automatic. Each annotation was made on the basis of the existing dataset fields (titles, dish descriptions, creator handles) and then reviewed for consistency. In two cases, entries T002 and T049, this review also surfaced data entry errors from Phase 1: field values had been shifted into incorrect columns during manual entry. These were corrected in the v2 dataset.

The use of an AI assistant for annotation raises its own interpretive questions, which I take up in the limitations section below.

---

## IV. What the Data Reveals

### Patterns in Convenience and Presentation

Of the 60 entries, 21 emphasize convenience explicitly, 15 implicitly, and 24 not at all. This distribution suggests that single-serving cooking content is not primarily a convenience genre; a significant portion of creators in this dataset present cooking for one as a full, effortful process, not a shortcut. The "lazy dinner for one" framing (T016) coexists with videos featuring from-scratch pasta (T042) and multi-component meals (T013). Single-serving is a portion size, not a cooking philosophy.

Creator presentation styles are strikingly varied. Among the 60 entries, face-on-camera, hands-only, voiceover, and text-only presentations each appear with roughly comparable frequency. This variety reflects TikTok's affordances for multimodal expression: the platform supports creators who want to narrate their cooking process, creators who prefer to stay off-camera, and creators who dispense with video narration entirely in favor of text overlays on carousel posts. Seventeen of the 60 entries are carousels (image-based posts rather than videos), a format I chose not to exclude because its prevalence is itself a finding about how "cooking content" is defined on the platform.

### Health Framing and Lifestyle Context

The Phase 2 augmentation revealed that health framing is present but not dominant: only 8 of 60 entries foreground health or nutrition goals, with `high_protein` (3 entries), `low_cal` (2 entries), and `balanced` (3 entries). This is notable given that health and fitness content is among TikTok's highest-performing categories. Single-serving cooking content, at least as surfaced by the search terms I used, sits somewhat apart from the high-protein/low-calorie optimization discourse, though that discourse is present in entries like T006 ("56g protein single serve broc cheddar pasta") and T007 ("my single serve, high protein version of the viral dumpling bake").

The `lifestyle_context` field shows that "living alone" is a significant but not dominant framing: 16 of 60 entries explicitly address an audience of solo dwellers, while 37 use a more general framing. This suggests that "cooking for one" on TikTok is not purely a niche genre for people who live alone; it has been adopted as a broader convention for single-portion cooking that appeals across living situations.

### Food Culture and Engagement

Western dishes dominate the dataset (43 of 60 entries), with Asian dishes comprising 9 entries and fusion dishes 8. This distribution likely reflects both the search terms I used (English-language terms that may skew toward Western-coded content) and the broader demographics of the TikTok creators whose content was surfaced. It is not a representative sample of global cooking; it is a snapshot of what English-language single-serving cooking content looks like on TikTok in early 2025.

Engagement varies enormously across entries, from 90 likes (T024, a hands-only cooking video with no convenience framing) to 738,400 likes (T040, "My most VIRAL single serve oven baked meal prep recipe"). That is a difference of more than 8,000 times between two entries in the same dataset, ostensibly about the same topic. This range makes aggregate engagement statistics almost meaningless, and it points to something the dataset cannot fully capture: the role of the creator's existing audience. A creator who is already a vertically established food influencer with a large following will generate high engagement regardless of what they cook, while a smaller or newer creator making equivalent content will not. The `impact_level` field records a snapshot of visible likes at the time of collection, but it cannot tell us how much of that engagement came from the content itself versus the creator's pre-existing platform position.

---

## V. What the Data Conceals

### The Limits of Text-Based Annotation

The most significant limitation of this dataset is that the majority of its fields, and all of the Phase 2 fields, were annotated from text signals (titles, captions, handles) rather than from watching the videos themselves. `lifestyle_context` and `health_framing` in particular are inferences, not observations. A video titled "dinner for one" could be addressing a solo diner, someone cooking a separate meal while their partner eats something else, or a creator who simply liked the phrase. The title does not tell me which.

This limitation is structural. Thorough re-watching of all 60 videos to verify Phase 2 annotations would have been feasible but time-intensive, and it would still not resolve the interpretive difficulty of translating visual and narrative cues into categorical fields. As Gebru et al. (2021) argue in their "Datasheets for Datasets" framework, responsible dataset documentation requires honesty about the gap between what data represents and the phenomenon it is meant to capture. This dataset documents a genre of TikTok content; it does not document the lived experiences of the creators or viewers involved.

### The Algorithm Is Also a Co-Author

The search terms I used ("single serving meal," "cooking for one," "dinner for one," "easy meal for one") shaped the dataset in ways I can partially but not fully account for. TikTok's search function and recommendation algorithm determine which content is returned for a given query. The `source_search_term` field, added in Phase 2, captures which search term I used for each entry, but it does not capture the full logic of why those particular videos appeared. As Schellewald (2023) notes, TikTok's algorithm is not transparent; users and researchers alike engage with it as a kind of imagined affordance; we develop intuitions about how it works without direct access to its logic.

This means the dataset reflects a collaboration between my search decisions and TikTok's algorithmic curation. The content that appears in this dataset is not a random sample of single-serving cooking content; it is a sample of what the algorithm made visible to a user conducting those searches at that time. A different researcher, searching the same terms on a different day or from a different account, might get a meaningfully different set of results.

### What Is Missing Entirely

The dataset does not include creator demographics, geographic location, or any information about audience beyond the visible like count. It does not capture comments, which is where much of the cultural negotiation around solo cooking (questions of loneliness, self-sufficiency, frugality, dietary identity) actually takes place. It does not include non-English content, which means it cannot speak to how single-serving cooking is framed in other language communities on TikTok. And it does not track content over time: the dataset is a cross-sectional snapshot, not a longitudinal record of how this genre has evolved.

Research on solo dining and eating alone has noted that cooking and eating by oneself carries complex social meanings: it can be experienced as freedom, as loneliness, as self-care, or as necessity, often simultaneously (Joosse & Mäkinen, 2022). These meanings are present in the content I collected, visible in titles like "Eating well alone is essential" (T050) or "Table for One" (T033), but the dataset's categorical fields cannot capture their nuance. The notes field was designed to hold some of this complexity, but in practice it was underused.

---

## VI. Computation, Scale, and What Changed Between Them

Phase 1 and Phase 2 of this project involved different kinds of interpretive labor, and the difference matters. In Phase 1, I watched each video, made annotation decisions in real time, and built up a sense of the genre through direct engagement with the content. That process was slow and sometimes uncertain, but it was grounded.

In Phase 2, annotation was mediated by an AI assistant working from text fields rather than video content. The consistency gains are real: the same logic was applied to all 60 entries for the new fields, but they came at the cost of the contextual judgment that comes from actually watching the content. This trade-off is not unique to this project; it is a defining feature of computational annotation at any scale. As Wang et al. (2024) found in their study of teenagers' interactions with TikTok food videos, the meaning of food content on the platform is deeply contextual, shaped by audio, visual style, creator persona, and comment culture in ways that text-based analysis cannot fully recover.

The lesson I take from this is not that computational augmentation is bad, but that it is different. Phase 1 and Phase 2 produced different kinds of knowledge about the same dataset. The bespoke phase gave me a feel for the genre; the augmentation phase gave me additional structured dimensions to analyze. Both are valuable. Neither is complete.

---

## VII. Situating the Work in Scholarship

This project sits at the intersection of platform studies, food culture research, and the emerging literature on responsible data practices in the digital humanities.

Within platform studies, the scholarship on TikTok's affordances provides essential context for understanding what this dataset is measuring. Schellewald's (2023) argument that TikTok's For You Page constitutes a distinctive mode of social engagement, one defined by algorithmic curation rather than social networking, which explains why the content I found through search may not represent the full range of single-serving cooking content on the platform. What the algorithm surfaces is not a neutral sample; it is a curated selection shaped by engagement signals, content policies, and recommendation logic.

Within food culture research, Joosse and Mäkinen's (2022) work on solo dining as a cultural phenomenon offers a useful frame for understanding what is at stake culturally in the genre I studied. Their argument that solo dining occupies a space between aloneness and togetherness, a practice that is physically solitary but socially mediated, which maps onto the TikTok context in interesting ways. A creator filming themselves cooking alone, for an audience of potentially millions, is performing solo cooking as a social act. The "single serving" is not just a portion size; it is a cultural position.

Finally, Gebru et al.'s (2021) "Datasheets for Datasets" framework has been a guiding touchstone throughout this project. Their argument that datasets should document their composition, collection process, and limitations with the same care given to the data itself is the reason this essay exists alongside the dataset rather than as a separate afterthought. The goal of responsible data work is not to produce a perfect dataset (there is no such thing) but to make the imperfections legible so that others can use the data critically.

---

## VIII. Lessons Learned

The most important thing I learned from this project is that every dataset is an argument. The fields I chose to include, and the ones I did not, already encoded a theory of what matters about single-serving cooking content on TikTok. Choosing to record `convenience_emphasis` rather than, say, `emotional_tone` or `creator_follower_count` was a decision about what aspects of this cultural phenomenon were worth tracking. That decision was not neutral, and it was mine.

I also learned that manual data creation is irreplaceable as a starting point. The 60-entry bespoke phase was where I developed the intuitions that made the Phase 2 augmentation possible. I learned what "implicit" convenience looks like in practice. I noticed that carousel posts behaved differently from videos and chose to record them separately rather than exclude them. I observed that some creators appear in a numbered series ("Part 14," "Episode 62") while others post standalone videos, a distinction the dataset does not currently capture but that points toward interesting questions about serialized versus episodic cooking content.

Finally, I learned that the gap between what you intend to measure and what you actually measure is always larger than it appears when you start. This is not a failure. It is the honest condition of any empirical inquiry into cultural phenomena that are richer, more contextual, and more ambiguous than any dataset can fully represent.

---

## IX. Conclusion

Sixty entries, ten original fields, four augmented fields, two dataset versions, and one semester later: what do I have? A partial, imperfect, carefully documented record of how single-serving cooking content circulates on TikTok. A dataset that captures something real about how creators frame convenience, presentation, and food culture in short-form video, while remaining honest about everything it cannot see.

The genre of single-serving cooking content is not just about portion sizes. It is about how people narrate the experience of feeding themselves alone, and how that narration is shaped by platform affordances, algorithmic visibility, and the social meanings of solo domestic life. This dataset is a first attempt to make some of those patterns visible in structured form. The questions it opens, about health discourse, about cultural representation in food content, about the relationship between algorithmic curation and the content creators make, are more interesting than the ones it closes.

That feels like the right place to end a semester-long project.

---

## References

Gebru, Timnit, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman Vaughan, Hanna Wallach, Hal Daumé III, and Kate Crawford. "Datasheets for Datasets." *Communications of the ACM* 64, no. 12 (2021): 86–92. https://doi.org/10.1145/3458723

Joosse, Sander, and Piia Mäkinen. "Solo Dining at Home in the Company of ICT Devices." *Frontiers in Computer Science* 3 (2022): 818650. https://doi.org/10.3389/fcomp.2022.818650

Schellewald, Andreas. "Understanding the Popularity and Affordances of TikTok through User Experiences." *Media, Culture & Society* 45, no. 4 (2023): 763–778. https://doi.org/10.1177/01634437221144562

Wang, Ching, Elizabeth Kaziunas, and Citing Chung. "From Viral Content to Real-Life Cuisine and Beyond: Examining Teenagers' Interactions with TikTok Food Videos and the Influence on their Food Practices." *Proceedings of the ACM on Human-Computer Interaction* 8, CSCW2 (2024). https://doi.org/10.1145/3686928

---

*AI Usage Disclosure: Claude (Anthropic) was used to assist with Phase 2 computational annotation, to help identify relevant scholarly literature, and to help draft and refine the language of this essay. All interpretive decisions, analytical conclusions, and reflections on the data collection process are the author's own.*
