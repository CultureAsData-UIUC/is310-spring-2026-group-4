# Constraint-Driven Food Practices: Dataset Documentation  
### Diara Shah

---

## Project Overview

This dataset explores how food practices are shaped by everyday constraints, especially among college students and young adults. Instead of focusing on ideal or aesthetic food content, this project focuses on meals that are quick, cheap, easy or low-effort.

The goal is to understand how people adapt their eating habits under limitations such as time, money, energy, and kitchen access.

---

## Cultural Materials & Approach

The dataset was created from scratch using publicly available content from TikTok and Reddit.

- TikTok was used to observe how meals are visually presented  
- Reddit was used to understand how people describe their situations and constraints  

Posts were included if they showed or described at least one constraint.

---

## Dataset Structure

The dataset contains approximately 50 posts.

Each entry includes:

- Platform (TikTok or Reddit)  
- Link to the post  
- Type of constraint (time, money, space, energy)  
- Whether the constraint is explicit or implied  
- Type of food (homemade, packaged, dining hall, etc.)  
- Level of effort  
- Tone (humorous, neutral, complaining, etc.)  

This structure focuses on how people adapt to constraints, not just what they eat.

---

## Computational Tools

Computational tools were used mainly for searching and organizing data.

- TikTok hashtags and Reddit keywords were used to find posts  
- Google Sheets was used to structure and organize the dataset  

These tools helped speed up the process, but they also have limitations. Platform algorithms really influence what content is shown, meaning the dataset is not fully neutral.

---

## Key Decisions

- Only public posts were included  
- Posts had to include some context (caption, text, or explanation)  
- Highly aesthetic or “perfect” food content was excluded because it does not match the focus on everyday constraint-based food practices.

The dataset focuses on everyday, realistic food practices rather than idealized content.

---

## Challenges

- Some constraints were implied rather than clearly stated  
- Tone (especially humor) was sometimes difficult to interpret  
- TikTok (video) and Reddit (text) are different formats, making comparison harder 
- The process was time-consuming, as each post required manual review without automated tools.
- Keeping categories consistent across different posts  

These were addressed by refining categories during the collection process.

---

## Observations

Some early patterns include:

- Constraints are often treated as normal in college life.
- Meals prioritize speed and convenience.
- Common strategies include microwave cooking, meal prep, and cheap substitutions to save money and time.
- TikTok content is more visually polished, while Reddit is more direct and detailed often including people asking for advice and receiving detailed responses.
---

## Next Steps

To expand this dataset, I plan to use simple computational methods that build on my current approach:

- Collect more Reddit posts using keyword searches (e.g., “cheap meals,” “dorm food,” “too tired to cook”) to increase dataset size  
- Collect additional TikTok posts using hashtags, while recognizing platform limitations  

- Use basic text analysis (in Python or similar tools) to identify common words and patterns (e.g., “cheap,” “quick,” “tired”)  
- Analyze how frequently different types of constraints appear across posts  

- Apply simple keyword-based rules to help label constraints  
  - Words like “busy” or “late” → time constraint  
  - Words like “broke” or “budget” → money constraint  

- Compare computer-generated labels with manual labels to see if they match

- Identify patterns across platforms (e.g., differences between TikTok and Reddit)

### Anticipated Challenges

- Automated labeling might miss meaning, especially when constraints are not clearly stated  
- Platform algorithms affect what content is shown and collected  
- It may be harder to keep labels consistent as the dataset gets larger  

### Expected Changes with Scale

- Larger datasets may make patterns easier to see  
- Some detail from manual labeling may be lost  
- There will be more reliance on simple computational methods  


The goal is to balance scale with maintaining meaningful interpretation.

## AI Usage Statement

This documentation was refined with the assistance of ChatGPT ONLY for clarity and wording. All the dataset collection, annotation, categorization decisions, and interpretation were done by me.