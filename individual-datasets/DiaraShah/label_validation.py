import pandas as pd
import os

# defining computational dictionary - how the computer "thinks"
keywords = {
    'money': ['cheap', 'broke', 'budget', 'frugal', 'price', 'affordable', 'save', 'cost', '£'],
    'time': ['quick', 'fast', 'minute', 'busy', 'ready', 'prep', 'efficient', 'routine', 'week'],
    'energy': ['tired', 'lazy', 'low effort', 'depressed', 'spoon', 'mental health', 'exhausted'],
    'space': ['dorm', 'microwave', 'mini fridge', 'no kitchen', 'kitchenless', 'fire alarm']
}

def auto_label(text):
    """Assigns a category based on keyword matching."""
    text = str(text).lower()
    for category, terms in keywords.items(): 
        if any(term in text for term in terms):
            return category
    return "unknown"

#loadng dataset
file_path = 'constraint_food_dataset_final.csv'

if not os.path.exists(file_path):
    print(f"Error: {file_path} not found. Make sure the CSV is in the same folder.")
else:
    df = pd.read_csv(file_path)

    # comp_label generation- putting this to the 'notes' column as a proxy for the computer "reading" the post
    df['comp_label'] = df['notes'].apply(auto_label)

    # compare human vs computer-  creates a column that literally flags where the computer was wrong
    df['label_match'] = df.apply(lambda x: True if str(x['constraint_type']).strip().lower() == str(x['comp_label']).strip().lower() else False, axis=1)

    output_file = 'constraint_food_final_audited.csv'
    df.to_csv(output_file, index=False)

    total = len(df)
    matches = df['label_match'].sum()
    accuracy = (matches / total) * 100

    print("--- COMPUTATIONAL AUDIT REPORT ---")
    print(f"Total Items Processed: {total}")
    print(f"Successful Matches: {matches}")
    print(f"Computer Accuracy: {accuracy:.2f}%")
    print(f"File saved as: {output_file}")


    #reddit or tikok better
    platform_accuracy = df.groupby('platform')['label_match'].mean() * 100

    print("\n--- Accuracy by Platform ---")
    print(platform_accuracy)

    # scaling by the age(compared to 2026)
    df['post_age'] = 2026 - df['approx_date']
    
    df.to_csv(output_file, index=False)

    mistakes = df[df['label_match'] == False]
    mistakes.to_csv('my_audit_mistakes.csv', index=False)

    print(f"\nExtra Analysis Done!")
    print(f"Check 'my_audit_mistakes.csv' to see where the computer failed.")

    #teying to show which of my search terms actually gave me the most "accurate" data
    query_results = df.groupby('search_query')['label_match'].mean() * 100
    
    print("\n--- Search Query Effectiveness ---")
    print(query_results.sort_values(ascending=False))
    query_results.to_csv('search_strategy_audit.csv')