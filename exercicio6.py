# Peça ao usuário um número N e gere os primeiros N termos da sequência de Fibonacci usando um laço. Exemplo: 0, 1, 1, 2, 3, 5, 8....

# Solicitação para o usuário
N = int(input("Digite um número para gerar a sequência de Fibonacci:\n"))

# Variáveis para iniciar a sequência
x = 0
y = 1

if N > 0:
    print(f"A sequência de Fibonacci ate o {N} algarismo é:")

    # Looping para imprimir os próximos números, de acordo com a quantidade n
    for i in range(0, N):
        print(x, end=", ")
        z = x + y
        x = y
        y = z

elif N <= 0:
    print("INVALIDO")