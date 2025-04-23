# Peça ao usuário um número e exiba sua tabuada de multiplicação de 1 a 10 usando um laço

# Solicitação para o usuário
numero = int(input("Digite um número:\n"))

# Looping para realizar a multiplicação
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")