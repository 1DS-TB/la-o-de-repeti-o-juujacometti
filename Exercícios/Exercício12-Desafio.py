"""
No jogo criado na atividade 11, adicionar as seguintes funcionalidades:
* Sistema de Crítico Adicione uma chance de 10% de dar o dobro de dano // * Itens Especiais. Use números para escolher itens como "Poção de Força" (aumenta ataque por 2 turnos). Use a criatividade para criar pelo menos 4 itens //
* Dois jogadores: Adicione ao menu a opção de multiplayer, onde a CPU é substituida por outro jogador
* Efeito de status, onde cada status só pode ser usado uma vez por partida: 
4.1 "Buffer Overflow" Assim como um buffer overflow sobrecarrega a memória, esse efeito sobrecarrega a saúde do personagem. Efeito: A cada turno, o personagem sofre dano equivalente a 5% do seu HP máximo
4.2 "Loop Infinito" Assim como um loop infinito paralisa um programa. Efeito: O alvo perde a vez por 1 turno enquanto "reinicia o sistema"
4.3 "Tela Azul" Assim como a "tela azul" deixa o sistema vulnerável. Reduz a defesa para 0 por 2 turnos
4.4 "Cache Hit". Recupera 30% do HP máximo. Só pode ser usado quando HP está abaixo de 25%.
"""

import random

jogo_ativo = True

