import re
import requests
from collections import Counter

def CommonWordsUsedController(text):
  try:
    # Get the list of common words
    response = requests.get("https://gist.githubusercontent.com/deekayen/4148741/raw/98d35708fa344717d8eee15d11987de6c8e26d7d/1-1000.txt")
    common_words = response.text.splitlines()[:100]

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
