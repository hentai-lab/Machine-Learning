# MISSING VALUES
# No R os valores faltantes são codificados como NA

vector1 = [188.2, 181.3, 193.4, NaN] # Cria um vetor dinâmico com tamanho variado com um dos valores sendo NaN
print(vector1) # Printa o vetor no console

print("\n\n===============\n\n") # Printa um separador

for i = 1:4  # Cria um laço de repetição que se repete por 4 vezes (tamanho do vetor)
    print(isnan(vector1[i]), "\n") # Verifica onde que há valores NaN dentro do vetor criado anteriormente, retornando um valor booleano para cada posição do vetor, indicando FALSE para onde não tem valor NaN e TRUE para onde tem, depois printa um valor por vez
end # Fecha o laço