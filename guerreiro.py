guerreiro_ficha = {
"vida_max": 100,
"vida_atual": 100,
"ataque": 3,
"defesa": 5,
"esquiva": 10,
"espada": 15,
"pocao_cura": 0
}


def mostrar_guerreiro(guerreiro_ficha):
    print('=' * 30)
    print('Guerreiro'.center(30))
    print(f'vida: {guerreiro_ficha["vida_atual"]} / {guerreiro_ficha["vida_max"]}')
    print(f'ataque: {guerreiro_ficha["ataque"]}')
    print(f'defesa: {guerreiro_ficha["defesa"]}')
    print(f'esquiva: {guerreiro_ficha["esquiva"]}')
    print('=' * 30)


def rolagem_ataque_guerreiro(guerreiro_ficha):
    input('\nRolar ataque?')
    import random
    numero_ataque = random.randint(1, 20)
    if(numero_ataque == 20):
        print('\n=== CRÍTICO ===')
        resultado_guerreiro = 100
    else:
        resultado_guerreiro = numero_ataque + guerreiro_ficha["ataque"]
        print(f'\nAtaque: {numero_ataque} + {guerreiro_ficha["ataque"]} = {resultado_guerreiro}')
    return resultado_guerreiro


def calcular_dano_guerreiro(guerreiro_ficha, resultado_guerreiro):
    if (resultado_guerreiro == 100):
        print(f'\nDano: {guerreiro_ficha["espada"] * 2}')
        return guerreiro_ficha["espada"] * 2
    else:
        print(f'\nDano: {guerreiro_ficha["espada"]}')
        return guerreiro_ficha["espada"]