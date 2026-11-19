from guerreiro import guerreiro_ficha, rolagem_ataque_guerreiro, calcular_dano_guerreiro

while(True):
    resultado_guerreiro = rolagem_ataque_guerreiro(guerreiro_ficha)
    calcular_dano_guerreiro(guerreiro_ficha, resultado_guerreiro)