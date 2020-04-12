import nltk, re
from nltk.tokenize import word_tokenize
# importing ngrams module from nltk
from nltk.util import ngrams
from collections import Counter

#text = open("iliad.txt", encoding='utf-8').read().lower()
text1 = open("./texts/seven_april.txt", "r").read().lower()
#text2 = open("./texts/eight_april.txt", "r").read().lower()
#text3 = open("./texts/nine_april.txt", "r").read().lower()
#text4 = open("./texts/nine_april.txt", "r").read().lower()

cleaned = re.sub('\W+', ' ', text1).lower()
tokenized = word_tokenize(cleaned)

# Change the n value to 2:
bigrams = ngrams(tokenized, 2)
bigrams_frequency = Counter(bigrams)

# Change the n value to 3:
trigrams = ngrams(tokenized, 3)
trigrams_frequency = Counter(trigrams)

# Change the n value to a number greater than 3:
pentagrams = ngrams(tokenized, 5)
pentagrams_frequency = Counter(pentagrams)

print("Bigrams:")
print(bigrams_frequency.most_common(10))

print("\nTrigrams:")
print(trigrams_frequency.most_common(10))

print("\nPentagrams:")
print(pentagrams_frequency.most_common(10))
