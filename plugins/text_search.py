class Plugin:
    """
    Searches for a keyword in the text and highlights occurrences.
    """

    def process(self, text):
        keyword = input("Enter the keyword to search for: ")
        highlighted_text = text.replace(keyword, f"[{keyword}]")
        return highlighted_text
