# Um número perfeito é aquele cuja soma de seus divisores (exceto ele mesmo) é igual a ele mesmo. Ex: 6 (1 + 2 + 3 = 6). Encontre todos os números perfeitos entre 1 e 10000 usando laços.

# Lista para armazenar os números perfeitos
numeros_perfeitos = []

# Looping para reaçizar a verificação de 1 a 10000
for numero in range(1, 10001):
    soma = 0

    for contador in range(1, numero):
        # Verificação se o contador é o divisor do número
        if numero % contador == 0:
            soma += contador

    # Adiciona o número perfeito ao final da lista
    if soma == numero:
        numeros_perfeitos.append(numero)
        
print(f"Os números perfeitos de 1 a 10.000 são: {numeros_perfeitos}")