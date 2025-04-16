# Calcule a soma da série harmônica até N termos: S = 1 + 1/2 + 1/3 + ... + 1/N. Arredonde o resultado para 2 casas decimais.

# Solicitação para o usuário
numero = int(input("Digite um número:\n"))

# Lista para guardar as séries
lista = []

# Variáveis
serie = 0
soma = 0

# Looping para ir de 1 até o número digitado pelo usuário
for i in range(1, numero+1):
    serie = f"1/{i}" # Formatação da série
    soma += 1/i
    lista.append(serie)

# Junção das séries com a formatação em +
serie_formatada = " + ".join(lista)

print(f'A série harmônica de {numero} é: {serie_formatada}')
print(f'A soma total é: {soma:.2f}')