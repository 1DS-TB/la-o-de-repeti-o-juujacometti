"""
No jogo criado no exercício 11, adicionar as funcionalidades citadas.
* Chance de 10% de dar o dobro de dano // * Itens Especiais Use números para escolher itens como "Poção de Força" (aumenta ataque por 2 turnos) - mínimo 4
* Adicione ao menu a opção de multiplayer, onde a CPU é substituida por outro jogador // * Efeito de status, onde cada status só pode ser usado uma vez por partida (ex: sobrecarregar vida)

"""

import random

jogo_ativo = True

# Looping para inicializar jogo
while jogo_ativo:
    print(f"{20 * "="}\n⚔️🤖 CYBER DUEL 🤖⚔️\n{20 * "="}")

    # Menu de opções para o usuário
    print("\n[ 1 ] Jogo Singleplayer 🧔\n [ 2 ] Jogo Multiplayer 🧔👩\n[ 3 ] Encerrar jogo ❌")
    escolha = int(input("Informe sua escolha: "))

    # Usuário saiu do jogo
    if escolha == 3:
        print("\nEncerrando o jogo em 3... 2.. 1. ❌")
        break