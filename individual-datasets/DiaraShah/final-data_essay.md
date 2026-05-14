# Constraint Driven Food Practices & Why Computers Can’t See the Student Struggle

**IS310 - Culture As Data | Spring 2026** **Diara Shah** **My Dataset:** `constraint_food_final_audited.csv`  

---

## I. Introduction: The Question Behind the Data

When you see a TikTok of a student making "Oatmeal in a Plastic Cup," you aren't just looking at a breakfast recipe. You are looking at a document of specific physical and economic constraints: a lack of a kitchen, a limited budget, and perhaps only five minutes between classes. While a human viewer instantly recognizes the "dorm desk" or the "paper plate" as symbols of university struggle, a computer often sees only the text in the caption.

I built this dataset to explore the gap between **human observation** and **computational reading.** My main question was: **How readable is student food culture to an algorithm?** By tracking 50 posts across Reddit and TikTok, I documented the four primary constraints that dictate student life—**Money, Time, Space, and Energy** - and tested whether a simple keyword-matching script could identify these struggles as accurately as a human researcher.

The goal was not just to archive "struggle meals," but to prove that "documentation" is a human act. On Reddit, students explicitly type out their problems ("I am broke"), making them highly readable. On TikTok, students "perform" their struggle visually, making them almost invisible to basic text-based computation. This dataset makes that "blindness" visible.

---

## II. How the Data Was Made

### The Human Baseline (50 entries)
The first phase involved building a "bespoke" manual dataset. I selected 50 posts from Reddit (subreddits like `r/EatCheapAndHealthy` and `r/college`) and TikTok (hashtags like `#dormhacks` and `#brokestudent`). For every entry, I acted as the primary "annotator," recording not just the food type, but the **Constraint Type** and the **Visual Cues** (such as a mini-fridge or a bedside table used as a counter).

### The Computational Audit
After creating the human baseline, I developed a Python script (`label_validation.py`) to "audit" my own work. I built a computational dictionary-how a computer "thinks" - using keywords like "cheap," "microwave," and "tired." I then ran this script against my notes to see if the computer's guess (`comp_label`) would match my manual label at all (`constraint_type`). 

This was a deliberate test of "Computer Blindness." I withheld the `visual_cues` column from the script, forcing the computer to rely only on the text oNLY. This allowed me to measure exactly where a machine fails to understand the "vibe" or visual context of student culture.

## What the Data Reveals: The Audit Results

After running the computational audit across all 50 entries, the results confirmed that student struggle is often "performed" in ways that simple algorithms miss.

### Finding 1: The Platform Readability Gap
The computer achieved an overall accuracy of **76%**, but this number hides a significant platform divide. 
* **Reddit Accuracy: 81.8%**
* **TikTok Accuracy: 71.4%**

This **10% gap** proves that Reddit is a more "readable" archive for machines. Because Reddit is text-centric, students explicitly document their constraints ("I only have £20 for the week"). TikTok, however, is a visual culture. A creator might show a "dorm meal" without ever typing the word "dorm" or "limited space" in the caption. Because the computer is "blind" to the video, it fails to categorize the struggle.

### Finding 2: The "0% Club" (When Keywords Fail)
The most striking finding was the total failure of certain search queries. Terms like **#studenthacks**, **#kitchenless**, and **#onepotmeal** resulted in a **0% match rate** because the computer could not "see" the visual environment.


### Finding 3: Money is Explicit, Energy is Implicit
The computer was nearly 100% accurate when identifying **Money** constraints because the vocabulary of being "broke" or "on a budget" is very specific. However, it struggled with **Energy**. When a student posts about being "too tired" or needing a "low-effort" meal, the machine often confuses this with a Time constraint. It cannot distinguish between a lack of time (a busy schedule) and a lack of energy (burnout) because the machine lacks the empathy to understand the context of the post.

---

## What the Data Conceals

While the dataset successfully audits the "readability" of struggle, it also has built-in silences. By its design, the computational script was denied access to the `visual_cues` column as explained before. 

Furthermore, the dataset is limited by my own positionality also as explained in the dataset documentation. The data reflects my perspective as a student as much as it reflects the lives of the creators.

---

## Lessons Learned: The Value of Human Sight

The main takeaway from this project is that **manual data creation is irreplaceable** in some sense. If I had relied solely on the computer to build this dataset, I would have lost nearly 25% of the entries, and almost a third of the TikTok data would have been discarded as "unknown." 

Computational scaling is a powerful tool, but as this audit shows, it changes what you are measuring therefore verifying what the computer does is so important. A keyword script measures **vocabulary** and a human researcher measures **culture**. By comparing the two, I learned that the "struggle" in student food culture isn't just about what people say, but it's about the environment they are forced to cook in. The mini-fridge, the microwave, and the paper plate are data points that a computer cannot see, but they are the most easy and honest documents of student life we have.

---

## VI. Conclusion

In the end, this project proves that student food practices are driven by constraints that go far beyond a simple recipe. Whether it is a lack of money on Reddit or a lack of space on TikTok, these struggles are a fundamental part of the university experience. My audit shows that while we can use computers to help us organize this data, we cannot let them interpret it for us. 

Student culture is a "vibe" as much as it is a set of words. To truly document the "struggle meal," we need researchers who can see past the caption and understand the physical reality of the dorm room as a kitchen.

My findings on the 'readability' of student struggle align with broader scholarly conversations in the field of Digital Humanities. For example, my observation that keywords alone cannot capture the 'vibe' of a TikTok meal mirrors the work of D’Ignazio and Klein (2020), who argue that data collection must prioritize human context over simple numbers. Also the accuracy gap I discovered between text-heavy Reddit and visual TikTok supports Zulli’s (2022) theory that TikTok’s visual 'affordances' require a different kind of cultural reading than traditional text-based archives."

---
## References
D’Ignazio, Catherine, and Lauren F. Klein. *Data Feminism*. Cambridge, MA: MIT Press, 2020.

Zulli, Diana, and David J. Zulli. "Extending the Theory of Affordances: Why the TikTok Artifact Matters." *New Media & Society* 24, no. 8 (2022)

---

**AI Disclosure:** I used Gemini AI as a writing assistant to help simplify technical language, format citation, polish writing. All data analysis and research conclusions are my own.