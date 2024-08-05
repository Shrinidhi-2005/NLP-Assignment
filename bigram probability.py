import nltk
from nltk import bigrams
from collections import Counter, defaultdict

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

# Calculate the frequency of each unigram (individual word)
unigram_freq = Counter(tokens)

# Calculate bigram probabilities
bigram_prob = defaultdict(float)

for bigram in bigram_freq:
    bigram_prob[bigram] = bigram_freq[bigram] / unigram_freq[bigram[0]]

# Print bigram probabilities
print("Bigram Probabilities:")
for bigram, prob in bigram_prob.items():
    print(f"{bigram}: {prob:.4f}")
