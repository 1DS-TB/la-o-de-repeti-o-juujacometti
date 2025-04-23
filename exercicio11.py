# Criar um jogo onde dois jogadores (ou um jogador e a CPU) lutam em turnos até que um seja derrotado.

import random

jogo_ativo = True

# Looping para inicializar jogo
while jogo_ativo:
    print(f"{20 * "="}\n⚔️🤖 CYBER DUEL 🤖⚔️\n{20 * "="}")

    # Menu de opções para o usuário
    print("\n[ 1 ] Iniciar jogo 🎮\n[ 2 ] Encerrar jogo ❌")
    escolha = int(input("Informe sua escolha: "))

    # Usuário saiu do jogo
    if escolha == 2:
        print("\nEncerrando o jogo em 3... 2.. 1. ❌")
        break

    elif escolha == 1:
        # Definição da vida, ataque, cura e defesa (jogador e inimigo)
        vida_jogador = random.randint(100, 500)
        vida_inimigo = random.randint(100, 500)
        # Salvar o valor máximo de vida

        vida_jogador_max = vida_jogador
        vida_inimigo_max = vida_inimigo

        ataque_jogador = random.randint(10, 50)
        ataque_inimigo = random.randint(10,50)

        defesa_jogador = random.randint(10, 25)
        defesa_inimigo = random.randint(10,25)

        cura = random.randint(5, 20)


        print(f"\n{15 * "_"}\n   VOCÊ 🧔\n❤️ Vida = {vida_jogador}\n🤺 Ataque = {ataque_jogador}\n🛡️ Defesa = {defesa_jogador}\n{15 * "_"}")
        print(f"\n{15 * "_"}\n   INIMIGO 👹\n❤️ Vida = {vida_inimigo}\n🤺 Ataque = {ataque_inimigo}\n🛡️ Defesa = {defesa_inimigo}\n{15 * "_"}\n")

        # Início rodadas:
        rodada = 1

        # Solicitação de decisão do usuário
        while vida_jogador > 0 and vida_inimigo > 0:
            print(f"{14 * "*"}\n* Rodada: {rodada} *\n🧔 Vida: {vida_jogador} | 👹 Vida: {vida_inimigo}")
            decisao = int(input(f"[ 1 ] Atacar\n[ 2 ] Curar\nEscolha: "))

            # Ataque
            if decisao == 1:
                dano = ataque_jogador - defesa_inimigo

                if dano <= 0:
                    dano = 0

                vida_inimigo = vida_inimigo - dano
                print(f"\nVocê atacou! Inimigo perde {dano} de vida. 🤺")

            # Cura
            elif decisao == 2:
                vida_jogador = min(vida_jogador + cura, vida_jogador_max)
                print(f"\nVocê se curou em {cura} de vida. 💊")

            # Opção inválida
            else:
                print("\nOpção inválida! Você perdeu o turno.")

            # Usuário vence
            if vida_inimigo <= 0:
                print("\n  🏆 Parabéns 🏆\nVocê venceu a disputa!")
                jogo_ativo = False
                break

            # Decisão do inimigo
            decisao_inimigo = random.choice(["atacar", "curar"])

            # Ataque:
            if decisao_inimigo == "atacar":
                dano = ataque_inimigo - defesa_jogador

                if dano < 0:
                    dano = 0

                vida_jogador = vida_jogador - dano
                print(f"O inimigo atacou! Você perdeu {dano} de vida. 🤺")

            # Cura
            else:
                vida_inimigo = min(vida_inimigo + cura, vida_inimigo_max)
                print(f"Inimigo se curou em {cura} de vida. 💊")

            if vida_jogador <= 0:
                print("\n  ☹️ Perdedor ☹️\nVocê perdeu a disputa!\nTente novamente!")
                jogo_ativo = False
                break

            # Próxima rodada
            rodada = rodada + 1

    else:
        print("INVALIDO")