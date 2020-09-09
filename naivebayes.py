# Importando as bibliotecas que iremos utilizar:
from nltk import word_tokenize
import nltk
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn import metrics
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from nltk.tokenize import TweetTokenizer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# Lendo a base de dados:
df = pd.read_csv('dados_treino.csv', encoding='utf-8')

df2 = pd.read_csv('dados_teste.csv', encoding='utf-8')


df.head().T

# Número de linhas da coluna ‘Text’:
df.Tweet.count()

# Removendo os valores duplicados:
df.drop_duplicates(['Tweet'], inplace=True)

df.Tweet.count()

# Separando tweets e suas classes:
tweets = df['Tweet']
classificacao = df['Sentimento']
tweets2 = df2['Tweet']
classificacao2 = df2['Sentimento']

def Preprocessing(instancia):
    instancia = re.sub(r"http\S+", "", instancia).lower().replace('.','').replace(';','').replace('-','').replace(':','').replace(')','').replace('"','')
    stopwords = set(nltk.corpus.stopwords.words('portuguese'))
    palavras = [i for i in instancia.split() if not i in stopwords]
    return (" ".join(palavras))

# Aplica a função em todos os dados:
tweets = [Preprocessing(i) for i in tweets]
tweets2 = [Preprocessing(i) for i in tweets2]

# Antes:
tweets[:10]

tweet_tokenizer = TweetTokenizer() 

# Instancia o objeto que faz a vetorização dos dados de texto:
vectorizer = CountVectorizer(analyzer="word", tokenizer=tweet_tokenizer.tokenize)

# Aplica o vetorizador nos dados de texto e retorna uma matriz esparsa ( contendo vários zeros):
freq_tweets = vectorizer.fit_transform(tweets)
type(freq_tweets)

# Visualizando o número de linhas e colunas da matriz:
freq_tweets.shape

#print(freq_tweets.shape)

# Treino de modelo de Machine Learning:
modelo = MultinomialNB()
modelo.fit(freq_tweets,classificacao)

freq_testes = vectorizer.transform(tweets2)

expected = classificacao2
predicted = modelo.predict(freq_testes)

# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))