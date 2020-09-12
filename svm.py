#importar bibliotecas
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.svm import SVC
from nltk.tokenize import TweetTokenizer
import pandas as pd
import re
import nltk

#ler o dataset
dados_treino = pd.read_csv('dados_treino.csv', encoding='utf-8')
dados_teste = pd.read_csv('dados_teste.csv', encoding='utf-8')

#removendo os valores duplicados
dados_treino.drop_duplicates(['Tweet'], inplace=True)

#separar tweets e suas classes
tweets = dados_treino['Tweet']
classificacao = dados_treino['Sentimento']
tweets2 = dados_teste['Tweet']
classificacao2 = dados_teste['Sentimento']

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

#visualizar o número de linhas e colunas da matriz
freq_tweets.shape

#modelagem do modelo
svclassifier = SVC(kernel='linear')
svclassifier.fit(freq_tweets, classificacao)

esperado = classificacao2
previsao = svclassifier.predict(freq_testes)

print(confusion_matrix(esperado, previsao))
print(classification_report(esperado, previsao))
