# LOGICAL SUBSETTING

import pandas # Importa a biblioteca Pandas para ser utilizada no código

vector1 = [188.2, 181.3, 193.4, 192.3] # Cria um vetor dinâmico com tamanho variado
vector2 = ["Jeff", "Roger", "Andre", "Brian"] # Cria um vetor dinâmico com tamanho variado
data = {'Heights': vector1, 'First_names': vector2} # Cria uma variável que armazena dois títulos com os dois vetores como valores
myDataFrame = pandas.DataFrame(data) # Cria um data frame usando a variável criada anteriormente como valor, listando de forma ordenada os dois valores (vetores)

is_jeff = myDataFrame.First_names == "Jeff" # Cria uma variável para servir de função comparativa, ou seja, apenas aqueles que tem o "First_names" "Jeff" poderá aparecer na consulta ao data frame utilizando esta variável
small_heights = myDataFrame.Heights < 190 # Cria uma variável para servir de função comparativa, ou seja, apenas aqueles que tem o "Heights" menor que 190 poderá aparecer na consulta ao data frame utilizando esta variável

print(myDataFrame.loc[is_jeff]) # Printa o valor do data frame que corresponda a variável de comparação
print("\n=======================\n") # Printa um separador
print(myDataFrame[small_heights]) # Printa o valor do data frame que corresponda a variável de comparação