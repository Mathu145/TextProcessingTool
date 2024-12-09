class Plugin:
    """
    Searches for a specific keyword in the text and highlights occurrences.
    """
    def process(self, text):
        keyword = input("Enter the keyword to search: ").strip()
        if not keyword:
            return "No keyword entered. Please try again."

        # Highlight all occurrences of the keyword
        if keyword in text:
            highlighted_text = text.replace(keyword, f"[{keyword}]")
            return highlighted_text
        else:
            return f"Keyword '{keyword}' not found in the text."