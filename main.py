from util import limpa_tela
import time
from guerreiro import guerreiro_ficha, mostrar_guerreiro
from arqueiro import arqueiro_ficha, mostrar_arqueiro
from assassino import assassino_ficha, mostrar_assassino
from mago import mago_ficha, mostrar_mago
from oponente import goblin_ficha, rolagem_ataque_goblin, calcular_dano_goblin

while(True):
    terminar_jogo = False
    limpa_tela()
    print('=' * 30)
    print('JOGO RPG'.center(30))
    print('=' * 30)
    print('\n=== ESCOLHA SEU PERSONAGEM ===')
    print('\n[1] Guerreiro')
    print('[2] Arqueiro')
    print('[3] Assassino')
    print('[4] Mago')
    escolha_de_personagem = int(input('Digite: '))


    if(escolha_de_personagem == 1):
        limpa_tela()
        mostrar_guerreiro(guerreiro_ficha)
        while(True):
            print('\nVocê quer mesmo jogar de Guerreiro?')
            print('[1] Sim')
            print('[2] Não')
            certeza_de_guerreiro = int(input('Digite: '))

            if(certeza_de_guerreiro == 1):
                limpa_tela()
                
                texto = 'Você é um grande Guerreiro em uma vila isolada dos mapas, \nDaqueles Guerreiros que não falham, apenas o melhor do reino, \nEntão o Rei um dia te chama até seu castelo.'
                for letra in texto:
                    print(letra, end="", flush=True)
                    time.sleep(0.05)

                time.sleep(0.3)

                print('\n')
                texto = '\n\033[1mRei:\033[0m Meu grande Guerreiro, o rei esqueleto da cidade amaldiçoada \nestá ameaçando nossas vendas de mercadoria, isso não pode acontecer! \nVá até lá e o derrote com toda a sua bravura!'
                for letra in texto:
                    print(letra, end="", flush=True)
                    time.sleep(0.05)

                time.sleep(0.3)

                print('\n')
                texto = '\n\033[1mGuerreiro:\033[0m Sim meu rei, destruirei todo aquele reino!'
                for letra in texto:
                    print(letra, end="", flush=True)
                    time.sleep(0.05)

                time.sleep(0.3)

                print('\n')
                texto = '\nEntão o grande Guerreiro vai até o encontro do castelo do rei esqueleto, \naté que no caminho um goblin pula do arbusto para te atacar.'
                for letra in texto:
                    print(letra, end="", flush=True)
                    time.sleep(0.05)

                time.sleep(0.3)

                print('\n')
                input('\nCONTINUAR?')
                limpa_tela()

                mostrar_guerreiro(guerreiro_ficha)
                print('=== VS ===')
                print('Goblin'.center(10))
                input('\nCOMEÇAR BATALHA?')
                while(True):
                    limpa_tela()
                    print('Goblin ataca:')
                    resultado_goblin = rolagem_ataque_goblin(goblin_ficha)
                    if (resultado_goblin >= guerreiro_ficha["esquiva"]):
                        print('\nGoblin te acerta!')
                        dano_goblin = calcular_dano_goblin(goblin_ficha, resultado_goblin)
                        guerreiro_ficha["vida_atual"] -= dano_goblin
                    else:
                        print('\nGoblin erra!')

                    if(guerreiro_ficha["vida_atual"] <= 0):
                        print('\nVocê morreu!')
                        guerreiro_ficha["vida_atual"] = guerreiro_ficha["vida_max"]
                        goblin_ficha["vida_atual"] = goblin_ficha["vida_max"]
                        input('\nRECOMEÇAR BATALHA?')
                    else:
                        print(f'\nSua vida: {guerreiro_ficha["vida_atual"]} / {guerreiro_ficha["vida_max"]}')
                        input('\nCONTINUAR?')

                    limpa_tela()
                    print('Guerreiro ataca:')
                    mostrar_guerreiro(guerreiro_ficha)
                    #continuar daqui
                        
                terminar_jogo = True
                break

            elif(certeza_de_guerreiro == 2):
                break

            else:
                print('Algo deu errado!')
                print('Tente novamente')

        if(terminar_jogo == True):
            break
        else:
            pass


    elif(escolha_de_personagem == 2):
        limpa_tela()
        mostrar_arqueiro(arqueiro_ficha)
        while(True):
            print('\nVocê quer mesmo jogar de Arqueiro?')
            print('[1] Sim')
            print('[2] Não')
            certeza_de_arqueiro = int(input('Digite: '))
        
            if(certeza_de_arqueiro == 1):
                
                pass
                terminar_jogo = True
                break
        
            elif(certeza_de_arqueiro == 2):
                break
        
            else:
                print('\nAlgo deu errado!')
                print('Tente novamente')
        
        if(terminar_jogo == True):
            break
        else:
            pass


    elif(escolha_de_personagem == 3):
        limpa_tela()
        mostrar_assassino(assassino_ficha)
        while(True):
            print('\nVocê quer mesmo jogar de Assassino?')
            print('[1] Sim')
            print('[2] Não')
            certeza_de_assassino = int(input('Digite: '))
        
            if(certeza_de_assassino == 1):
                pass
                terminar_jogo = True
                break
        
            elif(certeza_de_assassino == 2):
                break
        
            else:
                print('Algo deu errado!')
                print('Tente novamente')
        
        if(terminar_jogo == True):
            break
        else:
            pass


    elif(escolha_de_personagem == 4):
        limpa_tela()
        mostrar_mago(mago_ficha)
        while(True):
            print('\nVocê quer mesmo jogar de Mago?')
            print('[1] Sim')
            print('[2] Não')
            certeza_de_mago = int(input('Digite: '))
        
            if(certeza_de_mago == 1):
                pass
                terminar_jogo = True
                break
        
            elif(certeza_de_mago == 2):
                break
        
            else:
                print('Algo deu errado!')
                print('Tente novamente')
        
        if(terminar_jogo == True):
            break
        else:
            pass


    else:
        print('\nAlgo deu errado!')
        print('Tente novamente')
