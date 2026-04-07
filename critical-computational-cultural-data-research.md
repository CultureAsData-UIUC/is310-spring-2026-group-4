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
<summary><strong><b>Cynthia Shen</b></strong> — Camera Eats First: Exploring Food Aesthetics Portrayed on Social Media Using Deep Learning</summary>

## Bibliographic Information

**Authors:** Alessandro Gambetti, Qiwei Han

**Title:** Camera Eats First: Exploring Food Aesthetics Portrayed on Social Media Using Deep Learning

**Publication venue:** International Journal of Contemporary Hospitality Management

**Year:** 2022

**DOI:** https://doi.org/10.1108/IJCHM-09-2021-1206

**Article link:** https://www.emerald.com/ijchm/article/34/9/3300/117219/Camera-eats-first-exploring-food-aesthetics

**Code repository:** https://github.com/Data-Science-Knowledge-Center-Nova-SBE/food-aesthetics

---

## Part 1: AI Summary

**Prompt used:**

> "Please summarize the following research article in 1–2 paragraphs, focusing on:
> (1) what the data is,
> (2) what computational methods are used,
> (3) what the authors' main contribution is, and
> (4) how the article relates social media food images to broader questions of visual representation.
>
> Please keep the summary descriptive rather than critical, since I will write the critique separately.
>
> Article: Alessandro Gambetti and Qiwei Han, 'Camera Eats First: Exploring Food Aesthetics Portrayed on Social Media Using Deep Learning,' International Journal of Contemporary Hospitality Management, 2022, DOI: 10.1108/IJCHM-09-2021-1206."

**AI-generated summary (ChatGPT Thinking mode):**

This article studies how food is visually represented on social media using a large dataset of food images from Yelp. The authors treat these images as cultural data that reflect how people present food online, especially through aesthetics such as color, plating, composition, and visual appeal. Rather than only identifying what the food is, the paper asks how food looks across different restaurant settings, including cuisine types, rating levels, chain versus non-chain restaurants, and customer-posted versus owner-posted images.

To analyze this, the authors build a deep learning model that assigns each image a food aesthetics score. They adapt a pre-trained image aesthetics model and fine-tune it on food-related visual data, then compare the model’s results with human judgments and known photographic features. The paper’s main contribution is a way to measure food aesthetics at scale, showing that social media food images do not just record meals, but also shape how dining experiences are visually represented online.

---

## Part 2: My Critical Assessment

The data in this article is a large collection of food images from Yelp, which the authors use as a form of social media representation of dining. They focus on Las Vegas restaurants and collect 50,018 food images from 577 restaurants, along with metadata such as cuisine type, rating, price level, chain status, and whether the image was posted by a customer or the restaurant owner. This is useful because it shows how food is visually presented online at scale. However, the data is limited to Yelp, one city, and restaurant settings, so it leaves out other forms of food culture such as home cooking, everyday meals, and short-form video content. For my topic, this matters because TikTok single-serving meals are shaped not only by images, but also by captions, narration, editing, and platform trends, which this dataset cannot capture.

Computation is used mainly for analysis. The authors build a deep-learning model that assigns each food image an aesthetic score, then compare those scores across different restaurant categories and posting sources. This makes it possible to study visual patterns across a very large dataset that would be difficult to evaluate manually. At the same time, the method narrows representation to one main dimension: visual attractiveness. That is helpful for measuring food aesthetics, but it can flatten other meanings, such as comfort, convenience, affordability, or cultural familiarity. So the computational method is useful and mostly necessary for the article’s goals, but it also limits the kinds of claims the paper can make about food representation more broadly.

---

## Part 3: What AI Missed

The AI summary correctly described the article’s topic, data, and method, but it was too general. It did not stress that the dataset only comes from Yelp restaurants in Las Vegas, which limits how broadly the findings can apply. It also focused mainly on visual aesthetics and did not mention that important parts of online food culture—such as captions, narration, and everyday context—are missing from the data. Most importantly, it did not question how turning food images into a single aesthetic score may oversimplify other meanings, such as comfort, convenience, or cultural familiarity.

**Why I chose this article:**
This article is closely related to my topic, Representation of Single-serving Meals in TikTok, because it studies how food is visually represented on social media through computational methods. Although it focuses on social media food images rather than TikTok videos specifically, it is highly relevant to my project because single-serving meals on TikTok are also often framed through visual aesthetics, plating, color, and presentation. The paper is also a strong fit for the assignment because it is peer-reviewed, published within the required time range, and has publicly available code.

</details>

<details>
<summary><strong><b>Michelle Yi</b></strong> 
## Part 1: Article Summary
**Title:** “Food-101 – Mining Discriminative Components with Random Forests”
**Authors:** Lukas Bossard, Matthieu Guillaumin, Luc Van Gool
**Publication Year:** 2014
**DOI:** 10.1007/978-3-319-10599-4_29
**Code Repository:** https://github.com/alpapado/food-101 

**Prompt: “Summarize the following article in 1-2 paragraphs please.”**

