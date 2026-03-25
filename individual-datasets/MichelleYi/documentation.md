# Extreme Eating as Digital Performance – Initial Dataset Documentation

## Initial Dataset

This dataset consists of approximately 75 manually collected YouTube videos focused on extreme eating content. Each video is treated as a single data point and includes structured attributes such as creator, upload date, food type, portion size, food quantity, and estimated calories.

The dataset is organized to support comparison across:
- **creators** (ErikTheElectric, Matt Stonie, Nikocado Avocado)
- **time periods** (early, mid, recent)
- **food characteristics** (type, quantity, calories, portion size)

This structure allows for analysis of how extreme eating content changes over time and across creators.

---

## Initial Documentation

### Cultural Materials & Approach

This project focuses on extreme eating videos on YouTube as a form of digital food culture. These videos were selected because they transform food into spectacle, performance, and entertainment.

The dataset was created **from scratch** through manual collection and annotation of publicly available videos. This approach allowed for close engagement with each data point and highlighted the interpretive decisions involved in constructing a dataset.

---

### Computational Tools

Several tools were used to support the dataset creation process:
- **YouTube interface and metadata** to collect structured information such as upload date and view counts
- **Google Sheets** to organize, sort, and structure the dataset
- **ChatGPT** to assist with estimating calorie values and maintaining consistency across entries

These tools improved efficiency but had limitations. For example, calorie estimates required assumptions and could vary depending on interpretation.

---

### Interpretive Decisions & Methodology

Key decisions included:

- **Inclusion criteria:** Only extreme eating, food challenge, or mukbang-style videos were included. Recipe videos, reviews, and standard meals were excluded to maintain focus.
- **Unit of analysis:** Each video was treated as one data point.
- **Food categorization:** Foods were grouped into broad, consistent categories (e.g., burger, ramen, fast food (mixed)).
- **Portion size classification:** Portion size was categorized as moderate, large, or extreme based on perceived scale.
- **Calorie estimation:** When not explicitly provided, calories were estimated using standardized assumptions (e.g., calories per item or weight-based approximations).

A major challenge was balancing **consistency and accuracy**, especially when information was incomplete or exaggerated in the videos themselves.

---

### Challenges & Limitations

- Many videos lacked clear or reliable calorie and quantity information, making it difficult to estimate calories consumed.
- Portion size classification required subjective judgment

---

### Emerging Questions

This dataset raised questions about **how to define and measure “extreme” eating**. Decisions about portion size required balancing calorie estimates, food quantity, and perceived scale, showing that even basic categories rely on interpretation rather than fixed definitions.

---

## Next Steps (Scaling Plan)

To expand this dataset, I plan to scale from ~75 items to 500+ using computational methods such as:

- **YouTube API or web scraping** to collect additional videos
- **Keyword filtering** (e.g., “challenge,” “10,000 calories,” “mukbang”) to identify relevant content
- **LLM-assisted classification** to categorize food type, portion size, and calorie estimates

---

### What Will Change at Scale

At a larger scale:
- Manual interpretation will be partially replaced by automated classification
- Calorie estimation will rely more on generalized patterns
- Some nuance (e.g., tone, exaggeration, context) may be lost

---

### Anticipated Challenges

- Maintaining consistency across automated classifications
- Filtering irrelevant or mislabeled content
- Handling incomplete or inconsistent metadata
- Loss of interpretive depth compared to manual annotation

---

### Reflection

Scaling this dataset will highlight the tradeoff between **depth and scale**. While larger datasets allow for broader pattern recognition, they risk flattening the interpretive richness present in manually constructed data.