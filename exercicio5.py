# Peça ao usuário um número e verifique se ele é primo usando um laço. Um número primo é divisível apenas por 1 e por ele mesmo.

# Variável que conta a quantidade de vezes que um número foi dividido (resto da divisão zero)
divisor = 0

# Solicitação de número para o usuário
num = int(input("Digite um número para verificar se ele é primo:\n"))

# Condição para verificar se o número é maior ou igual a 1
if num >= 1:
    # Looping para dividir o número (de dois até numero - 1)
    for i in range(1, num + 1):
        if num % i == 0 and num >= 1:
            divisor += 1

    # Condição para verificar se o número foi dividido por mais algum número além de 1 e ele mesmo
    if divisor == 2:
        print(f"{num} eh primo")

    elif divisor < 1:
        print("INVALIDO")

    else:
        print(f"{num} nao eh primo")
