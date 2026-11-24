from util import limpa_tela
from guerreiro import guerreiro_ficha, mostrar_guerreiro, rolagem_ataque_guerreiro, calcular_dano_guerreiro, curar_guerreiro
from oponente import goblin_ficha, rolagem_ataque_goblin, calcular_dano_goblin
#fazer sistema de habilidade e de ganhar moedas
def guerreiro_nv1():
    limpa_tela()
    pocoes_usadas = 0
    mostrar_guerreiro(guerreiro_ficha)
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
        if (resultado_goblin >= guerreiro_ficha["esquiva"]):
            print('\nGoblin te acerta!')
            dano_goblin = calcular_dano_goblin(goblin_ficha, resultado_goblin) - guerreiro_ficha["defesa"]
            guerreiro_ficha["vida_atual"] -= dano_goblin
        else:
            print('\nGoblin erra!')

        if (guerreiro_ficha["vida_atual"] <= 0):
            print('\nVocê morreu!')
            guerreiro_ficha["vida_atual"] = guerreiro_ficha["vida_max"]
            goblin_ficha["vida_atual"] = goblin_ficha["vida_max"]
            pocoes_usadas += guerreiro_ficha["pocao_cura"]
            pocoes_usadas = 0
            input('\nRECOMEÇAR BATALHA?')
        else:
            print(f'\nSua vida: {guerreiro_ficha["vida_atual"]} / {guerreiro_ficha["vida_max"]}')
            input('\nCONTINUAR?')

        while(True):
            limpa_tela()
            terminar_rodada = False
            print('Guerreiro ataca:')
            mostrar_guerreiro(guerreiro_ficha)
            print('\n=== ESCOLHA AÇÃO ===')
            print('[1] Atacar')
            print('[2] Curar')
            print('[3] Habilidade')
            menu_guerreiro = int(input('Digite: '))

            if (menu_guerreiro == 1):
                limpa_tela()
                while(True):
                    print(f'Ataque com a espada: {guerreiro_ficha["espada"]} de dano')
                    print('\nQuer mesmo fazer isso?')
                    print('[1] Sim')
                    print('[2] Não')
                    certeza_atacar_guerreiro = int(input('Digite: '))
                    if (certeza_atacar_guerreiro == 1):
                        resultado_guerreiro = rolagem_ataque_guerreiro(guerreiro_ficha)
                        if (resultado_guerreiro >= goblin_ficha["esquiva"]):
                            print('\nGuerreiro acerta o ataque!')
                            dano_guerreiro = calcular_dano_guerreiro(guerreiro_ficha, resultado_guerreiro) - goblin_ficha["defesa"]
                            goblin_ficha["vida_atual"] -= dano_guerreiro
                            input('\nPRÓXIMA RODADA?')
                            terminar_rodada = True
                            break
                        else:
                            print('\nGuerreiro errou o ataque!')
                            input('\nPRÓXIMA RODADA?')
                            terminar_rodada = True
                            break
                    elif (certeza_atacar_guerreiro == 2):
                        break
                    else:
                        print('\nAlgo deu errado!')
                        print('Tente novamente')

            elif (menu_guerreiro == 2):
                if (guerreiro_ficha["pocao_cura"] == 0):
                    print('\nVocê não tem poções de cura!')
                    input('\nVOLTAR?')
                else:
                    while(True):
                        print('\nQuer mesmo fazer isso?')
                        print('[1] Sim')
                        print('[2] Não')
                        certeza_curar_guerreiro = int(input('Digite: '))
                        if (certeza_curar_guerreiro == 1):
                            curar_guerreiro(guerreiro_ficha)
                            pocoes_usadas += 1
                            input('\nPRÓXIMA RODADA?')
                            terminar_rodada = True
                            break
                        elif (certeza_curar_guerreiro == 2):
                            break
                        else:
                            print('\nAlgo deu errado!')
                            print('Tente novamente')

            elif (menu_guerreiro == 3):
                pass 

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
            print('=' * 30)
            goblin_ficha["vida_atual"] = goblin_ficha["vida_max"]
            input('\nCONTINUAR?')
            break
        else:
            pass