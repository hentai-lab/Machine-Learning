# FACTORS
# Variáveis qualitativas que podem ser incluídas no modelo.

import pandas # Importa a biblioteca Pandas para ser utilizada no código

smoker = ["Yes", "No", "Yes", "Yes"] # Cria um vetor dinâmico com tamanho variado
smokeFactor = pandas.Series(smoker, dtype="category") # Cria uma série categórica utilizando o vetor criado anteriormente e o data type (tipo de dado) "category"
print(smokeFactor) # Printa a série categórica