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
    input('Rolar ataque?')
    import random
    numero_ataque = random.randint(1, 20)
    if(numero_ataque == 20):
        print('\n=== CRÍTICO ===')
        return 100
    else:
        print(f'\nAtaque: {numero_ataque} + {guerreiro_ficha["ataque"]} = {numero_ataque + guerreiro_ficha["ataque"]}')
        return numero_ataque + guerreiro_ficha["ataque"]


#Tem que arrumar isso depois
def calcular_dano_guerreiro(guerreiro_ficha, rolagem_ataque_guerreiro):
    resultado = rolagem_ataque_guerreiro(guerreiro_ficha)
    if (resultado == 100):
        print(f'\nDano: {guerreiro_ficha["espada"] * 2}')
        return guerreiro_ficha["espada"] * 2
    else:
        print(f'Dano: {guerreiro_ficha["espada"]}')
        return guerreiro_ficha["espada"]