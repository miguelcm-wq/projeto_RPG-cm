from util import limpa_tela
from guerreiro import guerreiro_ficha, mostrar_guerreiro
from arqueiro import arqueiro_ficha, mostrar_arqueiro
from assassino import assassino_ficha, mostrar_assassino
from mago import mago_ficha, mostrar_mago

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
                pass
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
