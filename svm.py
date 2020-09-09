#import biblioteca dataset
import pandas as pd

# Lendo a base de dados:
dados_treino = pd.read_csv('dados_treino.csv', encoding='utf-8')
dados_teste = pd.read_csv('dados_teste.csv', encoding='utf-8')