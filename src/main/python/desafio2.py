#!/usr/bin/env python3

import pandas as pd
import requests

df_train = pd.read_csv('train.csv').fillna(0)

df_train['NOTA_FINAL'] = (3.0 * df_train['NU_NOTA_MT'] +
                          2.0 * df_train['NU_NOTA_CN'] +
                          1.5 * df_train['NU_NOTA_LC'] +
                          1.0 * df_train['NU_NOTA_CH'] +
                          3.0 * df_train['NU_NOTA_REDACAO']) / (3.0 + 2.0 + 1.5 + 1.0 + 3.0)

# procurar melhor correlacionamento

# criar modelo

# usar modelo para predição

df = pd.read_csv('test2.csv')

# df['NU_NOTA_MT'] = usar modelo para predição

df_answer = df[['NU_INSCRICAO', 'NU_NOTA_MT']]

answer = [{'NU_INSCRICAO': v[0], 'NU_NOTA_MT': v[1]} for v in df_answer.values]

envio = {
    "token": "b33ce0b52f2252786237a0ce80417dbfa954214c",
    "email": "ramonchiara@gmail.com",
    "answer": answer
}

r = requests.post('https://api.codenation.com.br/v1/user/acceleration/data-science/challenge/enem-2/submit', json = envio)
print(r.text)