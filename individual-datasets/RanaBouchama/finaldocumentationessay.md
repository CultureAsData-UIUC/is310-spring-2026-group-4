## Project Overview ##

What makes or breaks a popular FoodTok (TikTok community/genre dedicated to making videos about food) video? Are you more likely to get more views with a certain type of hook, caption, or hashtags? What about the music you use? Does an original sound or using a trendy audio mean you are more likely to be seen? That is the central thesis question for this project, analyzing [a pre-existing FoodTok dataset](https://www.adworkly.co/resources) while adding in my own manually collected dataset.

### Dataset information ###
* For the manually selected videos:
  * Videos in the FYP of a completely fresh, never-before-used account. 
  * This is to simulate what a new user would be seeing after demonstrating interest in food-related content, what is naturally pushed by the algorithm, and, in turn, what is deemed "popular."
  * Data included: post metadata
    * Username, video URL, views, likes, shares, comments, favorites, the hook (text within the video), as well as the caption and hashtags, music, whether a user's face was in the video or not, video language and format type.
  * My only criteria for what videos could be added were:
  * A) That it was about food in some way
  * B) That it surpassed 100K likes, this is a rather low bar, but this was my "minimum" for a video to be considered "viral."
  * 36 Videos in total
* For the pre-existing dataset:
  * Data included: post metadata
    * Username, video URL, views, likes, shares, comments, favorites, the hook (text within the video), as well as the caption and hashtags, music, whether a user's face was in the video or not, video language, and format type.
  * The dataset originally had 5,000 entries
    * A bigger dataset does make for a more in-depth analysis; however, that much data is equally as difficult to make sense of, and with more and more entries, the entries almost collapse in on themselves, and it's harder to consider individuals
  * I've cut that data down to 450 entries
  * I've also removed categories I deemed unrelated to my central question and thus superfluous information that served only to make the dataset less understandable 
    * Date the video was posted, this does have some important cultural context lost; the time a video is posted has a factor in who sees it/when, and thus can contribute to popularity. However, they were all posted around the same 2020-2024 range, and I am more concerned with what the author and viewers have control over that helps boost a video in the algorithm
    * Total videos posted, once again, there is a cultural context lost. Posting consistently also helps boost you in the algorithm; however, I am more concerned with popularity on a video-by-video basis
    * Outlier rate, I am uncertain how they collected this data and what it is based on; it would only serve to make it more confusing for the average viewer. I'd like my dataset to be as accessible and understandable as possible.
  * I also added a separate column for hashtags, as I believe it should be separated from the caption text to make it easier for computation purposes, as well as to make the hashtags more visible to others.
  * Finally, I changed the names of certain categories to make them more understandable (bookmarks became favorites because that is how they are referred to in the app, title became caption because the average person would not recognize "title" as referring to the video's caption, etc.)

### Computational Tools ###
* Originally, I intended to use PyTok to scrape for a dataset of my own; unfortunately, this was not possible, as I kept getting errors and decided to stop so as not to risk getting IP banned.
* Although not properly documented, the AdWorkly dataset used was likely made using the official marketing API or PyTok itself.
* Google Sheets also has built-in computational tools, namely, there are count formulas to count the occurrences of words, which is what I used to count the frequency of the hashtags.
  * This majorly streamlined the process, especially as everything else was done manually.

### Challenges ###
* As I previously went over, this being done almost entirely manually proved to be a bit of a challenge; unfortunately, I am completely inept at coding, especially when left to my own devices without an assignment's framework to guide me.
* Furthermore, PyTok deciding to just not work for me put quite the monkey wrench in my plans. Thankfully, I found the AdWorkly dataset to audit.
* The counting on Google Sheets isn't perfect, for instance, "brownnies" and "brownies)" are counted separately because it counts the parentheses as part of the phrase
* Removing the hashtags from the caption proved to be a little confusing when the caption didn't make sense without it (for instance, say the caption was "#fun day out" or when the caption was just hashtags or when the hashtag was placed as important context for the caption: "#ad", for example)
  * Ultimately, I decided to leave these special cases in. I think there is a difference between tags used for visibility and those that are naturally integrated into the caption, or if there was no caption its important to note that it was just hashtags. Ultimately, this makes it so that people unfamiliar with the dataset are still able to navigate it. Even if it makes the final count of words a bit messier than I'd have hoped.

### Trends, Take-Aways, Essay(ish) ###
* Surface Level Trends:
  * At 34 mentions, "chicken" is the most used word in hooks, does this mean you are more likely to go viral if you incorporate the word "chicken" in your caption? Possibly, it at least seems people are more likely to hear you out and get "hooked" if you incorporate tbe word chickensomewhere
  * "Chicken" is also in the top 20 words used in captions, sitting at a nice and pretty 163 mentions
    * Words also used frequently in captions include those associated with measurements (tsp, tbsp, cup etc) all in the top 20
  * In the theme of recipes, #easyrecipe was the most used hashtag at 62 uses after #fyp, with #recip at third with 57. 
  * The most popular language was english with 438 videos in english
    * All other languages pale in comparison, Russian in second only has 15
  * And finally, videos were more commonly faceless (386) as opposed to recorded with face (98)
* What does this say about FoodTok, popularity on FoodTok and the average FoodTok viewer?
  * Reveals that English speakers are incredibly over-represented, I don't doubt that there is a sizable communities of FoodTok users that don't speak English but they don't seem to be equal under tbe eyes of the algorithm. Very few actually made it into the dataset
    * There is, however, an alternative explanation for this: namely that TikTok factors in location data in its algorithm. It's entirely possible that because I am in America, it assumes I would only be interested in content in English and thus filters my reccomendations accordingly. Similarly, Adworkly is based in America (specifically in Wyoming) and thus even through web scraping would only be recommended videos in English
      * On one hand, this makes sense, reccomending Americans videos in Russian, for example, wouldn't make much money because the majority of Americans don't speak Russian and the video would be entirely inaccessible to them thus limiting their interactions on the site. On the other, it does create a bit of a filter bubble and limits cultural exchange which is the whole point of social media. That is all without considering how neo-colonialism and globalism reinforces American supremacy with this being yet another axis of that oppression. It would be no surprise to me if even internationally a sizable chunk of videos were still in English.
      * On a partially related note, I did make some corrections on the AdWorkly dataset incorrectly labeling some videos as "english" when they weren't. I'm unsure how this happened as I don't have access to the code but if I had to assume it may have been based on the audio playing instead of the caption or subtitles (if the video had subtitles). Again, this reinforces the heavy English bias TikTok has, international users are more likely to use audios in English rather their native languages.
  * Switching gears, I know this is more Soham's area of expertise with his dataset so as to not step on any toes I'll keep this brief, but the focus on chicken is particularly stand-out to me. I'm unsure 
