import nltk
from nltk import bigrams
from collections import Counter, defaultdict
import random

# Download required NLTK data
nltk.download('punkt')

# Sample text corpus
text = "This is a sample text corpus. It is used to demonstrate bigram probabilities. This is another sentence in the corpus."

# Tokenize the text
tokens = nltk.word_tokenize(text.lower())

# Create bigrams from the tokens
bigram_list = list(bigrams(tokens))

# Calculate the frequency of each bigram
bigram_freq = Counter(bigram_list)

# Create a dictionary to store the possible next words for each word
next_word_dict = defaultdict(list)

for (w1, w2) in bigram_freq:
    next_word_dict[w1].append((w2, bigram_freq[(w1, w2)]))

# Function to predict the next word given the current word
def predict_next_word(current_word):
    if current_word in next_word_dict:
        # Get the list of possible next words and their frequencies
        next_words = next_word_dict[current_word]
        # Sort the next words based on their frequency
        next_words = sorted(next_words, key=lambda x: x[1], reverse=True)
        # Return the word with the highest frequency
        return next_words[0][0]
    else:
        return None

# Test the next word prediction
test_words = ["this", "is", "a", "corpus"]

print("Next Word Predictions:")
for word in test_words:
    next_word = predict_next_word(word)
    if next_word:
        print(f"Next word after '{word}': {next_word}")
    else:
        print(f"No prediction available for the word '{word}'")
