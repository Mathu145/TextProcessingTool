class Plugin:
    """
    Searches for a keyword in the text and counts its occurrences.
    """
    def process(self, text):
        keyword = input("Enter a keyword to search: ")
        occurrences = text.lower().count(keyword.lower())
        return f"The keyword '{keyword}' appears {occurrences} times."
