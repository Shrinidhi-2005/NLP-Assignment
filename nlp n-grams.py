import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
nltk.download('punkt')
text = "Natural language processing with Python is quite interesting and fun."
tokens = word_tokenize(text.lower())
# Unigrams
unigrams = list(ngrams(tokens, 1))
print("Unigrams:", unigrams)

# Bigrams
bigrams = list(ngrams(tokens, 2))
print("Bigrams:", bigrams)

# Trigrams
trigrams = list(ngrams(tokens, 3))
print("Trigrams:", trigrams)

# N-grams (e.g., 4-grams)
n = 4
ngrams_list = list(ngrams(tokens, n))
print(f"{n}-grams:", ngrams_list)
