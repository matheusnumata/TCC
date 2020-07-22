from __future__ import division
from sklearn.model_selection import train_test_split
from stop_words import get_stop_words
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

auth = tweepy.OAuthHandler('Gges03ofUCtG7Fy4TI6Jy8XSE', 'woHaPvBJJSqYbbmjTnZnsy7vGIi6hq2qvIdY6t9BnVpWVPTO3u')
auth.set_access_token('957936725275365376-SmyN2POrnlLlXvDUd0AvccUL1d2lwQH', 'Vp0xBunfHNRmyCyqDxZ5PV2lijnsmQJIUWTfcojM1BnSZ')

api = tweepy.API(auth, wait_on_rate_limit=True)

searchQuery = 'morte OR se mata OR desgraça OR morre OR felicidade OR te amo OR saudades'

public_tweets = api.search(q=searchQuery, count=100,
                            result_type="recent",
                            lang="pt-br")

#public_tweets = api.user_timeline(screen_name='whindersson', count=100)

#abre/cria um arquivo csv
#csvFile = open('teste.csv', 'w')

with open('ofensivo.csv', 'w', encoding='utf-8') as csvFile:
    writer = csv.writer(csvFile, delimiter=',', dialect='excel', quotechar =  '"')
    writer.writerow(["ID",
                    "Usuário",
                    "Tweet",
                    "Seguidores",
                    "Sentimento"])

    for tweet in public_tweets:
        if tweet.text.startswith("RT @") == True:
            print('This tweet is a retweet')
        else:
            print('This tweet is not retweet')
            post = tweet.text
            post = post.replace('\n', ' ')
            writer.writerow(([str(tweet.user.id),
                            str(tweet.user.screen_name),
                            str(post),
                            str(tweet.user.followers_count)]))
        #print (tweet.text);
def on_data(self, data):
    datajson = json.loads(data)
    if any([i for i in filterKeywords if i in datajson["text"]]):
        """Do Desired function"""
