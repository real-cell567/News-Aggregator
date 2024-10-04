categories = {
    'technology': ['tech', 'AI', 'software', 'hardware'],
    'finance': ['stocks', 'cryptocurrency', 'bank', 'money']
}

def categorize_article(title, description):
    # Ensure title and description are strings
    title = title or ""  # Default to an empty string if None
    description = description or ""  # Default to an empty string if None

    for category, keywords in categories.items():
        # Check for keywords in a combined string of title and description
        combined_text = (title + " " + description).lower()
        if any(keyword.lower() in combined_text for keyword in keywords):
            return category
    return 'general'
