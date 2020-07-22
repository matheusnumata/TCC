from __future__ import division
from sklearn.model_selection import train_test_split
from nltk.tokenize import TweetTokenizer, word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from stop_words import get_stop_words
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import numpy as np
import string
import nltk
import nltk.corpus
import re
from string import punctuation 
from nltk.corpus import stopwords 

# Read in tweet data
tweets_data_path = 'teste.csv'

data = pd.read_csv(tweets_data_path, header=0, encoding='utf-8', error_bad_lines=False)

tweets = data['Tweet']
seguidores = data['Seguidores']

class PreProcessTweets:
    def __init__(self):
            
        exemplo = "Esta é uma frase de teste"
        word_tokens = word_tokenize(exemplo)

        self._stopwords = set(stopwords.words('portuguese') + list(punctuation) + ['AT_USER','URL'])

        filtered_sentence = []

        for w in word_tokens:
            if w not in stopwords:
                filtered_sentence.append(w)

        print(word_tokens)
        print(filtered_sentence)
