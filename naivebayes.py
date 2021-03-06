#importar bibliotecas
from nltk import word_tokenize
import nltk
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn import metrics
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.model_selection import cross_val_predict
from nltk.tokenize import TweetTokenizer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

#ler o dataset
df = pd.read_csv('dados_treino_1000.csv', encoding='utf-8')
df2 = pd.read_csv('dados_teste.csv', encoding='utf-8')

#removendo os valores duplicados
df.drop_duplicates(['Tweet'], inplace=True)
df2.drop_duplicates(['Tweet'], inplace=True)
df.dropna(axis=0, how='all')
df2.dropna(axis=0, how='all')

#separar tweets e suas classes
tweets = df['Tweet']
sentimento = df['Sentimento']
tweets2 = df2['Tweet']
sentimento2 = df2['Sentimento']

#função de pré-processamento
def Preprocessing(instancia):
    instancia = re.sub(r"http\S+", "", instancia).lower().replace('.','').replace(';','').replace('-','').replace(':','').replace(')','').replace('"','')
    stopwords = set(nltk.corpus.stopwords.words('portuguese'))
    palavras = [i for i in instancia.split() if not i in stopwords]
    return (" ".join(palavras))

#aplicar a função em todos os dados
tweets = [Preprocessing(i) for i in tweets]
tweets2 = [Preprocessing(i) for i in tweets2]

#instanciar o objeto que faz a vetorização dos dados
tweet_tokenizer = TweetTokenizer() 
vectorizer = CountVectorizer(analyzer="word", tokenizer=tweet_tokenizer.tokenize)

#aplicar o vetorizador nos dados e retorna uma matriz esparsa
freq_tweets = vectorizer.fit_transform(tweets)
freq_testes = vectorizer.transform(tweets2)
type(freq_tweets)

#visualizar o número de linhas e colunas da matriz:
freq_tweets.shape

print(freq_tweets.data[0:5])

#modelagem do modelo
modelo = MultinomialNB()
modelo.fit(freq_tweets,sentimento)

esperado = sentimento2
previsao = modelo.predict(freq_testes)

print(metrics.classification_report(esperado, previsao))
print(metrics.confusion_matrix(esperado, previsao))

print("Precisão: ", metrics.accuracy_score(esperado, previsao))