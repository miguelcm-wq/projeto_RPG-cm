assassino_ficha = {
"vida_max": 80,
"vida_atual": 80,
"ataque": 5,
"defesa": 3,
"esquiva": 12,
}

def mostrar_assassino(assassino_ficha):
    print('=' * 30)
    print('Assassino'.center(30))
    print(f'vida: {assassino_ficha["vida_atual"]} / {assassino_ficha["vida_max"]}')
    print(f'ataque: {assassino_ficha["ataque"]}')
    print(f'defesa: {assassino_ficha["defesa"]}')
    print(f'esquiva: {assassino_ficha["esquiva"]}')
    print('=' * 30)