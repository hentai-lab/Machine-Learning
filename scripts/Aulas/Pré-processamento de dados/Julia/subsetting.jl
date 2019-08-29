# SUBSETTING

using DataFrames # Importa a biblioteca DataFrames para ser utilizada no código

vector1 = [188.2, 181.3, 193.4, 192.3] # Cria um vetor dinâmico com tamanho variado
vector2 = ["Jeff", "Roger", "Andre", "Brian"] # Cria um vetor dinâmico com tamanho variado
myDataFrame = DataFrame(Heights = vector1, First_names = vector2) # Cria um data frame usando os dois vetores criados anteriormente, atribuindo o nomes as colunas em que os dois serão posicionados

print(vector1[1], "\n\n") # Printa o valor da primeira posição do vector1
print(vector1[1], " " ,vector1[2], " " , vector1[4]) # Printa o valor da primeira, segunda e quarta posição posição do vector1, respectivamente
print("\n\n===============\n\n") # Printa um separador
print(myDataFrame[1, :]) # Printa apenas a primeira linha do data frame
print("\n\n===============\n\n") # Printa um separador
print(myDataFrame[:, 2]) # Printa apenas os nomes ("First_names") que estão contidos dentro do data frame
print("\n\n===============\n\n") # Printa um separador