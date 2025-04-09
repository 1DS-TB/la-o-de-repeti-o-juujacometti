# Peça ao usuário um número inteiro positivo e calcule seu fatorial usando um laço for ou while. Exemplo: 5! = 5 × 4 × 3 × 2 × 1 = 120.

fatorial = 1

# Solicitação para o usuário
numero = int(input("Digite um número inteiro positivo:\n"))

# Condição para verificar se o número informado se enquadra nos parâmetros
if (numero < 0):
    print("INVALIDO")

else:
    while numero > 0:
        fatorial = fatorial * numero
        numero = numero - 1
print(fatorial)


