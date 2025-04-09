# Peça ao usuário um número inteiro positivo N e calcule a soma de todos os números de 1 até N usando um laço while
soma = 0
contador = 1

# Solicitação para o usuário
n = int(input("Insira um número inteiro positivo:\n"))

if n < 0:
    print("INVALIDO")

else:
    # Looping
    while contador <= n:
        soma += contador
        contador += 1
    print(f"A soma de todos os números de 1 ate {n} é: {soma}")