**AI-generated Summary:** This article introduces Food-101, a large public dataset of 101,000 food images across 101 dish categories, and presents a new computer vision method for recognizing food in photographs. The authors argue that food recognition is especially difficult because dishes often do not have a fixed spatial structure and can vary a lot in appearance due to lighting, angle, and preparation style. To address this, they use Random Forests to identify discriminative visual “components,” or informative image regions, based on superpixels rather than traditional sliding-window patches. This makes the method more efficient and allows it to focus on local textures, colors, and patterns that help distinguish one dish from another.


The paper’s main contributions are both methodological and infrastructural. First, it proposes a new Random Forest–based component mining framework that can find useful visual parts for all food categories at once. Second, it introduces the Food-101 dataset as a benchmark for real-world food recognition. In their experiments, the authors show that their method achieves 50.76% average accuracy on Food-101, outperforming several alternative classification methods, including Improved Fisher Vectors and other discriminative part-mining approaches, though it does not beat a convolutional neural network. Overall, the paper helps establish food recognition as a serious computer vision problem and provides both a new dataset and an efficient recognition method for future research.


## Part 2: Critical Assessment
**What is the Data?**
What cultural data is being analyzed? (e.g., poems, tweets, film scripts, museum catalogs)
Where does it come from? How was it collected, gathered, or created? What is the scale?
What might be missing? What aspects of the cultural phenomenon doesn’t the data capture?
How well does the data represent the cultural phenomena? Does it capture complexity or flatten important dimensions?


This article analyzes photographs of dishes shared by users online. The images are taken from a food dataset called foodspotting.com, where users upload images of their food with the place and type of food. 750 training images and 250 testing images were collected for the 101 top most popular dishes. This led to a dataset of 101,000 images in total. Something that the dataset does not capture is the cultural meaning of a dish beyond its visual appearance. The images also only capture the final plated dish, which erases the process or variation that defines cuisine. Additionally, less globally visible or foods that are more difficult to label, may be excluded. As a result, I believe the data may reinforce dominant cuisines while underrepresenting others. I also believe that the data flattens the complexity of the emotional or symbolic meanings attached to food in different cultures. 


**How is Computation Used and Why?**
What computational methods are being used? Focus on what the method does conceptually.
What is the primary purpose? Is computation augmenting the data (cleaning, enriching), analyzing it (patterns, arguments), sharing it (storytelling, visualization), or some combination?
How do the article’s goals shape the data? How does the data shape the article’s claims?
Is computation necessary here? Would the same insights be possible without it?

The paper uses computer vision and machine learning to classify food images. It uses a Random Forest-based model, which essentially breaks images into smaller regions called superpixels and identifies which parts of an image are most useful for distinguishing between different dishes. Afterward, these are used to train classifiers that recognize food categories. The primary purpose of this is to identify patterns in food images and distinguish between different food categories. With the article’s goal being to accurately classify food images, the data only includes images, which suggests that food can be understood visually, but ignores cultural context. The scale of the dataset being 101,000 images would make it extremely difficult and ambitious to complete manual image classification. Machine learning allows the model to detect visual patterns and while similar insights could theoretically be achieved through human analysis, it would require a significant amount of labor, and would not be as efficient as computational methods.


## Part 3: What AI Missed	
The AI accurately summarized the key takeaways from the article. However, the summary skims over the computational methods used and does not elaborate in detail what the methods are and how they work. The AI oversimplified the computational methods, as exemplified in how they describe how the authors “use Random Forests to identify discriminative visual “components,” or informative image regions, based on superpixels rather than traditional sliding-window patches.” The summary fails to provide a description of what this technique means and how it works. Additionally, the summary does not address the limitations of the computational approach, with the lack of cultural context in the data.

</details>

<details>
<summary><strong><b>Rana Bouchama</b></strong> — SAPPHIRE: A stacking-based ensemble learning framework for accurate prediction of thermophilic proteins </summary>

> ## Bibliographic Information

**Authors:** Phasit Charoenkwan, Nalini Schaduangrat, Mohammad Ali Moni, Pietro Lio, Balachandran Manavalan, Watshara Shoombuatong 

**Title:** SAPPHIRE: A stacking-based ensemble learning framework for accurate prediction of thermophilic proteins

**Publication venue:** ScienceDirect

**Year:** 2022

**DOI/URL:** https://www.sciencedirect.com/science/article/pii/S0010482522004863?casa_token=i9X6MZxGmpQAAAAA:dftWHZChqxySHI55aYZCiQe53uRU3qm-91yH6kD5O-uICkcZK5ZfMXGLzf5-R9EifBkN7t0Qow

**Code repository:** https://github.com/plenoi/SAPPHIRE
>
## Part 1: AI Summary

**Prompt used:**

> "write me a 1-2 paragraph summary on this article https://www.sciencedirect.com/science/article/pii/S0010482522004863?casa_token=i9X6MZxGmpQAAAAA:dftWHZChqxySHI55aYZCiQe53uRU3qm-91yH6kD5O-uICkcZK5ZfMXGLzf5-R9EifBkN7t0Qow and include apa citation"

**AI-generated summary(ChatGPt):**

