## **Cultural Materials and Project Focus**

This dataset examines how single-serving meals are presented and circulated in short-form cooking videos on social media, using TikTok as a case study. The project focuses on the cultural framing of cooking for one person and how creators adapt meals, narratives, and presentation styles to fit single-portion contexts.

Single-serving cooking videos often appear in contexts such as living alone, student life, quick meals, or small-batch cooking. By examining these videos closely, the dataset explores patterns in the types of meals that appear, how convenience is framed, and how creators present themselves within short-form video formats.

The dataset consists of 60 manually annotated TikTok posts featuring single-serving meals.

### **Dataset Structure**

Each record in the dataset includes the following fields:

Field	Description
item_id	Unique identifier for each video
video_title	Title or caption of the TikTok post
creator_handle	TikTok creator username
video_url	Link to the original TikTok post
dish_type	Description of the food or recipe shown
convenience_emphasis	Whether the video emphasizes convenience (explicit / implicit / none)
creator_presentation	How the creator appears in the video (hands_only, voiceover, text_only, face_on_camera)
video_length_seconds	Duration of the video or “Carousel” if the post is image-based
impact_level	Visible number of likes on the TikTok post
notes	Optional field for additional observations

### **Data Creation Methodology**

The dataset was created from scratch through manual collection of publicly available TikTok posts. Videos were identified using search terms such as:

"single serving meal"

"cooking for one"

"dinner for one"

"easy meal for one"

Additional videos were discovered through related hashtags and TikTok recommendation feeds.

Each video was manually reviewed and annotated according to the dataset fields. This process involved interpretive decisions about how to categorize food types, identify convenience narratives, and determine creator presentation styles.

The dataset contains 60 items, allowing for close qualitative and quantitative analysis of patterns within single-serving cooking content.

### **Interpretive Decisions**

Several interpretive decisions were required during dataset creation.

First, food types were recorded descriptively rather than using a fixed controlled vocabulary. This preserves the specificity of individual dishes while still allowing for later categorization.

Second, convenience narratives were categorized into three levels:

explicit: the video clearly emphasizes speed, ease, or minimal effort

implicit: the cooking process appears simplified but convenience is not directly stated

none: the video presents cooking without emphasizing convenience

Third, creator presentation styles were categorized based on how the creator appears in the video. Some creators appear on camera, while others present food preparation through hands-only demonstrations, voiceover narration, or text-based instructions.

Finally, posts that consisted of swipeable images rather than videos were recorded as "Carousel" in the duration field to distinguish them from timed videos.

### **Challenges**

One challenge in creating the dataset involved interpreting diverse video formats and presentation styles. TikTok posts often combine multiple narrative elements, such as voiceover narration with text overlays or quick visual cuts, making it necessary to determine a dominant presentation style for annotation.

Another challenge involved interpreting convenience narratives. In many cases, convenience is suggested through visual cues or simplified ingredient lists rather than explicitly stated.

Additionally, engagement metrics were recorded as visible like counts rather than normalized numerical values, since TikTok displays engagement in abbreviated formats such as "30.8k likes."

### **Preliminary Observations**

Several patterns emerged from the dataset.

First, most posts appear as standard videos rather than carousel posts. Of the 60 items in the dataset, 43 are timed videos while 17 are carousel posts.

Second, convenience narratives appear frequently but are not universal. While some videos explicitly frame the meal as quick or easy, many present full cooking processes adapted for a single portion.

Third, creator presentation styles are highly varied. The dataset shows an almost even distribution among hands-only cooking demonstrations, text-based instructions, voiceover narration, and face-on-camera presentation.

Fourth, several recurring food categories appear frequently, including pasta dishes, rice-based meals, and mixed entrée bowls. These types of meals are easily adaptable to single-portion cooking.

Finally, the typical length of timed videos is around 45 seconds, reflecting common short-form video conventions on TikTok.

### **Next Steps: Scaling the Dataset**

After creating this bespoke dataset, the next step would be to expand the dataset to a larger scale of 500–1,000 items.

One possible approach would be automated collection of TikTok posts using hashtag-based scraping or APIs. Relevant hashtags such as "cookingforone," "singleserving," and "dinnerforone" could be used to identify additional videos.

Natural language processing techniques or large language models could then assist with automatically categorizing dish types, detecting convenience narratives, and classifying creator presentation styles.

Scaling the dataset would allow for more robust statistical analysis and the identification of larger cultural patterns in how single-serving cooking is represented on social media.

**AI Usage Declaim:** This documentation uses ChatGPT to help refine languages, but all work including data collection, dataset formulation, comming up with statistical questions and generate findings from result where all done by myself.
