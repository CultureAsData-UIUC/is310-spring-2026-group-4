## Project Overview ##

This project intends to examine the way in which cuisine is represented online, not just the specific types of cuisine, but also the way in which algorithms are biased against marginalized groups who create this content. This project specifically seeks to analyze short-form video content, specifically TikTok videos about food. This can be the consumption of food (eg. mukbangs), TikToks discussing food, or food recipes.

It is important to note that I lump white-centric cuisines together as "Western" not because this is the default, but to further expose the disparity between the representation of traditionally "white" cuisine, versus cuisine that originates from marginalized communities.

### Dataset information ###
* Made from scratch
* Made manually, wanted to be as impartial as possible, and thus selected videos that landed in my FYP in a completely fresh, never-before-used account. 
  * This is to simulate what a new user would be seeing after demonstrating interest in food-related content, what is naturally pushed by the algorithm, and, in turn, what is deemed "popular."
* I attempted to include as much context about the videos as possible, without including every minute detail
  * Data included: post metadata (likes, favorites, and shares, this is due to these metrics being tied most directly to whether a viewer enjoyed the video and whether they were more or less likely to share with friends), the ethnic identity of the user (if that was discernible based on their profile/face or hands in the video), the origin of the food shown, the top comment (to somewhat preserve context), tags used on the post, as well as the link to the video.
* My only criteria for what videos could be added were:
 * A) That it was about food in some way
 * B) That it surpassed 100K likes, this is a rather low bar, but this was my "minimum" for a video to be considered "viral."
 
### Computational Tools ###
* As previously stated, this dataset was created manually and from scratch. In essence, it was me, a Google spreadsheet, and my TikTok For You Page against the world. Many factors contributed to this choice:
   * Being a coding novice, I still did not fully have a grasp on how to gather my data any other way
   * TikTok's API use is strict; additionally, scraping has the potential to get my account banned. I did not want to take this risk
   * I wanted to simulate what a user would have seen scrolling through the For You Page, instead of specifically scraping specific tags
* In the future, however, I aim to try to take advantage of these tools, not necessarily to scrape the tags. I still do not wish to risk getting banned; however, I would like to see if there are any pre-existing databases that I can audit and add my data to.


### Challenges ###
* Of course, with this dataset being made manually, there was no shortage of challenges: namely, it was a bit time-consuming to compile all this data together. Where I'm sure creating a code to semi-automate the process and collect post metadata would have been much, *much* faster.
* Additionally, I found labeling the food rather challenging
 * There is, naturally, a lot of overlap between cultures. When is a food traditionally "Western" and when is it just something that can be found no matter where you are, like salad, for instance
 * Furthermore, due to globalization, a lot of "Western" foods technically aren't "Western" in origin (Chipotle, for instance, has Mexican influence but originated in the United States; would that be considered Mexican or Western?), and foods that may be "Western" in origin are now in turn found around the globe.
 * I created a "non-specific" category for foods that are not intrinsically tied to one specific culture, but this felt more like a quick "band-aid" solution.
 * Perhaps to mitigate this, I should have looked into only food recipes instead of broadening my range to all kinds of food videos. Perhaps this would also give me a better idea of where the food originated, as this would be part of the post's caption
* Additionally, labeling people's ethnicities based on perception was incredibly challenging and felt incredibly constraining
* 

What cultural materials are you working with and why? What approach did you take (from scratch or auditing)?
What computational tools did you use to assist your work? How did they help? What were their limitations?
What decisions did you make about what to include, exclude, or how to categorize? Why? What challenges did you encounter? How did you address them? What patterns, questions, or tensions emerged from working closely with this data?
