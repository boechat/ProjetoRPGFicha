personagens = []  # Lista para armazenar os dicionários de cada personagem

while True:
    new_char = {}  # Dicionário para armazenar os dados do novo personagem

    nome_jogador = input("Digite o Nome do Jogador: ")
    nome = input("Digite o Nome do Personagem: ")
    sobrenome = input("Digite o Sobrenome do Personagem: ")

    new_char['Nome'] = nome
    new_char['Sobrenome'] = sobrenome
    new_char['Jogador'] = nome_jogador

    atributos = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']

    for atributo in atributos:
        print(f'Entre com {atributo}')
        atrib = atributo[:3]
        base = input(f"Base {atributo}: ")
        misc = input("Misc: ")
        temp = input("Temp: ")

        atributo_atual = int(base) + int(misc) + int(temp)
        new_char[atributo] = atributo_atual
        new_char[atrib + '_base'] = base
        new_char[atrib + '_misc'] = misc
        new_char[atrib + '_temp'] = temp

        if atributo_atual > 10:
            att_mod = (atributo_atual - 10) // 2
        else:
            att_mod = 0
        new_char[atrib + '_mod'] = att_mod

        print(f"{atributo_atual} - {atributo}")
        print('Modificador : ',att_mod)

    personagens.append(new_char)  # Adiciona o dicionário do personagem à lista

    fim_game = input('Deseja acabar com o preenchimento? (Y/N): ')
    if fim_game.upper() == 'Y':
        break

