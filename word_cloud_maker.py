import matplotlib.pyplot as pPlot
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image

# text1 = open("./texts/seven_april.txt", "r").read().lower()
# title1 = "7th April"
#
# text2 = open("./texts/eight_april.txt", "r").read().lower()
# title2 = "8th April"
#
# text3 = open("./texts/nine_april.txt", "r").read().lower()
# title3 = "9th April"
#
# text4 = open("./texts/nine_april.txt", "r").read().lower()
# title4 = "9th April 2"

text5 = open("./texts/unit_three.txt", "r").read().lower()
title5 = "4th May"

STOPWORDS.add("ve")

def create_word_cloud(string, title):
   # maskArray = np.array(Image.open("cloud.png"))
   maskArray = np.array(Image.open("cloud_three.png"))

   cloud = WordCloud(background_color = "white", max_words = 200, mask = maskArray, stopwords = set(STOPWORDS))
   cloud.generate(string)
   clean_title = title.replace(" ", "")
   cloud.to_file("%swordCloud.png" % clean_title)
# create_word_cloud(text1, title1)
# create_word_cloud(text2, title2)
# create_word_cloud(text3, title3)
create_word_cloud(text5, title5)
