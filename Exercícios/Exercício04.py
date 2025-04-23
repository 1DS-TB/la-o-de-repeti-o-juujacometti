# Peça ao usuário um número inteiro positivo e calcule seu fatorial usando um laço for ou while. Exemplo: 5! = 5 × 4 × 3 × 2 × 1 = 120.

# Solicitaçao para o usuário
N = int(input("Digite um número inteiro positivo: "))

# Condição
if N >= 0:
    fatorial = 1
    indice = 1

    # Looping
    while indice <= N:
        fatorial = fatorial * indice
        indice += 1
        print(fatorial)

    print(f"O fatorial de {N} é: {fatorial}")

elif N <= 0:
    print("INVALIDO")