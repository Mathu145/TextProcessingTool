class Plugin:
    """
    Counts the number of words in the given text.
    """
    def process(self, text):
        words = text.split()
        return f"Word count: {len(words)}"
