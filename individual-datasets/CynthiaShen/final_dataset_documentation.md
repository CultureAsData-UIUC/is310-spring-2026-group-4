# Single-Serving TikTok Dataset: Documentation

**IS310 - Culture As Data | Spring 2026**
**Cynthia Shen**

---

## Overview

This dataset examines how single-serving meals are presented and circulated in short-form cooking videos on social media, using TikTok as a case study. The project focuses on the cultural framing of cooking for one person and how creators adapt meals, narratives, and presentation styles to fit single-portion contexts.

Single-serving cooking videos often appear in contexts such as living alone, student life, quick meals, or small-batch cooking. By examining these videos closely, the dataset explores patterns in the types of meals that appear, how convenience is framed, and how creators present themselves within short-form video formats.

---

## Files in This Folder

| File | Description |
|---|---|
| `single_serving_tiktok_dataset.json` | Original 60-entry bespoke dataset created manually (Phase 1) |
| `single_serving_tiktok_dataset_v2.json` | Augmented dataset with 4 additional fields added via computational annotation (Phase 2) |
| `cli_data_entry.py` | Command-line tool used for structured data entry during Phase 1 |
| `summarize_dataset.py` | Python script for generating summary statistics from the dataset |
| `dataset_documentation.md` | This file |

---

## Dataset Structure

Each record in the dataset includes the following fields. Fields marked **Phase 2** were added during the computational augmentation stage.

| Field | Description | Phase |
|---|---|---|
| `item_id` | Unique identifier for each video | 1 |
| `video_title` | Title or caption of the TikTok post | 1 |
| `creator_handle` | TikTok creator username | 1 |
| `video_url` | Link to the original TikTok post | 1 |
| `dish_type` | Description of the food or recipe shown | 1 |
| `convenience_emphasis` | Whether the video emphasizes convenience (explicit / implicit / none) | 1 |
| `creator_presentation` | How the creator appears in the video (hands_only / voiceover / text_only / face_on_camera) | 1 |
| `video_length_seconds` | Duration of the video, or "Carousel" if the post is image-based | 1 |
| `impact_level` | Visible number of likes on the TikTok post | 1 |
| `notes` | Optional field for additional observations | 1 |
| `source_search_term` | The search term used to discover this video | 2 |
| `lifestyle_context` | The lifestyle context implied by the video (living_alone / student_life / meal_prep / general) | 2 |
| `health_framing` | Whether the video foregrounds health or nutrition goals (high_protein / low_cal / balanced / none) | 2 |
| `food_cultural_origin` | Broad cultural origin of the dish (western / asian / fusion) | 2 |

---

## Phase 1: Manual Dataset Creation

### Cultural Materials and Project Focus

The dataset was created from scratch through manual collection of publicly available TikTok posts. Videos were identified using the following search terms:

- "single serving meal"
- "cooking for one"
- "dinner for one"
- "easy meal for one"

Additional videos were discovered through related hashtags and TikTok recommendation feeds. Each video was manually reviewed and annotated according to the dataset fields defined above. This process involved interpretive decisions about how to categorize food types, identify convenience narratives, and determine creator presentation styles.

The dataset contains 60 items, allowing for close qualitative and quantitative analysis of patterns within single-serving cooking content.

### Interpretive Decisions

Several interpretive decisions were required during dataset creation.

First, food types were recorded descriptively rather than using a fixed controlled vocabulary. This preserves the specificity of individual dishes while still allowing for later categorization.

Second, convenience narratives were categorized into three levels:

- **explicit**: the video clearly emphasizes speed, ease, or minimal effort
- **implicit**: the cooking process appears simplified but convenience is not directly stated
- **none**: the video presents cooking without emphasizing convenience

Third, creator presentation styles were categorized based on how the creator appears in the video. Some creators appear on camera, while others present food preparation through hands-only demonstrations, voiceover narration, or text-based instructions.

Finally, posts that consisted of swipeable images rather than videos were recorded as "Carousel" in the duration field to distinguish them from timed videos.

### Computational Tools in Phase 1

Two Python scripts were built to assist the manual data collection process.

`cli_data_entry.py` provided a command-line interface with confirmation prompts and structured field validation, reducing the risk of inconsistencies across 60 entries.

`summarize_dataset.py` generates summary statistics from the dataset, including parsing functions for engagement metrics (handling formats like "30.8k"), duration parsing (handling formats like "1min02s"), and a rule-based dish classification system. Importantly, raw dish labels are preserved in the dataset itself; the classification is used only for summary purposes.

### Challenges

One challenge involved interpreting diverse video formats and presentation styles. TikTok posts often combine multiple narrative elements, making it necessary to determine a dominant presentation style for annotation.

Another challenge involved interpreting convenience narratives. In many cases, convenience is suggested through visual cues or simplified ingredient lists rather than explicitly stated.

Additionally, engagement metrics were recorded as visible like counts rather than normalized numerical values, since TikTok displays engagement in abbreviated formats such as "30.8k likes."

---

## Phase 2: Computational Augmentation

### Approach

