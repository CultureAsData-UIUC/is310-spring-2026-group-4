# Critical Computing & Cultural Data: Building Principles Through Published Research

**IS310 — Culture As Data | Spring 2026 | Group 4**

---

## Table of Contents

- [Individual Article Summaries](#individual-article-summaries)
  - [Flynn Huynh](#flynn-huynh)
  - [Cynthia Shen](#cynthia-shen)
  - [Michelle Yi](#michelle-yi)
  - [Rana Bouchama](#rana-bouchama)
  - [Soham Solanki](#soham-solanki)
  - [Diara Shah](#diara-shah)
- [Group Landscape Mapping](#group-landscape-mapping)
  - [Step 1: Augmentation–Analysis–Communication Spectrum](#step-1-augmentationanalysiscommunication-spectrum)
  - [Step 2: Trends, Divergences, and Silences](#step-2-trends-divergences-and-silences)
- [Contributors](#contributors)

---

## Individual Article Summaries

<details>
<summary><strong><b>Flynn Huynh</b></strong> — TASTEset: Recipe Dataset and Food Entities Recognition Benchmark</summary>

## Bibliographic Information

**Authors:** Ania Wróblewska, Agnieszka Kaliska, Maciej Pawłowski, Dawid Wiśniewski, Witold Sosnowski, Agnieszka Ławrynowicz

**Title:** TASTEset — Recipe Dataset and Food Entities Recognition Benchmark

**Publication venue:** arXiv preprint (cs.CL) — *Note on peer-review status: this paper is hosted on arXiv, which is a preprint server and not itself a peer-reviewed venue. The paper does not indicate a conference or journal publication in its submission metadata. This is a limitation I flag in my critical assessment below.*

**Year:** 2022

**DOI:** https://doi.org/10.48550/arXiv.2204.07775

**arXiv page:** https://arxiv.org/abs/2204.07775

**Code repository:** https://github.com/taisti/tasteset

---

## Part 1: AI Summary

**Prompt used:**

> "Please summarize the following research paper abstract in 1–2 paragraphs, focusing on what the dataset is, what computational methods are used, and what the authors' main contribution is:
>
> 'Food Computing is currently a fast-growing field of research. Natural language processing (NLP) is also increasingly essential in this field, especially for recognising food entities. However, there are still only a few well-defined tasks that serve as benchmarks for solutions in this area. We introduce a new dataset -- called TASTEset -- to bridge this gap. In this dataset, Named Entity Recognition (NER) models are expected to find or infer various types of entities helpful in processing recipes, e.g. food products, quantities and their units, names of cooking processes, physical quality of ingredients, their purpose, taste. The dataset consists of 700 recipes with more than 13,000 entities to extract. We provide a few state-of-the-art baselines of named entity recognition models, which show that our dataset poses a solid challenge to existing models. The best model achieved, on average, 0.95 F1 score, depending on the entity type -- from 0.781 to 0.982. We share the dataset and the task to encourage progress on more in-depth and complex information extraction from recipes.'"

**AI-generated summary (Perplexity):**

This paper introduces TASTEset, a new benchmark dataset designed to advance Named Entity Recognition (NER) in the domain of food and recipe processing. The dataset comprises 700 recipes containing over 13,000 manually annotated entities spanning multiple categories relevant to culinary text: food products, quantities and their units, cooking processes, physical qualities of ingredients, ingredient purpose, and taste descriptors. The authors' core motivation is that, despite the rapid growth of "Food Computing" as a research area, there are very few standardized benchmarks for evaluating NLP models on food-related text — and TASTEset is their attempt to fill that gap.

To establish the dataset's utility, the authors benchmark several state-of-the-art NER models against it, reporting F1 scores that range from 0.781 to 0.982 depending on entity type, with the best model achieving an average F1 of 0.95. The dataset and associated code are publicly released to encourage further research into structured information extraction from recipe text. The primary contribution is therefore twofold: providing a labeled dataset for training and evaluating food NER systems, and demonstrating that this is a genuinely challenging task that existing models do not trivially solve.

---

## Part 2: My Critical Assessment

**What is the Data?**

Based on the description and my exploration, TASTEset consists of 700 recipes annotated with over 13,000 entity labels across nine categories: FOOD, QUANTITY, UNIT, PROCESS, PHYSICAL_QUALITY, PURPOSE, TASTE, PART, and COLOR. Each token in a recipe's ingredient list and instructions is labeled using the BIO tagging scheme (Beginning, Inside, Outside), which is the standard format for NER tasks in NLP.

What the paper does not clearly specify is **where the 700 recipes came from**. The abstract and publicly available description do not disclose the source websites, the selection criteria, or whether the recipes represent any particular cuisine tradition, cultural community, or geographic region. I believe this is a significant documentation gap.

What the data structurally cannot capture is anything about the **cultural context of a recipe**: who wrote it, what community it comes from, whether the dish has an immigrant origin, how the dish's history is framed, or whether the source credits a particular cultural tradition. TASTEset treats recipes as purely technical documents — a sequence of ingredients and instructions to be parsed — and strips away every dimension of food culture that is not expressible as a named entity. For my project's purposes, this means the dataset is a useful engineering tool but an analytically limited cultural artifact.

**How is Computation Used and Why?**

The computational method at the center of this paper is **Named Entity Recognition (NER)**, a supervised machine learning task where a model is trained to classify each token in a text as belonging to a predefined category or not. In practice, the authors fine-tune transformer-based language models (BERT-family architectures) on their annotated recipe dataset. The model learns to recognize patterns — for example, that words appearing before a unit of measurement are likely quantities, or that certain verbs in cooking instructions are PROCESS entities.

The primary purpose here is **augmentation**: computation is being used to structure unstructured text (recipe prose) into machine-readable labeled data that downstream applications can use. This is not an analysis paper making a cultural argument — it is infrastructure work. The authors are building a benchmark, not interpreting food culture. The implicit claim is that once recipes can be parsed into structured entities at scale, other researchers can build applications on top: recipe recommendation systems, ingredient substitution tools, or nutritional databases.

Is computation necessary here? For the benchmark-building goal, yes — the whole point is to evaluate whether NLP models can reliably extract structured information from recipe text, which requires both a labeled dataset and automated models to test against it. But it is worth noting that the manual annotation labor (human annotators labeling 13,000+ entities across 700 recipes) is what makes the computational benchmarking possible at all. The paper frames NER as the contribution, but the real labor is the human interpretive work that produced the labeled training data — a version of exactly the dynamic our IS310 course asks us to think about.

For my project's scaling phase, TASTEset's NER approach is directly applicable: NER could be used to automatically extract ingredient lists from scraped recipe sources, enabling systematic comparison of ingredient substitutions across immigrant-origin dishes at scale. However, NER alone cannot detect cultural framing, authenticity claims, or origin story narration — so it would need to be combined with other methods.

---

## Part 3: What AI Missed

The AI summary accurately described what TASTEset is and what NER does at a surface level — it correctly identified the entity categories, the benchmark framing, and the F1 score results. What it completely glossed over, however, was again the question of **where the data comes from and what that means**.  A critical reader or a food lover should immediately ask: are these recipes from one platform? What languages and cuisines are represented? The AI did not ask any of these questions and did not flag the absence of this information as a limitation.

I also think The AI also missed the tension between what the paper frames as its contribution (NER benchmarking) and where the actual interpretive labor lies (human annotation decisions). It described the dataset as something the authors "introduced" without acknowledging that someone had to decide what counts as a TASTE entity versus a PHYSICAL_QUALITY entity in ambiguous cases — a decision that shapes what the model learns. Finally, the AI showed no awareness of what the data **cannot** represent: recipe text treated as pure instruction sequences is a very thin slice of what food culture actually is.

**Bonus — Code Repository Reflection:**

The GitHub repository contains the annotated dataset in JSON and CoNLL format, annotation guidelines, and baseline model scripts. I noticed from reading the annotation guidelines that the paper itself doesn't fully discuss some decision. For instance, the distinction between PHYSICAL_QUALITY ("finely chopped") and PROCESS ("chop finely") depends on whether the descriptor modifies an ingredient state or describes an action, which is genuinely ambiguous in many recipe constructions.
</details>

<details>
<summary><strong><b>Cynthia Shen</b></strong> — Add your article title here</summary>

> **Replace this stub with your individual section.**
> **Commit this section yourself** so it registers under your GitHub username for the pass/fail grade.
</details>

<details>
<summary><strong><b>Michelle Yi</b></strong> — Add your article title here</summary>

> **Replace this stub with your individual section.**
> **Commit this section yourself** so it registers under your GitHub username for the pass/fail grade.

</details>

<details>
<summary><strong><b>Rana Bouchama</b></strong> — Add your article title here</summary>

> **Replace this stub with your individual section.**
> **Commit this section yourself** so it registers under your GitHub username for the pass/fail grade.

</details>

<details>
<summary><strong><b>Soham Solanki</b></strong> — Add your article title here</summary>

> **Replace this stub with your individual section.**
> **Commit this section yourself** so it registers under your GitHub username for the pass/fail grade.

</details>

<details>
<summary><strong><b>Diara Shah</b></strong> — FoodieQA: A Multimodal Dataset for Fine-Grained Understanding of Chinese Food Culture</summary>

> ## Bibliographic Information

**Authors:** Wenyan Li, Xinyu Zhang, Jiaang Li, Qiwei Peng, Raphael Tang, Li Zhou, Weijia Zhang, Guimin Hu, Yifei Yuan, Anders Søgaard, Daniel Hershcovich, Desmond Elliott  

**Title:** FoodieQA: A Multimodal Dataset for Fine-Grained Understanding of Chinese Food Culture  

**Publication venue:** arXiv preprint  

**Year:** 2024  

**DOI/URL:** https://arxiv.org/abs/2406.11030  

**Code repository:** https://github.com/lyan62/FoodieQA 
>
## Part 1: AI Summary

**Prompt used:**

> "Summarize this research paper in 1–2 paragraphs, focusing on what the dataset is, what computational methods are used, and what the main contribution is."

**AI-generated summary(ChatGPt):**

The paper presents FoodieQA, a multimodal dataset developed to evaluate the capability of artificial intelligence systems to understand culturally grounded food knowledge. The dataset consists of image-text pairs and structured question-answer tasks that focus on regional Chinese food culture, including aspects such as ingredients, cuisine types, and geographic origins. It includes three primary evaluation tasks: multi-image visual question answering, single-image visual question answering, and text-based question answering. The dataset is manually curated to ensure fine-grained representation of cultural details and to provide a benchmark for assessing model performance.

To evaluate the dataset, the authors apply vision-language models (VLMs) and large language models (LLMs) and analyze their performance across different tasks. The results indicate that while language models achieve relatively strong performance on text-based questions, models demonstrate significant limitations in visual understanding, particularly in tasks requiring multi-image reasoning. The study highlights the gap between current model capabilities and the complexity of cultural understanding, emphasizing the need for improved multimodal reasoning in AI systems.

## Part 2: My Critical Assessment

**What is the Data?**

The FoodieQA dataset is made up of around 389 images and 350 different Chinese food dishes, along with question-answer pairs about them. The questions focus on things like ingredients, regional origin, and cuisine type. The images were collected from volunteers instead of being scraped online, which helps with consistency but also limits where the data comes from.

Even though the dataset is meant to capture food culture, it only represents a very specific version of it. It focuses only on Chinese cuisine and reduces cultural knowledge into fixed questions and answers. Things like personal experience with food, context, or how food is actually eaten in real life are not included. So while it looks like it’s capturing “culture,” it’s really just capturing structured facts about food.

**How is Computation Used and Why?**

Computation is used to test how well different AI models can answer questions about food using both images and text. Nodels  are given tasks like identifying the region a dish comes from or understanding ingredients based on images. This helps researchers compare how well models perform with different kinds of inputs.

The main purpose of computation here is to analyze model performance. It makes sense to use computation because the dataset is too large to evaluate manually. But also the method assumes that answering these types of questions means the model understands food culture. In reality, models might just be recognizing patterns without actually understanding the cultural meaning behind the food. So the results might show performance but probably not real understanding.

The dataset is designed specifically to test model performance, so it structures food culture into tasks rather than doing any reflecting on how food is experienced in real life. 

## Part 3: What AI Missed

The AI summary explains the dataset and methods pretty well, but it doesn’t really question anything. It treats the dataset like it fully represents food culture, when it’s actually pretty limited. It only looks at Chinese cuisine and turns culture into simple Q n A pairs, which leaves out a lot of context.

It also assumes that if a model answers correctly, it understands the culture. But realistically, the model could just be picking up patterns without actually understanding what the food means. The AI summary doesn’t really address this gap.

</details>

---

## Group Landscape Mapping

> **⚠️ TBD after everyone has added their individual summaries.**
> For each section, note who contributed and whether anyone disagrees.

---

### Step 1: Augmentation–Analysis–Communication Spectrum

> Our articles are on the table below. For each placement, we give a specific example from the article justifying where it falls. 

| Member | Article | Primary Role | Justification | Agrees / Disagrees |
|---|---|---|---|---|
| Flynn | TASTEset (Wróblewska et al., 2022) | **Augmentation** | Computation structures raw recipe text into labeled entity data for downstream use — no cultural argument is being made; the output is infrastructure | *To be filled after group discussion* |
| Cynthia | *TBD* | *TBD* | *TBD* | *TBD* |
| Michelle | *TBD* | *TBD* | *TBD* | *TBD* |
| Rana | *TBD* | *TBD* | *TBD* | *TBD* |
| Soham | *TBD* | *TBD* | *TBD* | *TBD* |
| Diara | FoodieQA (Li et al., 2024) | **Analysis** | Computation is used to test how well models understand food culture using image and text questions. It shows that models struggle with cultural understanding, especially in images. | *To be filled after group discussion* |
---

### Step 2: Trends, Divergences, and Silences

#### Trends
- *TBD*

#### Divergences
- *TBD*

#### Silences
- *TBD*

---

## Contributors
> Further details regarding our contributions in the group part

| Member | Group Mapping Contributions |
|---|---|
| Flynn Huynh | Spectrum placement for TASTEset + GitHub/Markdown template set up |
| Cynthia Shen | ⬜ Pending |
| Michelle Yi | ⬜ Pending |
| Rana Bouchama | ⬜ Pending | 
| Soham Solanki | ⬜ Pending | 
| Diara Shah | Completed individual article section and contributed to group discussion and spectrum placement|