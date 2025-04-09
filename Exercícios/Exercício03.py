# Peça ao usuário um número e exiba sua tabuada de multiplicação de 1 a 10 usando um laço

# Solicitação para o usuário
numero = float(input("Digite um número:\n"))
multiplicacao = 1

# Looping
while multiplicacao <= 10:
    resultado = numero * multiplicacao
    print(f"{numero} * {multiplicacao} = {resultado}")
    multiplicacao += 1



