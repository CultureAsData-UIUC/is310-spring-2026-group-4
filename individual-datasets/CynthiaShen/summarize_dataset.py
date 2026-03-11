import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from statistics import median

DATA_FILE = Path("dataset/single_serving_tiktok_dataset.json")


def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def parse_likes(text):
    """
    Convert values like:
    '3280 likes' -> 3280
    '30.8k likes' -> 30800
    '115k' -> 115000
    """
    text = str(text).strip().lower().replace(" likes", "")
    if text.endswith("k"):
        return float(text[:-1]) * 1000
    return float(text)


def parse_duration(value):
    """
    Convert values like:
    '18s' -> 18
    '1min02s' -> 62
    '31' -> 31
    'Carousel' -> None (handled separately as a post format)
    """
    value = str(value).strip().lower().replace(" ", "")

    if value == "carousel":
        return None

    if value.isdigit():
        return int(value)

    sec_match = re.fullmatch(r"(\d+)s", value)
    if sec_match:
        return int(sec_match.group(1))

    min_sec_match = re.fullmatch(r"(\d+)min(\d+)s", value)
    if min_sec_match:
        minutes = int(min_sec_match.group(1))
        seconds = int(min_sec_match.group(2))
        return minutes * 60 + seconds

    min_only_match = re.fullmatch(r"(\d+)min", value)
    if min_only_match:
        return int(min_only_match.group(1)) * 60

    return None


def normalize_presentation(value):
    value = str(value).strip().lower()
    if value in {"face_on_camera", "faces_on_camera"}:
        return "face_on_camera"
    if value in {"hands_only", "voiceover", "text_only"}:
        return value
    return value


def normalize_convenience(value):
    value = str(value).strip().lower()
    if value in {"explicit", "implicit", "none"}:
        return value

    # keep your intended category if it got embedded in a longer hand-entered string
    for label in ["explicit", "implicit", "none"]:
        if label in value:
            return label
    return value


def classify_dish(dish_text):
    """
    Broad categories for interpretive summary.
    Keeps raw dish_type intact in the dataset; this is only for summary.
    """
    t = str(dish_text).lower()

    if any(k in t for k in [
        "pasta", "spaghetti", "mac", "lasagn", "noodle", "ramen",
        "pomodoro", "goulash", "goodles"
    ]):
        return "pasta_noodles"

    if any(k in t for k in [
        "rice", "sushi", "enchilada", "fajita", "shawarma",
        "dumpling bake", "kfc bowl", "taco bowl", "hot pot"
    ]):
        return "rice_bowl_mixed_entree"

    if any(k in t for k in [
        "soup", "stew", "curry", "roast"
    ]):
        return "soup_stew_curry"

    if any(k in t for k in [
        "cookie", "cake", "brownie", "cinnamon bun", "tres leches",
        "pudding", "streusel"
    ]):
        return "dessert_sweets"

    if any(k in t for k in [
        "egg", "frittata", "breakfast"
    ]):
        return "egg_breakfast"

    if "salad" in t:
        return "salad"

    if any(k in t for k in [
        "sandwich", "burger", "grilled cheese", "sando"
    ]):
        return "sandwich_burger"

    if any(k in t for k in [
        "potato", "fries"
    ]):
        return "potatoes_sides"

    if any(k in t for k in [
        "chicken", "salmon", "steak", "beef", "pork"
    ]):
        return "protein_centered_entree"

    return "other"


def median_safe(values):
    return round(median(values), 1) if values else None


def mean_safe(values):
    return round(sum(values) / len(values), 1) if values else None


def print_counter(title, counter, limit=None):
    print(f"\n{title}")
    print("-" * len(title))
    items = counter.most_common(limit) if limit else counter.most_common()
    for key, count in items:
        print(f"{key}: {count}")


def main():
    data = load_data()

    total_records = len(data)

    raw_dish_counter = Counter()
    broad_dish_counter = Counter()
    convenience_counter = Counter()
    presentation_counter = Counter()
    creator_counter = Counter()
    format_counter = Counter()

    timed_lengths = []
    timed_likes = []
    carousel_likes = []

    likes_by_convenience = defaultdict(list)
    likes_by_presentation = defaultdict(list)
    likes_by_format = defaultdict(list)

    for item in data:
        raw_dish = item["dish_type"]
        convenience = normalize_convenience(item["convenience_emphasis"])
        presentation = normalize_presentation(item["creator_presentation"])
        likes = parse_likes(item["impact_level"])
        duration_seconds = parse_duration(item["video_length_seconds"])

        raw_dish_counter[raw_dish] += 1
        broad_dish_counter[classify_dish(raw_dish)] += 1
        convenience_counter[convenience] += 1
        presentation_counter[presentation] += 1
        creator_counter[item["creator_handle"]] += 1

        if str(item["video_length_seconds"]).strip().lower() == "carousel":
            post_format = "carousel"
            carousel_likes.append(likes)
        else:
            post_format = "timed_video"
            if duration_seconds is not None:
                timed_lengths.append(duration_seconds)
                timed_likes.append(likes)

        format_counter[post_format] += 1
        likes_by_convenience[convenience].append(likes)
        likes_by_presentation[presentation].append(likes)
        likes_by_format[post_format].append(likes)

    print("\nDATASET SUMMARY")
    print("===============")
    print(f"Total records: {total_records}")

    print_counter("Post Format Distribution", format_counter)
    print_counter("Convenience Emphasis Distribution", convenience_counter)
    print_counter("Creator Presentation Distribution", presentation_counter)
    print_counter("Broad Dish Category Distribution", broad_dish_counter)
    print_counter("Top 10 Raw Dish Labels", raw_dish_counter, limit=10)
    print_counter("Creators Appearing More Than Once",
                  Counter({k: v for k, v in creator_counter.items() if v > 1}))

    print("\nTimed Video Length Summary (excluding Carousel)")
    print("-----------------------------------------------")
    if timed_lengths:
        print(f"Count of timed videos: {len(timed_lengths)}")
        print(f"Average length: {mean_safe(timed_lengths)} seconds")
        print(f"Median length: {median_safe(timed_lengths)} seconds")
        print(f"Shortest: {min(timed_lengths)} seconds")
        print(f"Longest: {max(timed_lengths)} seconds")
    else:
        print("No timed videos found.")

    print("\nMedian Likes by Convenience Emphasis")
    print("------------------------------------")
    for key, values in likes_by_convenience.items():
        print(f"{key}: {median_safe(values)}")

    print("\nMedian Likes by Creator Presentation")
    print("------------------------------------")
    for key, values in likes_by_presentation.items():
        print(f"{key}: {median_safe(values)}")

    print("\nMedian Likes by Post Format")
    print("---------------------------")
    for key, values in likes_by_format.items():
        print(f"{key}: {median_safe(values)}")

    print("\nNotes for Interpretation")
    print("------------------------")
    print("- Likes are treated as the visible quantitative engagement signal.")
    print("- Carousel is treated as a distinct post format, not as missing duration.")
    print("- Dish categories are rule-based summary labels built from your raw dish descriptions.")
    print("- Raw dish labels remain available in the original dataset for close reading.")


if __name__ == "__main__":
    main()
