# DATA FRAMES
# Múltiplos vetores de classes diferentes, mas com o mesmo tamanho.

using DataFrames # Importa a biblioteca DataFrames para ser utilizada no código

vector1 = [188.2, 181.3, 193.4] # Cria um vetor dinâmico com tamanho variado
vector2 = ["Jeff", "Roger", "Andrew", "Brian"] # Cria um vetor dinâmico com tamanho variado

myDataFrame = DataFrame(Heights = vector1, First_names = vector2) # Cria um data frame usando os dois vetores criados anteriormente, atribuindo o nomes as colunas em que os dois serão posicionados e depois o printa

# Contudo, um erro será gerado, pois os dois vetores tem tamanhos diferentes, então o data frame não será construída de forma correta.

# Mesmo printando, gerará um erro, pois o data frame não foi gerado por consequência da má construção dos dois vetores.
# Portanto, uma correção deverá ser feita: diminuir o número de elementos de um vetor, ou acrescentar mais um elemento no outro vetor.

vector1 = [188.2, 181.3, 193.4] # Cria um vetor dinâmico com tamanho variado
vector2 = ["Jeff", "Roger", "Andrew"] # Cria um vetor dinâmico com tamanho variado

myDataFrame = DataFrame(Heights = vector1, First_names = vector2) # Cria um data frame usando os dois vetores criados anteriormente, atribuindo o nomes as colunas em que os dois serão posicionados e depois o printa