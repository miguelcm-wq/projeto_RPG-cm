personagem_ficha = {}

def mostrar_personagem(personagem_ficha):
    print('=' * 30)
    print(personagem_ficha["nome"].center(30))
    print(f'vida: {personagem_ficha["vida_atual"]} / {personagem_ficha["vida_max"]}')
    print(f'ataque: {personagem_ficha["ataque"]}')
    print(f'defesa: {personagem_ficha["defesa"]}')
    print(f'esquiva: {personagem_ficha["esquiva"]}')
    print('=' * 30)


def rolagem_ataque_personagem(personagem_ficha):
    input('\nRolar ataque?')
    import random
    numero_ataque = random.randint(1, 20)
    if(numero_ataque == 20):
        print('\n=== CRÍTICO ===')
        resultado_personagem = 100
    else:
        resultado_personagem = numero_ataque + personagem_ficha["ataque"]
        print(f'\nAtaque: {numero_ataque} + {personagem_ficha["ataque"]} = {resultado_personagem}')
    return resultado_personagem


def calcular_dano_personagem(personagem_ficha, resultado_personagem):
    if (resultado_personagem == 100):
        print(f'\nDano: {personagem_ficha["dano"] * 2}')
        dano_personagem = personagem_ficha["dano"] * 2
    else:
        print(f'\nDano: {personagem_ficha["dano"]}')
        dano_personagem = personagem_ficha["dano"]
    return dano_personagem


def curar_personagem(personagem_ficha):
    personagem_ficha["pocao_cura"] -= 1
    personagem_ficha["vida_atual"] += 30
    if (personagem_ficha["vida_atual"] >= personagem_ficha["vida_max"]):
        personagem_ficha["vida_max"] = personagem_ficha["vida_atual"]
        print(f'\nSua vida: {personagem_ficha["vida_atual"]}')
    else:
        pass
    print(f'\nSua vida: {personagem_ficha["vida_atual"]}')