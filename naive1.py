import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('teste.csv')

x = df.drop('Usuário', axis=1)
y = df['Usuário']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

model = GaussianNB()
model.fit(x_train, y_train)
