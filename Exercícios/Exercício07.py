# Peça ao o usuário um numero N. E o utilize laços aninhados para imprimir o seguinte padrão : N = 5

# Solicitação de quantidade para o usuário
N = int(input("Digite um número para definir a quantidade de linhas do padrão:\n"))

# Condição para verificar se o número informado pelo usuário é valido
if N > 0:
    # Looping para imprimir a quantidade de algarismos "*" escolhida pelo usuário
    for num in range(1, N + 1):
        for i in range(1, num + 1):
            print(i, end="")
        print("")

elif N <= 0:
    print("INVALIDO")
