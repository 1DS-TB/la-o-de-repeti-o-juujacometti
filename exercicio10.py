# Implemente um algoritmo que encontre e imprima todos os números de Kaprekar em um intervalo definido pelo usuário (ex: 1 a 10000). Onde você irá solicitar os 2 numeros do intervalo

# Lista pra armazenar os valores kaprekar
kaprekar = []

# Determinação do início e fim da sequência
inicio = int(input("Digite o número inicial:\n"))
fim = int(input("Digite o número final:\n"))

# Verifica se o início é maior que o fim
if inicio <= 0 or fim <= 0 or inicio > fim:
    print("INVALIDO")

else:
    for numero in range(inicio, fim + 1):
        quadrado = numero ** 2
        quadrado_str = str(quadrado)
        digitos = len(str(numero))

        # Separação (direita e esquerda)
        direita = quadrado_str[-digitos:]
        esquerda = quadrado_str[:-digitos]

        if esquerda == '':
            esquerda = '0'

        soma = int(esquerda) + int(direita)

        if soma == numero:
            print(f"{numero} é um número de Kaprekar!")