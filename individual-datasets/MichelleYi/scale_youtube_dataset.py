from googleapiclient.discovery import build
import pandas as pd
import re
from datetime import datetime
import time

API_KEY = "AIzaSyD9Kzjphae2wKqT41YJbqD3LcMwAfgFg_U"

youtube = build("youtube", "v3", developerKey=API_KEY)

CHANNEL_IDS = {
    "ErikTheElectric": "UC6huXz0F6-7KA7-mW0jdejA",
    "Matt Stonie": "UCd1fLoVFooPeWqCEYVUJZqg",
    "Nikocado Avocado": "UCDwzLWgGft47xQ30u-vjsrg",
}

KEYWORDS = [
    "challenge", "calorie", "calories", "mukbang", "eating",
    "food", "giant", "massive", "biggest", "menu", "spicy",
    "noodle", "ramen", "burger", "pizza", "chicken", "kfc",
    "donut", "burrito", "taco"
]

def get_uploads_playlist_id(channel_id):
    response = youtube.channels().list(
        part="contentDetails",
        id=channel_id
    ).execute()
    return response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

def get_all_video_ids(playlist_id):
    ids = []
    page_token = None

    while True:
        response = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=page_token
        ).execute()

        for item in response.get("items", []):
            ids.append(item["contentDetails"]["videoId"])

        page_token = response.get("nextPageToken")
        if not page_token:
            break

        time.sleep(0.1)

    return ids

def keep_video(title, description):
    text = f"{title} {description}".lower()
    return any(k in text for k in KEYWORDS)

def classify_food_type(title):
    t = title.lower()

    if "burger" in t:
        return "burger"
    if "pizza" in t:
        return "pizza"
    if "ramen" in t or "noodle" in t:
        return "ramen/noodles"
    if "chicken" in t or "kfc" in t:
        return "fried chicken"
    if "donut" in t or "cake" in t or "dessert" in t:
        return "dessert/sweets"
    if "taco" in t or "burrito" in t:
        return "taco/burrito"
    if "seafood" in t or "crab" in t or "lobster" in t:
        return "seafood"
    if "menu" in t or "everything" in t:
        return "fast food/mixed"
    return "mixed/unknown"

def classify_portion_size(title, calorie_claim):
    t = title.lower()

    if calorie_claim:
        if calorie_claim >= 10000:
            return "super extreme"
        if calorie_claim >= 4000:
            return "extreme"
        if calorie_claim >= 1500:
            return "large"
        return "moderate"

    if any(word in t for word in ["world record", "entire menu", "everything", "biggest", "massive", "giant"]):
        return "super extreme"
    if any(word in t for word in ["challenge", "mukbang", "10,000", "10000", "calorie"]):
        return "extreme"
    if any(word in t for word in ["spicy", "noodle", "burger", "pizza", "chicken"]):
        return "large"

    return "unknown"

def extract_calorie_claim(text):
    text = text.lower()
    match = re.search(r"(\d{1,3}(?:,\d{3})+|\d{4,6})\s*(?:calorie|calories|cals|kcal)", text)
    if match:
        return int(match.group(1).replace(",", ""))
    return ""

def extract_food_quantity(text):
    text = text.lower()

    patterns = [
        r"\d+\s*(?:lb|lbs|pounds|pound)\b[^,.!?\n]*",
        r"\d+\s*(?:oz|ounces)\b[^,.!?\n]*",
        r"\d+\s*(?:pieces|piece|pc|pcs)\b[^,.!?\n]*",
        r"\d+\s*(?:burgers|pizzas|donuts|wings|nuggets|tacos|burritos|sandwiches|pancakes)\b[^,.!?\n]*",
        r"\d+\s*(?:calorie|calories|cals|kcal)\b[^,.!?\n]*",
    ]

    found = []
    for pattern in patterns:
        found.extend(re.findall(pattern, text))

    return "; ".join(found[:5])

def assign_period(published_at):
    year = datetime.fromisoformat(published_at.replace("Z", "+00:00")).year

    if year <= 2017:
        return "early"
    if year <= 2021:
        return "mid"
    return "recent"

def get_video_details(video_ids, creator):
    rows = []

    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i+50]

        response = youtube.videos().list(
            part="snippet,statistics",
            id=",".join(batch)
        ).execute()

        for item in response.get("items", []):
            snippet = item.get("snippet", {})
            stats = item.get("statistics", {})

            title = snippet.get("title", "")
            description = snippet.get("description", "")
            published_at = snippet.get("publishedAt", "")

            if not keep_video(title, description):
                continue

            full_text = f"{title} {description}"
            calories = extract_calorie_claim(full_text)

            rows.append({
                "creator": creator,
                "video_title": title,
                "link": f"https://www.youtube.com/watch?v={item.get('id')}",
                "upload_date": published_at[:10],
                "period": assign_period(published_at),
                "food_type": classify_food_type(title),
                "portion_size": classify_portion_size(title, calories if calories != "" else None),
                "views": stats.get("viewCount", ""),
                "likes": stats.get("likeCount", ""),
                "comments": stats.get("commentCount", ""),
                "food_quantity": extract_food_quantity(full_text),
                "calories": calories
            })

        time.sleep(0.1)

    return rows

all_rows = []

for creator, channel_id in CHANNEL_IDS.items():
    print(f"Collecting {creator}...")
    uploads_playlist_id = get_uploads_playlist_id(channel_id)
    video_ids = get_all_video_ids(uploads_playlist_id)
    rows = get_video_details(video_ids, creator)
    all_rows.extend(rows)

df = pd.DataFrame(all_rows)

df.to_csv("scaled_extreme_eating_dataset.csv", index=False)

print(f"Saved {len(df)} rows to scaled_extreme_eating_dataset.csv")