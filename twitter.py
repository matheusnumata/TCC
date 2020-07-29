from __future__ import division
from sklearn.model_selection import train_test_split
from stop_words import get_stop_words
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import numpy as np
import string
import re
from tweepy import *
import tweepy
import csv
import io
from textblob import TextBlob

auth = tweepy.OAuthHandler('Gges03ofUCtG7Fy4TI6Jy8XSE', 'woHaPvBJJSqYbbmjTnZnsy7vGIi6hq2qvIdY6t9BnVpWVPTO3u')
auth.set_access_token('957936725275365376-SmyN2POrnlLlXvDUd0AvccUL1d2lwQH', 'Vp0xBunfHNRmyCyqDxZ5PV2lijnsmQJIUWTfcojM1BnSZ')

api = tweepy.API(auth, wait_on_rate_limit=True)

searchQuery = 'morte'

public_tweets = api.search(q=searchQuery, count=10,
                            result_type="recent",
                            lang="pt-br")

with open('teste.csv', 'w', encoding='utf-8') as csvFile:
            writer = csv.writer(csvFile, delimiter=',', dialect='excel', quotechar =  '"')
            writer.writerow(["ID",
                            "Usuário",
                            "Tweet",
                            "Seguidores",
                            "Polarity",
                            "Subjectivity",
                            "Sentimento"])

for tweet in public_tweets:
    frase = TextBlob(tweet.text)
    if tweet.text.startswith("RT @") == True:
            print('oi')
    elif frase.detect_language() != 'en':
        traducao = TextBlob(str(frase.translate(to='en')))
        print('Tweet: {0} - Sentimento: {1}'.format(tweet.text, traducao.sentiment))
        post = tweet.text
        post = post.replace('\n', ' ')
        writer.writerow(([str(tweet.user.id),
                        str(tweet.user.screen_name),
                        str(post),
                        str(tweet.user.followers_count),
                        str(traducao.sentiment.polarity),
                        str(traducao.sentiment.subjectivity)]))
    else:
        print('Tweet: {0} - Sentimento: {1}'.format(tweet.text, frase.sentiment))
        post = tweet.text
        post = post.replace('\n', ' ')
        writer.writerow(([str(tweet.user.id),
                        str(tweet.user.screen_name),
                        str(post),
                        str(tweet.user.followers_count),
                        str(traducao.sentiment.polarity),
                        str(traducao.sentiment.subjectivity)]))