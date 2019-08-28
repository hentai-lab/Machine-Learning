# MISSING VALUES
# No R os valores faltantes são codificados como NA

import numpy # Importa a biblioteca NumPy para ser utilizada no código

vector1 = [188.2, 181.3, 193.4, numpy.nan] # Cria um vetor dinâmico com tamanho variado com um dos valores sendo NaN
print(vector1) # Printa o vetor no console

print(numpy.isnan(vector1)) # Verifica onde que há valores NaN dentro do vetor criado anteriormente, retornando um valor booleano para cada posição do vetor, indicando FALSE para onde não tem valor NaN e TRUE para onde tem, depois printa