# Peça ao usuário um número inteiro positivo N e calcule a soma de todos os números de 1 até N usando um laço while
soma = 0
contador = 1

# Solicitação para o usuário
N = int(input("Insira um número inteiro positivo:\n"))

if N < 0:
    print("INVALIDO")

else:
    # Looping
    while contador <= N:
        soma += contador
        contador += 1
    print(f"A soma de todos os números de 1 ate {N} é: {soma}")