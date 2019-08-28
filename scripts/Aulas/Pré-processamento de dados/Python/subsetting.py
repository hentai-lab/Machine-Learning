# SUBSETTING

import pandas # Importa a biblioteca Pandas para ser utilizada no código

vector1 = [188.2, 181.3, 193.4, 192.3] # Cria um vetor dinâmico com tamanho variado
vector2 = ["Jeff", "Roger", "Andre", "Brian"] # Cria um vetor dinâmico com tamanho variado
data = {'Heights': vector1, 'First_names': vector2} # Cria uma variável que armazena dois títulos com os dois vetores como valores
myDataFrame = pandas.DataFrame(data) # Cria um data frame usando a variável criada anteriormente como valor, listando de forma ordenada os dois valores (vetores)

vectorFactor = pandas.Series(vector2, dtype="category") # Cria uma série categórica utilizando o vetor criado anteriormente (vector2) e o data type (tipo de dado) "category"

print(vector1[:1]) # Printa o valor da primeira posição do vector1
print(vector1[0:2], vector1[3:]) # Printa o valor da primeira, segunda e quarta posição posição do vector1, respectivamente
print("\n=======================\n") # Printa um separador
print(myDataFrame[0:1]) # Printa apenas a primeira linha do data frame
print("\n=======================\n") # Printa um separador
print(myDataFrame['First_names'].to_string(index=False)) # Printa apenas os nomes ("First_names") que estão contidos dentro do data frame
print("\n=======================\n") # Printa um separador
print(vectorFactor) # Printa a série categórica