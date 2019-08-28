# DATA FRAMES
# Múltiplos vetores de classes diferentes, mas com o mesmo tamanho.

import pandas # Importa a biblioteca Pandas para ser utilizada no código

vector1 = [188.2, 181.3, 193.4] # Cria um vetor dinâmico com tamanho variado
vector2 = ["Jeff", "Roger", "Andrew", "Brian"] # Cria um vetor dinâmico com tamanho variado
data = {'Heights': vector1, 'First_names': vector2} # Cria uma variável que armazena dois títulos com os dois vetores como valores

myDataFrame = pandas.DataFrame(data) # Cria um data frame usando a variável criada anteriormente como valor, listando de forma ordenada os dois valores (vetores)

# Contudo, um erro será gerado, pois os dois vetores tem tamanhos diferentes, então o data frame não será construída de forma correta.

print(myDataFrame) # Printa o data frame no console

# Mesmo printando, gerará um erro, pois o data frame não foi gerado por consequência da má construção dos dois vetores.
# Portanto, uma correção deverá ser feita: diminuir o número de elementos de um vetor, ou acrescentar mais um elemento no outro vetor.

vector1 = [188.2, 181.3, 193.4] # Cria um vetor dinâmico com tamanho variado
vector2 = ["Jeff", "Roger", "Andrew"] # Cria um vetor dinâmico com tamanho variado
data = {'Heights': vector1, 'First_names': vector2} # Cria uma variável que armazena dois títulos com os dois vetores como valores

myDataFrame = pandas.DataFrame(data) # Cria um data frame usando a variável criada anteriormente como valor, listando de forma ordenada os dois valores (vetores)
print(myDataFrame) # Printa o data frame no console