#!/usr/bin/env python3

import pandas as pd
import requests

df_train = pd.read_csv('train.csv').fillna(0)

import statsmodels.api as sm

x = df_train[['NU_NOTA_CN', 'NU_NOTA_LC', 'NU_NOTA_CH', 'NU_NOTA_REDACAO']]
y = df_train['NU_NOTA_MT']

model = sm.OLS(y, x).fit()

df = pd.read_csv('test2.csv').fillna(0)

x = df[['NU_NOTA_CN', 'NU_NOTA_LC', 'NU_NOTA_CH', 'NU_NOTA_REDACAO']]

predictions = model.predict(x)

df['NU_NOTA_MT'] = predictions.values.reshape(-1, 1)

df_answer = df[['NU_INSCRICAO', 'NU_NOTA_MT']]

answer = [{'NU_INSCRICAO': v[0], 'NU_NOTA_MT': v[1]} for v in df_answer.values]

envio = {
    "token": "b33ce0b52f2252786237a0ce80417dbfa954214c",
    "email": "ramonchiara@gmail.com",
    "answer": answer
}

r = requests.post('https://api.codenation.com.br/v1/user/acceleration/data-science/challenge/enem-2/submit', json=envio)
print(r.text)
