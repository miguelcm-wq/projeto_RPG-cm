arqueiro_ficha = {
    "vida_max": 60, 
    "vida_atual": 60, 
    "ataque": 3, 
    "defesa": 2, 
    "esquiva": 16
    }

def mostrar_arqueiro(arqueiro_ficha):
    print('=' * 30)
    print('Arqueiro'.center(30))
    print(f'vida: {arqueiro_ficha["vida_atual"]} / {arqueiro_ficha["vida_max"]}')
    print(f'ataque: {arqueiro_ficha["ataque"]}')
    print(f'defesa: {arqueiro_ficha["defesa"]}')
    print(f'esquiva: {arqueiro_ficha["esquiva"]}')
    print('=' * 30)