from util import limpa_tela
from personagem import personagem_ficha, mostrar_personagem, rolagem_ataque_personagem, calcular_dano_personagem, curar_personagem
from oponente import goblin_ficha, rolagem_ataque_goblin, calcular_dano_goblin

def batalha_goblin_nv1(personagem_ficha):
    limpa_tela()
    pocoes_usadas = 0
    mostrar_personagem(personagem_ficha)
    print('=== VS ===')
    print('Goblin'.center(10))
    print(f'Vida: {goblin_ficha["vida_atual"]}'.center(10))
    input('\nCOMEÇAR BATALHA?')
    while(True):
        terminar_combate = False
        limpa_tela()
        print('Goblin ataca:')
        print(f'Vida: {goblin_ficha["vida_atual"]}')
        resultado_goblin = rolagem_ataque_goblin(goblin_ficha)
        if (resultado_goblin >= personagem_ficha["esquiva"]):
            print('\nGoblin te acerta!')
            dano_goblin = calcular_dano_goblin(goblin_ficha, resultado_goblin) - personagem_ficha["defesa"]
            if (dano_goblin < 0):
                dano_goblin = 0
            else:
                pass
            personagem_ficha["vida_atual"] -= dano_goblin
        else:
            print('\nGoblin erra!')

        if (personagem_ficha["vida_atual"] <= 0):
            print('\nVocê morreu!')
            personagem_ficha["vida_atual"] = personagem_ficha["vida_max"]
            goblin_ficha["vida_atual"] = goblin_ficha["vida_max"]
            pocoes_usadas += personagem_ficha["pocao_cura"]
            pocoes_usadas = 0
            input('\nRECOMEÇAR BATALHA?')
        else:
            print(f'\nSua vida: {personagem_ficha["vida_atual"]} / {personagem_ficha["vida_max"]}')
            input('\nCONTINUAR?')

        while(True):
            limpa_tela()
            terminar_rodada = False
            print(f'{personagem_ficha["nome"]} ataca:')
            mostrar_personagem(personagem_ficha)
            print('\n=== ESCOLHA AÇÃO ===')
            print('[1] Atacar')
            print('[2] Curar')
            menu_personagem = int(input('Digite: '))

            if (menu_personagem == 1):
                limpa_tela()
                while(True):
                    print(f'Ataque: {personagem_ficha["dano"]} de dano')
                    print('\nQuer mesmo fazer isso?')
                    print('[1] Sim')
                    print('[2] Não')
                    certeza_atacar_personagem = int(input('Digite: '))
                    if (certeza_atacar_personagem == 1):
                        resultado_personagem = rolagem_ataque_personagem(personagem_ficha)
                        if (resultado_personagem >= goblin_ficha["esquiva"]):
                            print(f'\n{personagem_ficha["nome"]} acerta o ataque!')
                            dano_personagem = calcular_dano_personagem(personagem_ficha, resultado_personagem) - goblin_ficha["defesa"]
                            if (dano_personagem < 0):
                                dano_personagem = 0
                            else:
                                pass
                            goblin_ficha["vida_atual"] -= dano_personagem
                            input('\nPRÓXIMA RODADA?')
                            terminar_rodada = True
                            break
                        else:
                            print(f'\n{personagem_ficha["nome"]} errou o ataque!')
                            input('\nPRÓXIMA RODADA?')
                            terminar_rodada = True
                            break
                    elif (certeza_atacar_personagem == 2):
                        break
                    else:
                        print('\nAlgo deu errado!')
                        print('Tente novamente')

            elif (menu_personagem == 2):
                if (personagem_ficha["pocao_cura"] == 0):
                    print('\nVocê não tem poções de cura!')
                    input('\nVOLTAR?')
                else:
                    while(True):
                        print('\nQuer mesmo fazer isso?')
                        print('[1] Sim')
                        print('[2] Não')
                        certeza_curar_personagem = int(input('Digite: '))
                        if (certeza_curar_personagem == 1):
                            curar_personagem(personagem_ficha)
                            pocoes_usadas += 1
                            input('\nPRÓXIMA RODADA?')
                            terminar_rodada = True
                            break
                        elif (certeza_curar_personagem == 2):
                            break
                        else:
                            print('\nAlgo deu errado!')
                            print('Tente novamente')

            else:
                print('\nAlgo deu errado!')
                print('Tente novamente') 

            if (goblin_ficha["vida_atual"] <= 0):
                terminar_combate = True
            else:
                pass

            if (terminar_rodada == True):
                break
            else:
                pass

        if (terminar_combate == True):
            limpa_tela()
            print('=' * 30)
            print('!VOCÊ VENCEU!'.center(30))
            print(f'!Você ganhou {goblin_ficha["recompensa"]} moedas!'.center(30))
            print('=' * 30)
            personagem_ficha["moedas"] += goblin_ficha["recompensa"]
            personagem_ficha["vida_atual"] = personagem_ficha["vida_max"]
            goblin_ficha["vida_atual"] = goblin_ficha["vida_max"]
            input('\nCONTINUAR?')
            break
        else:
            pass