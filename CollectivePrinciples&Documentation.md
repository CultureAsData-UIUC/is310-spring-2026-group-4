# Collective Principles & Documentation: Food as Cultural Data

**IS310 - Culture As Data | Spring 2026 | Group 4**  
---

## About This Document

This document synthesizes what us (Group 4) collectively learned about working with food as cultural data. It is methodological guidance and collective wisdom for future researchers - not a repeat of our individual essays.

---

## I. What Future Researchers Should Know Before Starting

### Working with food as cultural data is always working with power

We learned that food data is never neutral. Every dish/item in any of our food dataset carries a history of who made it, who profited from it, who got credit, and who did not. Before choosing a dish, a platform, or a metric, ask: whose labor created this food? Whose voice is represented in the sources you are collecting? Whose is absent? A dataset about food is always also a dataset about immigration, economics, race, and cultural ownership - whether you name those dimensions explicitly or not.

### The source type is as important as the content

In food media research, what a source ***is*** determines what it can say. Recipe aggregators have structural format constraints that make cultural framing almost impossible - a recipe card has no space for history. Community food blogs are authored by people with personal stakes but corporate sites have brand incentives. Understanding these structural differences before you collect data will prevent you from treating all sources as equivalent observations.

### Absence is data

Whenever there is a null observation or entries in any of our datast, such absence is meaningful - but it is not self-interpreting. We believe absence could mean deliberate erasure, format constraint, audience assumption, or editorial policy. Your methodology needs to distinguish between these before you can say what the silence means.

### Web collection is not and might never be a neutral sample

If you collect data by scraping or searching the web, the corpus you retrieve reflects search engine optimization, corporate marketing budgets, platform algorithms, and which communities have had access to publishing infrastructure. For example, in Flynn's immigrant food dishes dataset, a dish that is heavily marketed by fast food chains will generate far more web content than a dish that is primarily made in home kitchens and community restaurants. Your dataset will be skewed by this before you write a single line of code.

---

## II. Principles for Working with Food as Cultural Data

The following principles emerged from our diverse approaches to food media, social media, and recipe data. They are intended as guidance for future IS310 students and other researchers working in this space.

### Principle 1: Document your coding scheme as if someone else will use it

- Qualitative coding of cultural materials. Write down what you decided and why. Include examples of hard cases. If you change a category definition mid-project, note when and why. The coding scheme is part of the dataset.
- Even if AI is doing majority of the heavy lifting, make sure you note down each prompt so it's more easily reproducible.


### Principle 2: Treat LLM annotation as a first draft rather than a final product

- We learned that LLMs can apply a coding scheme consistently at scale, but they make systematic errors in ambiguous cases and cannot access context that is not in the text excerpt. Always define a review process, such as documenting cases where you disagreed with the model and why. 

### Principle 3: The platform will shape the data

- Whether your source is TikTok, Reddit, a recipe blog, or a corporate website, the platform's design, moderation policies, algorithm, and audience norms shape what gets posted and how. We noticed that platform is a variable, and it is not a neutral conduit.

---

## III. What Each Member Learned (To be completed by each member)

> **Instructions:** Add 2–3 sentences describing the most important methodological lesson from your individual project. Focus on what you would tell a future researcher doing similar work, not on summarizing your findings.

**Flynn Huynh** - I learned that manual data creation before computational scaling is somewhat mandotory, because it is where you learn what your categories actually mean and where the edge cases live. The categories that seemed clear in the abstract (e.g., "community credit given") turned out to require constant judgment calls in practice, and those judgment calls need to be made by a human before you can ask a machine to make them at scale. I did have a hard time with that sections.

**Cynthia Shen** - I learned that descriptive field recording, even when it creates inconsistency, often preserves more analytical value than premature standardization. When I recorded dish names exactly as creators wrote them in their captions, the same food category ended up with wildly different labels across entries; but that variation itself turned out to reflect how creators brand and position their content for algorithmic visibility. A future researcher should resist the urge to clean and standardize too early, because the messiness in raw cultural data is often where the meaning lives.

**Michelle Yi** - I learned that scaling a dataset changes the type of patterns you can see, but it also removes a lot of nuance. The larger scaled dataset made engagement trends and creator differences easier to analyze, while the manual dataset made it easier to notice contextual details that could not be captured automatically. I would tell future researchers that computational methods are useful for identifying broad patterns, but cultural performance and spectacle are often difficult to fully measure through metadata alone.

**Rana Bouchama** - I learned that even with good intentions, one can still make mistakes in representing data. For instance, in an earlier version of my dataset I added a race/ethnicity category, the intent was to show the disparity in the for you page overwhelmingly pushing white creators, however this was a flawed way of going about it as my own assumptions of peoples racial/ethnic backgrounds may not match up to how the individual identifies. In trying to do good, ultimately I was perpetuating the same problems I was aiming to solve.

**Soham Solanki** - The most important lesson from this project is that running multiple independent classification methods on the same content is worth the time and effort, especially the disagreements between them. Where my manual coding, LLM classification, and regex pass converged, I had validated findings; where they diverged, I had the most interesting videos to dive deeper, like the ones doing several kinds of cultural work at once and refusing single-category placement. A future researcher should build that triangulation in from the start rather than treating it as a validation step at the end, and should pay particular attention to which patterns get undercounted by caption-only analysis when the piece of media being analyzed performs them visually.

**Diara Shah** - I learned that computational "blindness" is a very important factor to account for when moving between text-based and visual-based platforms. My project showed that while a computer can easily read explicit struggle on Reddit, it misses the implicit cultural "performance" on TikTok, proving that manual documentation of visual cues is essential to prevent huge data loss in digital food studies or other topics too.

---

## IV. Contributor Notes

| Member | Contribution to this document |
|---|---|
| Flynn Huynh | Drafted full structure|
| Cynthia Shen | What I learned |
| Michelle Yi | What I learned |
| Rana Bouchama | What I learned |
| Soham Solanki | Principle and Learnings |
| Diara Shah | Learnings  |
