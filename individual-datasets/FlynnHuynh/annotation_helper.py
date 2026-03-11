#imports
import os
import json
import time
import google.generativeai as genai

# Free tier: ~15 req/min, ~1500 req/day. Wait between requests to stay under limit.
MIN_DELAY_BETWEEN_REQUESTS_SEC = 60
MAX_RETRIES_ON_RATE_LIMIT = 2
RETRY_WAIT_SEC = 60

#system prompt
SYSTEM_PROMPT = """You are a cultural food studies research assistant helping to annotate 
sources about immigrant-origin dishes that have been transformed in American contexts.

For each source text provided, return ONLY a JSON object with these exact keys and 
allowed values:

{
  "origin_story_mentioned": "Yes" | "No" | "Partial",
  "origin_story_framing": "omitted" | "simplified" | "mythologized" | "detailed_historical" | "corrective" | "contested",
  "authenticity_framing": "claimed" | "distanced" | "dismissed" | "contested" | "reclaimed" | "not_mentioned",
  "community_credit_given": "Yes" | "No" | "Partial" | "N/A",
  "annotation_notes": "<1-2 sentence explanation of your coding choices>"
}

Definitions for coding:

origin_story_mentioned:
- Yes: The source explicitly discusses the dish's cultural or historical origin
- No: No mention of origin at all
- Partial: Vague or passing mention without depth

origin_story_framing (only if mentioned):
- omitted: Not discussed
- simplified: Brief, surface-level mention
- mythologized: Romantic or uncritical narrative that flattens complexity
- detailed_historical: Engages with immigration history, transformation process, named actors
- corrective: Actively corrects a common misconception about origin
- contested: Acknowledges that multiple or disputed origin claims exist

authenticity_framing:
- claimed: Source asserts the dish is authentic (to a culture or tradition)
- distanced: Source acknowledges it is not authentic but presents it positively
- dismissed: Source actively argues authenticity does not matter
- contested: Source acknowledges ongoing debate about authenticity
- reclaimed: A community member claims the dish as their own valid tradition
- not_mentioned: Authenticity is not referenced

community_credit_given:
- Yes: The immigrant community that created/adapted the dish is named and credited
- No: No credit given; dish treated as cultureless or mainstream
- Partial: Community mentioned but without substantive acknowledgment
- N/A: Not applicable (e.g., pure reference entry)

Return ONLY valid JSON. No preamble, no markdown formatting."""

#functions
#get api key
def get_api_key():
    key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
    if not key:
        key = input("Enter your Google/Gemini API key: ").strip()
    return key


#annotate source
def annotate_source(model: genai.GenerativeModel, source_text: str, dish_info: str):
    user_message = f"""Dish context: {dish_info}

Source text to annotate:
\"\"\"
{source_text}
\"\"\"

Return the JSON annotation for this source."""

    response = model.generate_content(
        user_message,
        generation_config={"max_output_tokens": 500},
    )

    raw = response.text.strip()
    # Strip markdown code fences if present
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()

    return json.loads(raw)

# wait for rate limit
def wait_for_rate_limit(last_request_time: float):
    elapsed = time.monotonic() - last_request_time
    if elapsed < MIN_DELAY_BETWEEN_REQUESTS_SEC:
        wait = MIN_DELAY_BETWEEN_REQUESTS_SEC - elapsed
        print(f"Free-tier rate limit: waiting {wait:.0f}s before next request...")
        time.sleep(wait)


#main function
def main():
    print("=" * 60)
    print("Immigrant Dish Dataset — Annotation Helper")
    print("Uses Gemini API (free tier) to assist qualitative coding")
    print("=" * 60)
    print(f"Rate limit: 1 request every {MIN_DELAY_BETWEEN_REQUESTS_SEC}s to avoid quota errors.")
    print("=" * 60)

    api_key = get_api_key()
    genai.configure(api_key=api_key)
    # Free-tier models: gemini-2.0-flash, gemini-2.5-flash, or gemini-pro
    model = genai.GenerativeModel(
        "gemini-2.5-flash",
        system_instruction=SYSTEM_PROMPT,
    )

    last_request_time = 0.0

    while True:
        print("\n--- New Annotation ---")
        dish_info = input(
            "Dish context (e.g., 'Orange Chicken, Chinese-American, Pure American Invention'): "
        ).strip()
        if not dish_info:
            print("No dish info provided. Exiting.")
            break

        print("Paste the source text below. Enter a blank line followed by 'END' to finish:")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == "END":
                break
            lines.append(line)
        source_text = "\n".join(lines).strip()

        if not source_text:
            print("No source text provided. Skipping.")
            continue

        wait_for_rate_limit(last_request_time)
        print("\nAnnotating with Gemini API...")
        last_request_time = time.monotonic()

        last_error = None
        for attempt in range(MAX_RETRIES_ON_RATE_LIMIT + 1):
            try:
                annotation = annotate_source(model, source_text, dish_info)
                print("\n--- Annotation Result ---")
                print(json.dumps(annotation, indent=2))
                print("\nCopy the values above into your dataset CSV.")
                last_error = None
                break
            except json.JSONDecodeError as e:
                print(f"Error parsing Gemini response as JSON: {e}")
                break
            except Exception as e:
                last_error = e
                err_str = str(e)
                if "429" in err_str or "quota" in err_str.lower() or "rate" in err_str.lower():
                    if attempt < MAX_RETRIES_ON_RATE_LIMIT:
                        print(f"Rate limit hit. Waiting {RETRY_WAIT_SEC}s before retry...")
                        time.sleep(RETRY_WAIT_SEC)
                        last_request_time = time.monotonic()
                    else:
                        print(f"Gemini API error (rate limit): {e}")
                        print("Tip: Wait a few minutes or check https://ai.dev/rate-limit for usage.")
                else:
                    print(f"Gemini API error: {e}")
                    break
        if last_error and "429" in str(last_error):
            print("Skipping this source. You can run the script again later.")
        again = input("\nAnnotate another source? (y/n): ").strip().lower()
        if again != "y":
            print("Done. Exiting annotation helper.")
            break


if __name__ == "__main__":
    main()