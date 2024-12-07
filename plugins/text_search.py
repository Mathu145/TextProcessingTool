class Plugin:
    def process(self, text):
        keyword = input("Enter a keyword to search: ")
        occurrences = text.lower().count(keyword.lower())
        return f"The keyword '{keyword}' appears {occurrences} times."
