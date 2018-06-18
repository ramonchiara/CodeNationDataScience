#!/usr/bin/env python3

import pandas as pd
import requests

df_train = pd.read_csv('train.csv')
df_train['TX_RESPOSTAS_MT'] = df_train[['TX_RESPOSTAS_MT']].fillna('.' * 45)
df_train = df_train.fillna(0)

df_train['TX_RESPOSTAS_MT_H'] = df_train['TX_RESPOSTAS_MT'].str[0:-5]
df_train['TX_RESPOSTAS_MT_T'] = df_train['TX_RESPOSTAS_MT'].str[-5:]
df_train['TX_RESPOSTAS_MT_1'] = df_train['TX_RESPOSTAS_MT'].str[-5:-4]
df_train['TX_RESPOSTAS_MT_2'] = df_train['TX_RESPOSTAS_MT'].str[-4:-3]
df_train['TX_RESPOSTAS_MT_3'] = df_train['TX_RESPOSTAS_MT'].str[-3:-2]
df_train['TX_RESPOSTAS_MT_4'] = df_train['TX_RESPOSTAS_MT'].str[-2:-1]
df_train['TX_RESPOSTAS_MT_5'] = df_train['TX_RESPOSTAS_MT'].str[-1:]

x = df_train[['NU_NOTA_MT', 'TX_RESPOSTAS_MT_H']]
y = df_train['TX_RESPOSTAS_MT_T']

df = pd.read_csv('test3.csv')
df['TX_RESPOSTAS_MT'] = df[['TX_RESPOSTAS_MT']].fillna('.' * 45)
df = df.fillna(0)

x = df[['TX_RESPOSTAS_MT']]

df['TX_RESPOSTAS_MT'] = '.....'

df_answer = df[['NU_INSCRICAO', 'TX_RESPOSTAS_MT']]

answer = [{'NU_INSCRICAO': v[0], 'TX_RESPOSTAS_MT': v[1]} for v in df_answer.values]

envio = {
    "token": "b33ce0b52f2252786237a0ce80417dbfa954214c",
    "email": "ramonchiara@gmail.com",
    "answer": answer
}

print(envio)

# r = requests.post('https://api.codenation.com.br/v1/user/acceleration/data-science/challenge/enem-3/submit', json=envio)
# print(r.text)
