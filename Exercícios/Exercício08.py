# Calcule a soma da série harmônica até N termos: S = 1 + 1/2 + 1/3 + ... + 1/N. Arredonde o resultado para 2 casas decimais.

# Solicitação para o usuário
divisor = int(input("Digite um número:\n"))

serie_harmonica = []

n = 1
soma = 0

# Condição que verifica número negativo
if divisor < 0:
    print("INVALIDO")

else:
    # Looping
    while n <= divisor:
        serie_harmonica.append(f"1/{n}")
        serie = 1 / n
        n += 1
        soma += serie

    print(serie_harmonica)
    print(f"A soma da série harmônica é igual a: {soma:.2f}")



