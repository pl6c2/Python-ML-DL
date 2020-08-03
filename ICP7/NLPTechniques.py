import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import numpy as np

url = 'https://en.wikipedia.org/wiki/Google'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

# print(soup.prettify())
# print(soup.text)
f1 = open("TextFile", "w")

for i in soup.find_all('p'):
    f1.write(str(i.text))

f1.close()

from nltk.tokenize import sent_tokenize, word_tokenize


f = open("TextFile", "r")   # opening a file
data = f.read()

# for i in word_tokenize(data):
#     print(i)


from nltk.stem import PorterStemmer

ps = PorterStemmer()
# for i in word_tokenize(data):
#     print(ps.stem(i))

# Parts of speech tagging can be important for syntactic and semantic analysis. So, for something like the sentence above
# the word can has several semantic meanings. One being a modal for question formation, another being a container for
# holding food or liquid, and yet another being a verb denoting the ability to do something. Giving a word such as this a
# specific meaning allows for the program to handle it in the correct manner in both semantic and syntactic analyses.

import nltk
# for i in word_tokenize(data):
#     print(nltk.pos_tag(i))




from nltk import WordNetLemmatizer
# lemmatizer = WordNetLemmatizer()
# for i in word_tokenize(data):
#     print(lemmatizer.lemmatize(i))

# from nltk.collocations import BigramCollocationFinder
# from nltk.metrics import BigramAssocMeasures
# finder = BigramCollocationFinder.from_words(data)
# finder.nbest(BigramAssocMeasures.likelihood_ratio(10))


# from nltk.collocations import TrigramCollocationFinder
# from nltk.metrics import TrigramAssocMeasures
# finder = TrigramCollocationFinder.from_words(data[:100])
# finder.nbest(TrigramAssocMeasures.likelihood_ratio(10))
# triword =  [t for t in nltk.trigrams(data)]
# print(triword)

# trigrm = list(nltk.trigrams(data.split()))
#
#
# print(*map(' '.join, trigrm), sep=', ')

# Some English words occur together more frequently. For example - Sky High, do or die, best performance,
# heavy rain etc. So, in a text document we may need to identify such pair of words which will help in sentiment
# analysis. First, we need to generate such word pairs from the
# existing sentence maintain their current sequences. Such pairs are called bigrams


# Named Entity Recognition, also known as entity extraction classifies named entities that are present in a text
# into pre-defined categories like “individuals”, “companies”, “places”, “organization”, “cities”, “dates”,
# “product terminologies” etc. It adds a wealth of semantic knowledge to your content and helps you to promptly understand
# the subject of any given text.

# for i in word_tokenize(data):
#     tagged = nltk.pos_tag(i)
#     namedEnt = nltk.ne_chunk(tagged)
    # namedEnt.draw()

# def preprocess(data):
#     sent = nltk.word_tokenize(data)
#     sent = nltk.pos_tag(sent)
#     return sent
#
#
# sent = preprocess(data)
# # print(sent)
#
# pattern = 'NP: {<DT>?<JJ>*<NN>}'
#
# cp = nltk.RegexpParser(pattern)
# cs = cp.parse(sent)
#
# # print(cs)
#
# from nltk.chunk import conlltags2tree, tree2conlltags
# from pprint import pprint
# iob_tagged = tree2conlltags(cs)
# # pprint(iob_tagged)
#
# ne_tree = nltk.ne_chunk(nltk.pos_tag(word_tokenize(data)))
# print(ne_tree)
