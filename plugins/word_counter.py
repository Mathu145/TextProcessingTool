import re

class Plugin:
    """
    Counts the number of words in a given text, ignoring punctuation.
    """

    def process(self, text):
        if not text.strip():
            return "The input text is empty. Please provide valid text."

        # Remove punctuation and count words
        cleaned_text = re.sub(r"[^\w\s]", "", text)
        word_count = len(cleaned_text.split())

        # Provide detailed feedback
        return (
            f"Total words counted: {word_count}\n"
            f"Note: Punctuation was ignored during the count."
        )