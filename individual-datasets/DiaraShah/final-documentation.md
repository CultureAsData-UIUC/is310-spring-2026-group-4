# Dataset Documentation: Auditing the "Struggle/Easy Meal"

**IS310 - Culture As Data | Spring 2026**    
**Author:** Diara Shah  
**Repository:** `is310-spring-2026-group-4`

---

## I. Quick Reference

| Category | Details |
| :--- | :--- |
| **File Name** | `constraint_food_final_audited.csv` |
| **Total Entries** | 50 |
| **Overall Accuracy** | 76.00% |
| **Platforms** | Reddit (r/EatCheapAndHealthy, r/college, r/Cooking), TikTok |
| **Annotation Tool** | Custom Python Keyword Script (`label_validation.py`) |
| **Date Range** | 2010–2026 |

---

## II. What Is This Dataset?

This dataset documents the **"Struggle/Easy/Fast Meal" culture** of university students by tracking how food preparation is dictated by four primary constraints: **Money, Time, Space, and Energy.** The project is to measure the "readability" of student struggle. I built a bespoke dataset of 50 entries, then developed a Python-based computational auditor to see if a machine could identify these constraints as accurately as a human could. The dataset captures the tension between **explicit documentation** (Reddit users stating their problems) and **implicit performance** (TikTok creators showing their constraints thorugh visual cues).

---

## III. Column Reference

| Column | Type | Description |
| :--- | :--- | :--- |
| `id` | Integer | Unique identifier for each entry (1–50) |
| `platform` | String | Source platform: `reddit` or `tiktok` |
| `post_link` | String | Direct URL to the original post |
| `approx_date` | Integer | Estimated year of posting |
| `constraint_type` | String | **Ground Truth:** Human assigned label (Money, Time, Space, Energy, Skill) |
| `constraint_expression`| String | How struggle is conveyed: `explicit` (text) vs `implicit` (vibe/visual) |
| `adaptation_strategy` | String | The solution used (e.g., `microwave_only`, `meal_prep`, `one_pot`) |
| `food_type` | String | Categorization of ingredients: `homemade`, `packaged`, or `mixed` |
| `effort_level` | String | Labor required: `low` or `medium` |
| **`comp_label`** | String | **Audit Result:** The category assigned by the Python keyword script |
| `search_query` | String | The specific hashtag or subreddit search used for discovery |
| `framing_of_constraint`| String | Emotional framing: `problem` (burden) vs `normalized` (lifestyle) |
| `tone` | String | Delivery style: `neutral` or `humorous` |
| `visual_cues` | String | **TikTok Only:** Physical proof of struggle (e.g., "mini-fridge," "cramped desk") |
| `notes` | String | Qualitative text used by the Python script for matching |
| **`label_match`** | Boolean | **Audit Logic:** `True` if machine matches human; `False` if not |
| **`post_age`** | Integer | Years elapsed between post date and 2026 baseline |

---

## IV. The Computational Audit Logic

To test the machine’s ability to "see" culture, I build classifier. This represents how a basic algorithm "thinks" about student food.

### The Keyword Dictionary:
* **Money:** `cheap`, `broke`, `budget`, `frugal`, `price`, `affordable`, `save`, `cost`, `£`
* **Time:** `quick`, `fast`, `minute`, `busy`, `ready`, `prep`, `efficient`, `routine`, `week`
* **Energy:** `tired`, `lazy`, `low effort`, `depressed`, `spoon`, `mental health`, `exhausted`
* **Space:** `dorm`, `microwave`, `mini fridge`, `no kitchen`, `kitchenless`, `fire alarm`

**IMP Design Choice:** I included "spoon" and "mental health" in the **Energy** category to account for the "Low-Spoon Cooking" community on Reddit, which documents cooking as a struggle against burnout rather than just a lack of time.


## V. Detailed Findings & Distribution

### 1. Accuracy by Platform
| Platform | Total Entries | Accuracy % |
| :--- | :--- | :--- |
| **Reddit** | 22 | 81.81% |
| **TikTok** | 28 | 71.42% |

The **10% gap** between platforms reveals a structural finding: Reddit is a text-centric archive where constraints are explicitly stated, making them highly machine-readable. TikTok is a more visual-centric archive where constraints are often "invisible" to text-based scripts.

### 2. The "0% Accuracy" Cluster
Certain search queries resulted in a **0.0% match rate**, meaning the computer failed every single time. These include:
* `#studenthacks`
* `#kitchenless`
* `r/college "what do you eat"`
* `#onepotmeal`

**Analysis:** In these cases, the computer returned `unknown`. While a human sees "paper plates and a bathroom sink" (`#kitchenless`) and correctly labels it as a **Space** constraint, the computer finds no matching keywords in the description. This highlights the **limitation of text-as-documentation** for all visual platforms.

---

## VI. Known Limitations & Ethics

1. **The Metadata Gap:** The `visual_cues` column was manually recorded but was not accessible to the Python script. I did this to show that a simple computer program is "blind" to anything that isn't written down. It proves that if a student shows their struggle in a video but doesn't type it in the caption, the computer will miss it completely.
2. **Platform Imbalance:** The dataset slightly favors TikTok (28 entries) over Reddit (22). This reflects the higher volume of "lifestyle" food documentation currently being produced on TikTok.
3. **Positionality:** The categories (Money, Time, Space, Energy) were defined based on the observation of "Student Struggle." A creator might see their "One Pot Meal" as a choice, while this dataset codes it as a **Time/Energy** constraint.
4. **Privacy:** All data was collected from public subreddits and public TikTok tags. No private usernames or identifiable personal info were included in the final CSV.

---

## VII. Files in This Folder

```text
DiaraShah/
|- constraint_food_dataset_final.csv  <- Original manual dataset (pre-audit)
|- constraint_food_final_audited.csv  <- Final dataset with audit results
|- label_validation.py               <- The Python script used for the audit
|- search_strategy_audit.csv         <- Effectiveness report for search terms
|- my_audit_mistakes.csv             <- Log of every time the computer failed
|- final-data-essay.md               <- The data essay
|_ final-documentation.md            <- This file (Technical documentation)