The article published in Computers in Biology and Medicine (2022) provides a comprehensive review of how deep learning techniques are applied to medical image analysis, with a particular focus on tasks such as image segmentation, classification, and disease detection. It explains that medical imaging—such as MRI, CT scans, and X-rays—produces complex, high-dimensional data that can be difficult to interpret using traditional methods. Deep learning models, especially convolutional neural networks (CNNs), are highlighted for their ability to automatically learn hierarchical features from images, enabling more accurate detection of abnormalities like tumors or lesions. The paper emphasizes that these methods significantly improve diagnostic accuracy and efficiency, supporting clinicians in making faster and more informed decisions.

The article also discusses the limitations and challenges associated with deep learning in medical imaging. These include the need for large, high-quality annotated datasets, the risk of overfitting, and the lack of interpretability in many models, which can hinder clinical trust and adoption. Additionally, computational cost and data privacy concerns are identified as barriers to widespread implementation. The authors suggest that future research should focus on explainable AI, improved data-sharing frameworks, and hybrid models that combine domain knowledge with machine learning. Overall, the study concludes that while deep learning has transformative potential in healthcare, careful validation and integration into clinical workflows are essential for its successful use.

APA Citation:
Author(s). (2022). Deep learning for medical image analysis: A review. Computers in Biology and Medicine, 152, 106347. https://doi.org/10.1016/j.compbiomed.2022.106347

## Part 2: My Critical Assessment

**What is the Data?**

The data in this article is a collection of Thermophilic Proteins (TTPS) identified by the SAPPHIRE computational program. The dataset was based on the pre-existing Charoenkwan2021 dataset and augmented by the SAPPHIRE program, which is meant to analyze strings and determine whether a protein is a TTPS or not. In this situation, there is no "cultural phenomenon" being observed; it has more to do with whether or not the SAPPHIRE is an effective model at identifying TTPS. Therefore, I would not say anything is necessarily "missing" from the dataset, nor does it flatten cultural context, as the data has little to do with the cultural context of these proteins to begin with. Moreso, the cultural element to it is how the SAPPHIRE can shape the culture around TTPS identification: whether or not the food industry will adopt its use on a grand scale.

**How is Computation Used and Why?**

Computation is a Machine Learning algorithm used for data analysis. In essence, you put in the DNA string for coding a certain protein, and the SAPPHIRE will return whether or not that protein is a thermophilic protein. The article wishes to make the argument that SAPPHIRE should be an industry standard. Therefore, the data must reflect positively on the SAPPHIRE. Charoenkwan et al. make the point to emphasize that the SAPPHIRE has a much higher success rate, 5.12% higher than its contemporaries. Whether or not that is statistically sound remains to be seen; admittedly, I am no expert, but I do believe that anything lower than 5% is statistically insignificant, which the SAPPHIRE only barely clears. Regardless, Charoenkwan et al.'s main goal is to argue for it to be the new industry standard, and therefore, they must make the data seem more successful than it is. Computation, in this case, is more than just necessary. Having a human being check individual strings of data is time-consuming and laborious; it would be much more efficient, as well as beneficial to whatever poor soul has to do that job, to have a machine check the strings.

## Part 3: What AI Missed

The AI completely missed a lot of this very central information. Perhaps this is in part due to my lacklustre prompting; however, it completely misses the point of the article. Not once is the article's namesake mentioned in the AI summary. It does not discuss the SAPPHIRE, nor does it discuss machine learning, models relating to TTPS analysis, or even TTPS as a whole. Rather, it seems ChatGPT has hallucinated a completely different article. At no point is medical imaging mentioned in the article, which, according to ChatGPT, is what the article is completely about. It feels almost like a waste of time going over everything the AI got wrong, because it got the entire article wrong. I had to copy and paste the link I sent into a new tab just to make absolutely certain I provided it with the right one and didn't accidentally paste something else. The only part of the article that is correct is the journal the article was published in. I'm not quite sure why the AI was completely unable to summarize this article, perhaps it is because you need to complete a CAPTCHA to access it, or perhaps because the full article is not free to the general public. But as a whole, this was a very eye-opening experience to see how AI can so often get it wrong.

</details>

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
| Cynthia | *Camera Eats First (Gambetti & Han, 2022)* | *Analysis* | *Computation converts large-scale social media food images into aesthetic scores, enabling comparison across restaurant types and posting sources — the method is used to identify patterns in visual representation rather than to build data infrastructure* | *To be filled after group discussion* |
| Michelle | *TBD* | *TBD* | *TBD* | *TBD* |
| Rana | *SAPPHIRE: A stacking-based ensemble learning framework for accurate prediction of thermophilic proteins* | *Analysis* | *Computation analyzes strings of DNA data to determine whether or not proteins are thermophilic. The article is mainly a justification for the use of this machine learning model called "SAPPHIRE" the AI summary was a complete hallucination and did not discuss the main ideas of the article.* | *To be filled after group discussion* |
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
| Cynthia Shen | Spectrum placement and individual parts finished |
| Michelle Yi | Individual article section completed |
| Rana Bouchama | ⬜ Individual part completed & Spectrum placement | 
| Soham Solanki | ⬜ Pending | 
| Diara Shah | Completed individual article section and contributed to group discussion and spectrum placement|
