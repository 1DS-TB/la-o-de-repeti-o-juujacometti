# Peça ao o usuário um numero N. E o utilize laços aninhados para imprimir o seguinte padrão : N = 5

# Solicitação de quantidade para o usuário
n = int(input("Digite um número para definir a quantidade de linhas do padrão:\n"))

# Condição para verificar se o número informado pelo usuário é valido
if n > 0:
    # Looping para imprimir a quantidade de algarismos "*" escolhida pelo usuário
    for linhas in range(1, n + 1):
        print("*" * linhas)  # Multiplica a quantidade de strings
else:
    print("INVALIDO")
