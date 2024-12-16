import re

class Plugin:
    """
    Analyzes the sentiment of the text and classifies it as positive, negative, or neutral.
    Includes total word count and lists the positive and negative words found in the text.
    """
    def process(self, text):
        if not text.strip():
            return "The input text is empty. Please provide valid text."

        # Count total words using the same logic as Word Counter plugin
        cleaned_text = re.sub(r"[^\w\s]", "", text)
        words = cleaned_text.split()
        total_word_count = len(words)

        # Define sets of positive and negative words
        positive_words_set = {"good", "happy", "excellent", "positive", "great"}
        negative_words_set = {"bad", "sad", "terrible", "negative", "poor"}

        # Identify positive and negative words in the text
        positive_words_found = [word for word in words if word.lower() in positive_words_set]
        negative_words_found = [word for word in words if word.lower() in negative_words_set]

        # Count occurrences of positive and negative words
        positive_count = len(positive_words_found)
        negative_count = len(negative_words_found)

        # Determine sentiment based on counts
        if positive_count > negative_count:
            sentiment = "positive"
        elif negative_count > positive_count:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        # Return the sentiment analysis result
        return (
            f"Total words: {total_word_count}\n"
            f"The sentiment of the text is {sentiment}.\n"
            f"Positive words: {positive_count} ({', '.join(positive_words_found) if positive_words_found else 'None'})\n"
            f"Negative words: {negative_count} ({', '.join(negative_words_found) if negative_words_found else 'None'})"
        )

