# LOGICAL SUBSETTING

using DataFrames # Importa a biblioteca DataFrames para ser utilizada no código

vector1 = [188.2, 181.3, 193.4, 192.3] # Cria um vetor dinâmico com tamanho variado
vector2 = ["Jeff", "Roger", "Andre", "Brian"] # Cria um vetor dinâmico com tamanho variado
myDataFrame = DataFrame(Heights = vector1, First_names = vector2) # Cria um data frame usando os dois vetores criados anteriormente, atribuindo o nomes as colunas em que os dois serão posicionados

print(myDataFrame[myDataFrame.First_names .== "Jeff", :]) # Printa o valor do data frame que corresponda a todos os "First_names" iguais a "Jeff"
print("\n\n===============\n\n") # Printa um separador
print(myDataFrame[myDataFrame.Heights .< 190, :]) # Printa o valor do data frame que corresponda a todos os "Heights" menor que 190