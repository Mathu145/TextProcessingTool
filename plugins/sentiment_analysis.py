class Plugin:
    """
    Analyzes the sentiment of the text.
    """

    def process(self, text):
        positive_words = ["good", "great", "excellent", "happy", "wonderful"]
        negative_words = ["bad", "terrible", "poor", "sad", "horrible"]

        positive_count = sum(word in text.lower() for word in positive_words)
        negative_count = sum(word in text.lower() for word in negative_words)

        if positive_count > negative_count:
            return "Sentiment: Positive"
        elif negative_count > positive_count:
            return "Sentiment: Negative"
        else:
            return "Sentiment: Neutral"