# Looping para inicializar jogo
while jogo_ativo:
    print(f"{20 * '='}\n⚔️🤖 CYBER DUEL 🤖⚔️\n{20 * '='}")

    # Menu de opções para o usuário
    print("\n[ 1 ] Jogo Singleplayer 🧔\n [ 2 ] Jogo Multiplayer 🧔👩\n[ 3 ] Encerrar jogo ❌")
    escolha = int(input("Informe sua escolha: "))

    # Usuário saiu do jogo
    if escolha == 3:
        print("\nEncerrando o jogo em 3... 2.. 1. ❌")
        break

    # Definição da vida, ataque, cura e defesa (jogador e inimigo)
    vida1 = random.randint(100, 500)
    vida2 = random.randint(100, 500)
    # Salvar o valor máximo de vida
    vida1_max = vida1
    vida2_max = vida2

    ataque1 = random.randint(10, 50)
    ataque2 = random.randint(10, 50)

    defesa1 = random.randint(10, 25)
    defesa2 = random.randint(10, 25)

    # Efeitos especiais (rodadas restantes)
    forca1_rodada = 0
    forca2_rodada = 0
    protecao1_rodada = 0
    protecao2_rodada = 0
    fantasma1_rodada = 0
    fantasma2_rodada= 0
    tela_azul1_rodada = 0
    tela_azul2_rodada = 0

    # Efeitos de status (ativos ou não)
    buffer1 = False
    buffer2 = False
    loop1_infinito = False
    loop2_infinito = False
    cache1_usado = False
    cache2_usado = False
    
    # Efeitos únicos por jogador
    efeitos1 = []
    efeitos2 = []
    
    print(f"\n{15 * '_'}\n   VOCÊ 🧔\n❤️ Vida = {vida1}\n🤺 Ataque = {ataque1}\n🛡️ Defesa = {defesa1}\n{15 * '_'}")
    print(f"\n{15 * '_'}\n   INIMIGO 👹\n❤️ Vida = {vida2}\n🤺 Ataque = {ataque2}\n🛡️ Defesa = {defesa2}\n{15 * '_'}\n")
    
    # Início rodadas
    rodada = 1
    
    #Looping de batalha         
    while vida1 > 0 and vida2 > 0:
        print(f"{14 * '*'}\n* Rodada: {rodada} *\n🧔 Vida: {vida1} | 👹 Vida: {vida2}")
        
        for jogador in [1, 2]:
            if vida1 <= 0 or vida2 <= 0:
                break

            # Definição de 2 jogadores ou jogador x CPU
            if escolha == 1 and jogador == 2:
                tipo = "CPU"
            else:
                tipo = "Player"            
            
            if jogador == 1:
                vida, ataque, defesa = vida1, ataque1, defesa1
                forca, protecao, fantasma = forca1_rodada, protecao1_rodada, fantasma1_rodada
                tela_azul = tela_azul2_rodada
                buffer = buffer1
                loop = loop1_infinito
                efeitos_usados = efeitos1
                cache_usado = cache1_usado
                vida_max = vida1_max
            else:
                vida, ataque, defesa = vida2, ataque2, defesa2
                forca, protecao, fantasma = forca2_rodada, protecao2_rodada, fantasma2_rodada
                tela_azul = tela_azul1_rodada
                buffer = buffer2
                loop = loop2_infinito
                efeitos_usados = efeitos2
                cache_usado = cache2_usado
                vida_max = vida2_max
                
            # Loop infinito - jogador perde o turno
            if loop:
                print(f"O jogador {jogador} perdeu a vez devido ao Loop Infinito! ♾️")
                
                if jogador == 1:
                    loop1_infinito = False
                    vida1  = vida
                    
                else:
                    loop2_infinito = False
                    vida2 = vida
                    
                continue
            
            # Tela azul - defesa zerada
            if tela_azul > 0:
                defesa = 0
                if jogador == 1:
                    tela_azul2_rodada -= 1
                else:
                    tela_azul1_rodada -= 1
                    
            # Buffer Overflow - dano contínuo
            if buffer:
                dano_buffer = int(vida_max * 0.05)
                vida -= dano_buffer
                print(f"O jogador {jogador} sofre {dano_buffer} de Buffer Overflow! 🤜")

                # Alteração da vida do jogador com o dano do buffer
                if jogador == 1:
                    vida1 = vida 
                    
                else:
                    vida2 = vida  
                            
            # Poder de Força - aumento de ataque
            if forca > 0:
                ataque += 10
                
                if jogador == 1:
                    forca1_rodada -= 1
                    
                else:
                    forca2_rodada -= 1
            
            # Poder de Proteção - aumento de defesa
            if protecao > 0:
                defesa += 10
                
                if jogador == 1:
                    protecao1_rodada -= 1
                    
                else:
                    protecao2_rodada -= 1

            # Fantasma - jogador não sofre dano por uma rodada
            if fantasma > 0:
                print(f"O jogador {jogador} está com o poder Fantasma! Não recebe dano durante essa rodada!. 👻")
                
                if jogador == 1:
                    fantasma1_rodada -= 1
                    
                else:
                    fantasma2_rodada -= 1

            # Jogador escolhe uma ação
            if tipo == "Player":
                print(f"\nJogador {jogador}, escolha sua ação:")
                print("[1] Atacar 🤺\n[2] Curar ❤️\n[3] Usar Item 🎁\n[4] Usar Efeito de Status ✨")
                decisao = input("-> ")
                
            else:
                decisao = random.choice(["1", "2", "3", "4"])

            # Decisão  1 - Atacar
            if decisao == "1":
                critico = random.random() < 0.1  # 10% de chance de crítico
                dano = ataque - defesa
                dano = max(dano, 0)  # dano nunca pode ser negativo
                
                if critico:
                    dano *= 2
                    print(f"Jogador {jogador} acertou um CRÍTICO! ⚡")
                    
                print(f"Jogador {jogador} ataca e causa {dano} de dano! 💥")
                
                # Atualiza a vida do adversário corretamente
                if jogador == 1:
                    vida2 -= dano
                    print(f"Jogador 2 perdeu {dano} de vida! 💥")
                    
                else:
                    vida1 -= dano
                    print(f"Jogador 1 perdeu {dano} de vida! 💥")

            # Decisão 2 - Curar
            elif decisao == "2":
                cura = random.randint(20, 50)
                vida += cura
                print(f"Jogador {jogador} se cura em {cura} de HP! ❤️")
                
                # Altgeração na vida dos jogadores 
                if jogador == 1:
                    vida1 = vida
                    
                else:
                    vida2 = vida

            # Decisão  3 - Usar Item
            elif decisao == "3":
                
                if tipo == "CPU":
                    item = random.choice(["1", "2", "3", "4"])
                    
                else:
                    print("[ 1 ] Poder de Força (+10 Ataque por 2 turnos) 💪")
                    print("[ 2 ] Poder de Cura (+50 HP) 💊")
                    print("[ 3 ] Poder de Defesa (+10 Defesa por 2 turnos) 🛡️")
                    print("[ 4 ] Poder de Fantasma (Não sofre dano por 1 turno) 👻")
                    item = input("Escolha um item: ")

                if item == "1":
                    print(f"Jogador {jogador} usou Poção de Força! 💪")
                    
                    if jogador == 1:
                        forca1_rodada = 2
                        
                    else:
                        forca2_rodada = 2
                        
                elif item == "2":
                    print(f"Jogador {jogador} usou Poder de Cura! 💊")
                    vida += 50
                    
                elif item == "3":
                    print(f"Jogador {jogador} usou Poder de Defesa! 🛡️")
                    
                    if jogador == 1:
                        protecao1_rodada = 2
                        
                    else:
                        protecao2_rodada = 2
                        
                elif item == "4":
                    print(f"Jogador {jogador} usou Poder Fantasma! 👻")
                    
                    if jogador == 1:
                        fantasma1_rodada = 1
                        
                    else:
                        fantasma2_rodada = 1

                if jogador == 1:
                    vida1 = vida
                    
                else:
                    vida2 = vida

            # Ação 4 - Usar Efeito de Status
            elif decisao == "4":
                
                if tipo == "CPU":
                    continue  # CPU não usa efeitos

                print("\nEfeitos disponíveis:")
                print("[ 1 ] Buffer Overflow (5% de dano por turno) 💥")
                print("[ 2 ] Loop Infinito (inimigo perde 1 turno) ♾️")
                print("[ 3 ] Tela Azul (DEF = 0 por 2 turnos) 💻")
                print("[ 4 ] Cache Hit (+30% HP, se HP < 25%) 💾")
                efeito = input("Escolha um efeito: ")

                if efeito in efeitos_usados:
                    print("Você já usou esse efeito! 😅")
                    continue
                
                # Acrescenta os efeitos que já foram usados na lista de efeitos
                efeitos_usados.append(efeito)

                if efeito == "1":
                    print("Buffer Overflow ativado! 💥")
                    
                    if jogador == 1:
                        buffer2 = True
                    
                    else:
                        buffer1 = True
                
                elif efeito == "2":
                    print("Loop Infinito ativado! ♾️")
                
                    if jogador == 1:
                        loop2_infinito = True
                
                    else:
                        loop1_infinito = True
                
                elif efeito == "3":
                    print("Tela Azul ativada! 💻")
                
                    if jogador == 1:
                        tela_azul2_rodada = 2
                
                    else:
                        tela_azul1_rodada = 2
                
                elif efeito == "4":
                
                    if vida < vida_max * 0.25 and not cache_usado:
                        cura = int(vida_max * 0.3)
                        vida += cura
                        print(f"Cache Hit ativado! Cura de {cura} HP. 💾")
                
                        if jogador == 1:
                            cache1_usado = True
                
                        else:
                            cache2_usado = True
                
                    else:
                        print("Você não pode usar Cache Hit agora! 😔")

                if jogador == 1:
                    vida1 = vida
                
                else:
                    vida2 = vida

        rodada += 1 

    # Fim do duelo
    print("\n*** FIM DE JOGO ***")
    if vida1 <= 0 and vida2 <= 0:
        print("Empate! 🤝")
        
    elif vida1 <= 0:
        print("Jogador 2 (INIMIGO) venceu! 👹")
        
    else:
        print("Jogador 1 (VOCÊ) venceu! 🏆")
