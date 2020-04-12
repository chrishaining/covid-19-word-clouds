# importing regex and nltk
import re, nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# importing Counter to get word counts for bag of words
from collections import Counter

# importing part-of-speech function for lemmatization
from part_of_speech import get_part_of_speech

# import the texts
text1 = open("./texts/seven_april.txt", "r").read().lower()
text2 = open("./texts/eight_april.txt", "r").read().lower()
text3 = open("./texts/nine_april.txt", "r").read().lower()
text4 = open("./texts/nine_april.txt", "r").read().lower()

# define a function to count the words in a text
def count_words(text):
    cleaned = re.sub('\W+', ' ', text).lower()
    tokenized = word_tokenize(cleaned)

    stop_words = stopwords.words('english')
    filtered = [word for word in tokenized if word not in stop_words]

    normalizer = WordNetLemmatizer()
    normalized = [normalizer.lemmatize(token, get_part_of_speech(token)) for token in filtered]

    bag_of_looking_glass_words = Counter(normalized)
    return bag_of_looking_glass_words

# call the function
text1_count = count_words(text1)
text2_count = count_words(text2)
text3_count = count_words(text3)
text4_count = count_words(text4)

#print(text4_count)
