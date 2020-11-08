from __future__ import division
import tweepy
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
import csv
import io
from textblob import TextBlob
import time
from googletrans import Translator

tradutor = Translator()

auth = tweepy.OAuthHandler('Gges03ofUCtG7Fy4TI6Jy8XSE', 'woHaPvBJJSqYbbmjTnZnsy7vGIi6hq2qvIdY6t9BnVpWVPTO3u')
auth.set_access_token('957936725275365376-SmyN2POrnlLlXvDUd0AvccUL1d2lwQH', 'Vp0xBunfHNRmyCyqDxZ5PV2lijnsmQJIUWTfcojM1BnSZ')

api = tweepy.API(auth, wait_on_rate_limit=True)

query_treino = "morte OR puta que pariu OR vai se fuder OR caralho OR filho da puta OR desgraça OR merda OR morra OR morre OR foda-se"
query_teste = "futebol OR felicidade OR neutro OR feliz OR normal -filter:retweets"

public_tweets2 = tweepy.Cursor(api.search,
                               q="morte OR puta que pariu OR vai se fuder OR caralho OR filho da puta OR desgraça OR merda OR morra OR morre OR foda-se -filter:retweets",
                               lang="pt-br",).items(1000)

with open('dados_treino_1000.csv', 'w', encoding='utf=8') as csvFile:
            writer = csv.writer(csvFile, delimiter=',', dialect='excel')
            writer.writerow(["ID",
                            "Usuário",
                            "Tweet",
                            "Seguidores",
                            "Polaridade",
                            "Subjetividade",
                            "Sentimento"]) 
            for tweet in public_tweets2:
                frase = tweet.text 
                frase_textblob = TextBlob(tweet.text)
                frase_detect = tradutor.detect(frase)
                
                if frase_detect != 'english':
                    traducao = tradutor.translate(tweet.text, dest='en')
                    traducao_blob = TextBlob(traducao.text)
                    #print(traducao)
                    #print('Tweet: {0} - Sentimento: {1}'.format(tweet.text, traducao_blob.sentiment))
                    if (traducao_blob.sentiment.polarity > 0.0):
                        post = tweet.text
                        post = post.replace('\n', ' ')
                        writer.writerow(([str(tweet.user.id),
                                        str(tweet.user.screen_name),
                                        str(post),
                                        str(tweet.user.followers_count),
                                        str(traducao_blob.sentiment.polarity),
                                        str(traducao_blob.sentiment.subjectivity),
                                        ("Positivo")]))
                    elif (traducao_blob.sentiment.polarity == 0.0):
                        post = tweet.text
                        post = post.replace('\n', ' ')
                        writer.writerow(([str(tweet.user.id),
                                        str(tweet.user.screen_name),
                                        str(post),
                                        str(tweet.user.followers_count),
                                        str(traducao_blob.sentiment.polarity),
                                        str(traducao_blob.sentiment.subjectivity),
                                        ("Neutro")]))
                    else:
                        post = tweet.text
                        post = post.replace('\n', ' ')
                        writer.writerow(([str(tweet.user.id),
                                        str(tweet.user.screen_name),
                                        str(post),
                                        str(tweet.user.followers_count),
                                        str(traducao_blob.sentiment.polarity),
                                        str(traducao_blob.sentiment.subjectivity),
                                        ("Negativo")]))
                else:
                    print("nao funcionou")
