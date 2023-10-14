import re
from collections import Counter

def CommonWordsUsedController(text, common_words):
  try:
    # Remove punctuation and convert text to lowercase
    text = re.sub(r'[^\w\s]', '', text.lower())
    
    # Tokenize the text
    words = text.split()

    # Count the frequency of each word
    word_count = Counter(words)

    # Create a new dictionary for common word counts
    common_word_count = {}

    # Loop through the common words
    for word in common_words:
        lowercase_word = word.lower()
        # Check if the word is in the word_count dictionary
        if lowercase_word in word_count:
            # Add the count of the common word to the common_word_count dictionary
            common_word_count[word] = word_count[lowercase_word]

    # common_word_count now contains the counts of common words
    sorted_word_count = dict(sorted(common_word_count.items(), key=lambda item: item[1], reverse=True))
    
    return sorted_word_count
  except Exception as e:
    print(e)
    return {}
