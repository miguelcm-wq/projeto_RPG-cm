guerreiro_ficha = {
"vida_max": 100,
"vida_atual": 100,
"ataque": 3,
"defesa": 5,
"esquiva": 10,
}

def mostrar_guerreiro(guerreiro_ficha):
    print('=' * 30)
    print('Guerreiro'.center(30))
    print(f'vida: {guerreiro_ficha["vida_atual"]} / {guerreiro_ficha["vida_max"]}')
    print(f'ataque: {guerreiro_ficha["ataque"]}')
    print(f'defesa: {guerreiro_ficha["defesa"]}')
    print(f'esquiva: {guerreiro_ficha["esquiva"]}')
    print('=' * 30)