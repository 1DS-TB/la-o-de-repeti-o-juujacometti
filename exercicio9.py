# Um número perfeito é aquele cuja soma de seus divisores (exceto ele mesmo) é igual a ele mesmo. Ex: 6 (1 + 2 + 3 = 6). Encontre todos os números perfeitos entre 1 e 10000 usando laços.

# Looping para reaçizar a verificação de 1 a 10000
for num in range(1, 10001):
    soma = 0

    for i in range(1, num):
        # Verificação se o contador é o divisor do número
        if num % i == 0:
            soma += i

    # Adiciona o número perfeito ao final da lista
    if soma == num:
        print(f"{num} é um número perfeito.")
