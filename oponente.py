goblin_ficha = {
"vida_max": 25,
"vida_atual": 25,
"ataque": 2,
"defesa": 1,
"esquiva": 8,
"dano": 10
}

def rolagem_ataque_goblin(goblin_ficha):
    import random
    numero_ataque = random.randint(1, 20)
    if(numero_ataque == 20):
        print('\n=== CRÍTICO ===')
        resultado_goblin = 100
    else:
        resultado_goblin = numero_ataque + goblin_ficha["ataque"]
    return resultado_goblin

def calcular_dano_goblin(goblin_ficha, resultado_goblin):
    if (resultado_goblin == 100):
        print(f'\nDano: {goblin_ficha["dano"] * 2}')
        dano_goblin = goblin_ficha["dano"] * 2
    else:
        print(f'\nDano: {goblin_ficha["dano"]}')
        dano_goblin = goblin_ficha["dano"]
    return dano_goblin