# Importando as bibliotecas que iremos utilizar:
from nltk import word_tokenize
import nltk
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import cross_val_predict
from nltk.tokenize import TweetTokenizer

# Lendo a base de dados:
df = pd.read_csv('whindersson.csv', encoding='utf-8')

df.head().T

# Número de linhas da coluna ‘Text’:
df.Tweet.count()

# Removendo os valores duplicados:
df.drop_duplicates(['Tweet'], inplace=True)

df.Tweet.count()

# Separando tweets e suas classes:
tweets = df['Tweet']
usuario = df['Usuário']

def Preprocessing(instancia):
    instancia = re.sub(r"http\S+", "", instancia).lower().replace('.','').replace(';','').replace('-','').replace(':','').replace(')','').replace('"','')
    stopwords = set(nltk.corpus.stopwords.words('portuguese'))
    palavras = [i for i in instancia.split() if not i in stopwords]
    return (" ".join(palavras))

# Aplica a função em todos os dados:
tweets = [Preprocessing(i) for i in tweets]

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

# Treino de modelo de Machine Learning:
modelo = MultinomialNB()
modelo.fit(freq_tweets,usuario)

# Defina instâncias de teste dentro de uma lista:
testes = []

# Transforma os dados de teste em vetores de palavras:
freq_testes = vectorizer.transform(testes)

# Fazendo a classificação com o modelo treinado:
for t, c in zip (testes,modelo.predict(freq_testes)):
    # t representa o tweet e c a classificação de cada tweet.
    print (t +", "+ c) 