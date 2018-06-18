#!/usr/bin/env python3

import pandas as pd
import requests

df_train = pd.read_csv('train.csv').fillna(0)

from sklearn import linear_model

cols = [
    'NU_IDADE',
    'TP_COR_RACA',
    'TP_ANO_CONCLUIU',
    'TP_ESCOLA',
    'TP_ENSINO',
    'IN_TREINEIRO',
    'TP_DEPENDENCIA_ADM_ESC',
    'IN_BAIXA_VISAO',
    'IN_CEGUEIRA',
    'IN_SURDEZ',
    'IN_DISLEXIA',
    'IN_DISCALCULIA',
    'IN_SABATISTA',
    'IN_GESTANTE',
    'IN_IDOSO',
    'NU_NOTA_CN',
    'NU_NOTA_LC',
    'NU_NOTA_CH',
    'NU_NOTA_REDACAO'
]

x = df_train[cols]
y = df_train['NU_NOTA_MT']

lm = linear_model.LinearRegression()
model = lm.fit(x, y)

# print(lm.score(x, y))

df = pd.read_csv('test2.csv').fillna(0)

x = df[cols]

predictions = lm.predict(x)

df['NU_NOTA_MT'] = predictions

df_answer = df[['NU_INSCRICAO', 'NU_NOTA_MT']]

answer = [{'NU_INSCRICAO': v[0], 'NU_NOTA_MT': v[1]} for v in df_answer.values]

envio = {
    "token": "b33ce0b52f2252786237a0ce80417dbfa954214c",
    "email": "ramonchiara@gmail.com",
    "answer": answer
}

r = requests.post('https://api.codenation.com.br/v1/user/acceleration/data-science/challenge/enem-2/submit', json=envio)
print(r.text)