After completing the 60-entry manual dataset, the dataset was augmented computationally by adding four new annotation fields to all existing entries. Rather than expanding the number of entries, this phase focused on deepening the complexity of annotations — an approach that reflects the instructor's feedback that scaling "is not so much in the number of videos but in the complexity of the annotations."

The four new fields were annotated using Claude (Anthropic's AI assistant) as an augmentation tool within the data curation workflow. Each entry's existing fields — including video title, dish type, creator handle, and convenience emphasis — were used as the basis for annotation. All annotations were reviewed for consistency and accuracy. Two data entry errors from Phase 1 were also identified and corrected during this process (T002 and T049 had field values shifted into incorrect columns due to manual entry mistakes).

### New Field Definitions

**`source_search_term`** records which of the four original search terms most likely led to this video. This field was specifically noted as missing in instructor feedback: "recording which search term or hashtag led you to each video directly in the dataset itself would make it much easier to analyze later whether different search terms surface different kinds of content." Of the 60 entries, 22 were attributed to "single serving meal," 14 to "easy meal for one," 13 to "cooking for one," and 11 to "dinner for one."

**`lifestyle_context`** captures the lifestyle framing implied by the video's title and content, using four categories: `living_alone` (16 entries), `meal_prep` (6 entries), `student_life` (1 entry), and `general` (37 entries). This field allows analysis of whether the platform's single-serving content is primarily addressed to people living alone versus people cooking efficiently for other reasons.

**`health_framing`** records whether the video foregrounds health or nutrition goals. The majority of entries (52) have no explicit health framing. Among those that do, `high_protein` (3 entries) and `low_cal` (2 entries) reflect common fitness-oriented framings on the platform, while `balanced` (3 entries) captures more general health-conscious presentation.

**`food_cultural_origin`** provides a broad classification of the dish's cultural background: `western` (43 entries), `asian` (9 entries), and `fusion` (8 entries). This field enables analysis of which food cultures are most represented in single-serving cooking content.

### Interpretive Decisions in Phase 2

Several interpretive choices shaped the Phase 2 annotations.

For `source_search_term`, because videos were not collected with systematic per-entry provenance tracking during Phase 1, the attribution is inferred from video titles, creator handles, and content — not from a direct log of which search term returned each result. This is a limitation that future data collection should address by logging search term provenance at the time of collection.

For `food_cultural_origin`, the categories are deliberately broad and reflect the dish's cultural roots rather than the creator's identity. "Fusion" was used where a dish combines elements from multiple culinary traditions without a single dominant origin. This classification is a coarse summary label and does not capture the full complexity of culinary cross-cultural exchange.

For `health_framing`, the field captures explicit or strongly implied health framing only. Videos that happen to feature nutritious ingredients without foregrounding health goals were coded as `none`.

### Limitations of Phase 2

The Phase 2 annotations are based on metadata available in the existing dataset (titles, dish descriptions, creator handles) rather than on direct re-viewing of the videos. This means that `lifestyle_context` and `health_framing` in particular are inferences from textual signals, not from full analysis of video content. A more rigorous Phase 2 would involve re-watching each video to verify annotations.

Additionally, the `source_search_term` field is reconstructed rather than directly logged, which introduces uncertainty for entries where the title does not clearly indicate which search term would have surfaced it.

---

## Preliminary Observations

Several patterns emerged from the dataset.

Most posts appear as standard videos rather than carousel posts. Of the 60 items, 43 are timed videos while 17 are carousel posts.

Convenience narratives appear frequently but are not universal. While some videos explicitly frame the meal as quick or easy, many present full cooking processes adapted for a single portion.

Creator presentation styles are highly varied, with an almost even distribution among hands-only cooking demonstrations, text-based instructions, voiceover narration, and face-on-camera presentation.

Several recurring food categories appear frequently, including pasta dishes, rice-based meals, and mixed entrée bowls. Western dishes dominate the dataset (43 of 60 entries), with Asian and fusion dishes representing a meaningful but smaller share.

Health framing is present but not dominant: only 8 of 60 entries foreground health or nutrition goals, suggesting that single-serving content is more broadly about portion adaptation than about health optimization.

The `living_alone` lifestyle context appears in 16 entries, confirming that solo living is a significant but not exclusive framing for single-serving content. The majority of entries use a more general framing not tied to a specific life situation.

---

## Known Data Quality Issues

- **T002**: Fields were shifted during manual entry; `convenience_emphasis` and `creator_presentation` values were corrected in v2.
- **T049**: `creator_handle` contained a concatenation error ("aloneAlex Reesh"); corrected to "Alex Reesh" in v2.
- TikTok URLs are subject to link rot. Videos may become inaccessible if accounts are suspended or content is deleted. Local archiving of videos was not completed for this dataset.

---

## Ethical and Privacy Considerations

All data in this dataset was collected from publicly available TikTok posts. No private communications or personal data beyond what creators have made public were collected. Creator handles are recorded as they appear publicly on the platform.

Engagement metrics reflect publicly visible like counts at the time of collection and may not reflect current values.

---

*AI Usage Disclosure: Claude (Anthropic) was used to assist with Phase 2 computational annotation and to help refine the language of this documentation. All data collection, field design, manual annotation, and interpretive decisions were made by the author.*
