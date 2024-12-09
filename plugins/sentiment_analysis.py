import re

class Plugin:
    """
    Analyzes the sentiment of the text and classifies it as positive, negative, or neutral.
    """

    def process(self, text):
        if not text.strip():
            return "The input text is empty. Please provide valid text."

        # Predefined positive and negative word sets
        positive_words = {"good", "happy", "excellent", "positive", "great"}
        negative_words = {"bad", "sad", "terrible", "negative", "poor"}

        # Remove punctuation and split text into words
        words = re.findall(r'\b\w+\b', text.lower())

        # Count occurrences of positive and negative words
        positive_count = sum(word in positive_words for word in words)
        negative_count = sum(word in negative_words for word in words)

        # Determine sentiment
        if positive_count > negative_count:
            sentiment = "positive"
        elif negative_count > positive_count:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        # Return detailed sentiment analysis
        return (
            f"The sentiment of the text is classified as '{sentiment}'.\n"
            f"Positive words: {positive_count}, Negative words: {negative_count}.\n"
            f"Words analyzed: {len(words)}."
        )