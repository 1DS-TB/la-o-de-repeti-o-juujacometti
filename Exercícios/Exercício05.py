# Peça ao usuário um número e verifique se ele é primo usando um laço. Um número primo é divisível apenas por 1 e por ele mesmo.

# Variável que conta a quantidade de vezes que um número foi dividido (resto da divisão zero)
contador_divisores = 0

# Solicitação de número para o usuário
numero = int(input("Digite um número para verificar se ele é primo:\n"))

# Condição para verificar se o número é maior ou igual a 1
if numero >= 1:
    # Looping para dividir o número (de dois até numero - 1)
    for i in range(2, (numero - 1)):
        if numero % i == 0:
            contador_divisores += 1

    # Condição para verificar se o número foi dividido por mais algum número além de 1 e ele mesmo
    if contador_divisores == 0:
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")

# Condição para verificar se o número é zero
else:
    print("INVALIDO")
