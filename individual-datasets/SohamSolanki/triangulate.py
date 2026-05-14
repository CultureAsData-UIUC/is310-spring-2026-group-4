"""
Three-way methodological triangulation.

Joins the manual labels, LLM classifications, and regex/keyword
classifications by id, then reports:
  - pairwise agreement rates
  - three-way agreement
  - per-row disagreement breakdown
  - moral language pattern frequencies (from the regex pass)

Writes a combined triangulation CSV and prints a summary.
"""

import csv
from collections import Counter
from pathlib import Path


def load_csv(path: Path) -> list[dict]:
    with path.open("r", newline="") as f:
        return list(csv.DictReader(f))


def main():
    base = Path("/mnt/user-data/uploads/FINAL_tiktok_protein_dataset.csv")
    llm  = Path("/mnt/user-data/outputs/tiktok_protein_LLM_classifications_only.csv")
    rex  = Path("/mnt/user-data/outputs/tiktok_protein_regex_classifications.csv")
    out  = Path("/mnt/user-data/outputs/tiktok_protein_triangulation.csv")

    base_rows = {r["id"]: r for r in load_csv(base)}
    llm_rows  = {r["id"]: r for r in load_csv(llm)}
    rex_rows  = {r["id"]: r for r in load_csv(rex)}

    # Join
    combined = []
    for vid, base_r in base_rows.items():
        l = llm_rows[vid]
        x = rex_rows[vid]
        combined.append({
            "id": vid,
            "caption_snippet": (base_r["caption"] or "")[:80],
            "manual_category": base_r["cultural_theme"],
            "llm_category": l["llm_category"],
            "regex_category": x["regex_category"],
            "manual_vs_llm":   l["llm_category"]   == base_r["cultural_theme"],
            "manual_vs_regex": x["regex_category"] == base_r["cultural_theme"],
            "llm_vs_regex":    l["llm_category"]   == x["regex_category"],
            "all_three_agree": (l["llm_category"] == base_r["cultural_theme"]
                                and x["regex_category"] == base_r["cultural_theme"]),
            "llm_position": l["llm_position"],
            "llm_function": l["llm_function"],
            "llm_genre": l["llm_genre"],
            "regex_protein_grams_max": x["regex_protein_grams_max"],
            "regex_speed_marker_count": x["regex_speed_marker_count"],
            "regex_guilt_free": x["regex_guilt_free"],
            "regex_fuel_language": x["regex_fuel_language"],
            "regex_ad_markers": x["regex_ad_markers"],
        })

    # Write triangulation CSV
    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(combined[0].keys()),
                                quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        # Convert booleans to yes/no for human reading
        for row in combined:
            row = {k: ("yes" if v is True else "no" if v is False else v)
                   for k, v in row.items()}
            writer.writerow(row)

    # --- Summary stats ---
    n = len(combined)
    print(f"\n{'='*60}\nTHREE-WAY TRIANGULATION (n={n})\n{'='*60}")

    pairwise = {
        "Manual vs LLM":   sum(1 for r in combined if r["manual_vs_llm"]),
        "Manual vs Regex": sum(1 for r in combined if r["manual_vs_regex"]),
        "LLM vs Regex":    sum(1 for r in combined if r["llm_vs_regex"]),
    }
    print("\nPairwise agreement:")
    for k, v in pairwise.items():
        print(f"  {k:20s}  {v:>3}/{n}  ({v/n*100:.1f}%)")

    all3 = sum(1 for r in combined if r["all_three_agree"])
    print(f"\nAll three agree:   {all3}/{n}  ({all3/n*100:.1f}%)")

    none_agree = sum(1 for r in combined
                     if not r["manual_vs_llm"]
                     and not r["manual_vs_regex"]
                     and not r["llm_vs_regex"])
    print(f"None agree:        {none_agree}/{n}  ({none_agree/n*100:.1f}%)")

    # Where regex says "High Protein (General)" — the fallback bucket
    fallback = [r for r in combined if r["regex_category"] == "High Protein (General)"]
    print(f"\nRegex falls back to 'High Protein (General)':  "
          f"{len(fallback)}/{n}  ({len(fallback)/n*100:.1f}%)")
    print("  (Manual put these into:)")
    print("  ", Counter(r["manual_category"] for r in fallback))

    # Disagreement table
    print(f"\n{'='*60}\nROW-BY-ROW DISAGREEMENTS\n{'='*60}")
    print(f"\n{'id':<28}  {'manual':<32}  {'llm':<32}  regex")
    print("-" * 130)
    for r in combined:
        if r["all_three_agree"]:
            continue
        print(f"{r['id']:<28}  {r['manual_category']:<32}  "
              f"{r['llm_category']:<32}  {r['regex_category']}")

    # --- Moral language frequencies ---
    print(f"\n{'='*60}\nMORAL LANGUAGE PATTERNS (regex pass)\n{'='*60}")
    # NOTE: values come from regex CSV as the literal strings "yes"/"no",
    # both of which are truthy in Python. Compare to "yes" explicitly.
    guilt = sum(1 for r in combined if r["regex_guilt_free"] == "yes")
    fuel  = sum(1 for r in combined if r["regex_fuel_language"] == "yes")
    ad    = sum(1 for r in combined if r["regex_ad_markers"] == "yes")
    has_grams = sum(1 for r in combined if r["regex_protein_grams_max"])
    avg_speed = sum(int(r["regex_speed_marker_count"]) for r in combined) / n

    print(f"  Quantification (mentions protein grams):  "
          f"{has_grams}/{n} ({has_grams/n*100:.1f}%)")
    print(f"  Guilt-free framing:                       "
          f"{guilt}/{n} ({guilt/n*100:.1f}%)")
    print(f"  Fuel / optimization language:             "
          f"{fuel}/{n} ({fuel/n*100:.1f}%)")
    print(f"  Ad / brand markers:                       "
          f"{ad}/{n} ({ad/n*100:.1f}%)")
    print(f"  Average speed-marker count per caption:   {avg_speed:.2f}")

    # Cross-tab: do regex flags align with LLM tone?
    print(f"\nLLM-tone × regex_ad_markers cross-tab:")
    ct = Counter()
    for r in combined:
        ct[(r["regex_ad_markers"], r.get("llm_function", "?"))] += 1
    # Simpler: how often does regex_ad_markers=yes align with llm_tone=promotional?
    ad_promo_agree = 0
    promo_total = 0
    ad_total = 0
    for r in combined:
        llm_row = llm_rows[r["id"]]
        tone = llm_row["llm_tone"]
        if r["regex_ad_markers"] == "yes":
            ad_total += 1
            if tone == "promotional":
                ad_promo_agree += 1
        if tone == "promotional":
            promo_total += 1
    print(f"  Of {ad_total} videos with regex ad markers, "
          f"{ad_promo_agree} were tagged promotional by LLM "
          f"({ad_promo_agree/ad_total*100:.0f}% if ad_total else 0)")
    print(f"  Of {promo_total} LLM-tagged promotional videos, "
          f"{ad_promo_agree} were also flagged by regex "
          f"({ad_promo_agree/promo_total*100:.0f}%)")

    print(f"\nWrote {n} rows to:\n  {out}")


if __name__ == "__main__":
    main()
