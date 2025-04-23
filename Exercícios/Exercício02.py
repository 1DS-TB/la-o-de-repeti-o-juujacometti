# Peça ao usuário um número inteiro positivo N e calcule a soma de todos os números de 1 até N usando um laço while
soma = 0

# Solicitação para o usuário
numero = int(input("Por favor, insira um número inteiro positivo: "))

if numero <= 0:
    print("INVALIDO")

else:
    # Looping
    numero += 1
    while numero > 1:
        numero -= 1
        soma += numero

print(f"A soma de todos os números de 1 ate {numero} é: {soma}")