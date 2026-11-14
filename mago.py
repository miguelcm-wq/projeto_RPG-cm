mago_ficha = {
"vida_max": 40,
"vida_atual": 40,
"ataque": 7,
"defesa": 0,
"esquiva": 14,
}

def mostrar_mago(mago_ficha):
    print('=' * 30)
    print('Mago'.center(30))
    print(f'vida: {mago_ficha["vida_atual"]} / {mago_ficha["vida_max"]}')
    print(f'ataque: {mago_ficha["ataque"]}')
    print(f'defesa: {mago_ficha["defesa"]}')
    print(f'esquiva: {mago_ficha["esquiva"]}')
    print('=' * 30)