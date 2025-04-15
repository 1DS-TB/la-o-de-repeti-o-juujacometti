# Peça ao usuário um número N e gere os primeiros N termos da sequência de Fibonacci usando um laço. Exemplo: 0, 1, 1, 2, 3, 5, 8....

# Solicitação para o usuário
n = int(input("Digite um número para gerar a sequência de Fibonacci:\n"))

# Variáveis para iniciar a sequência
a = 0
b = 1

if n > 0:
    print(f"A sequência de Fibonacci ate o {n} algarismo é:")

    # Impressão dos dois primeiros números da sequência
    print(f"\n{a}\n{b}")

    # Looping para imprimir os próximos números, de acordo com a quantidade n
    for sequencia in range(
            n - 2):  # Subtração de -2 de n para que os dois primeiros algarismos não extrapolem a quantidade
        novo_numero = a + b
        a = b
        b = novo_numero
        print(b)
else:
    print("INVALIDO")