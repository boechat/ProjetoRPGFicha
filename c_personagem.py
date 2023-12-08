import verifica_tam as vt

def criar_personagem():
    personagens = []  # Lista para armazenar os dicionários de cada personagem

    while True:
        new_char = {}  # Dicionário para armazenar os dados do novo personagem

        nome_jogador = input("Digite o Nome do Jogador: ")
        nickname = input("Digite o Nome do Herói: ").capitalize()
        nome = input("Digite o Nome Civil do Personagem: ")
        sobrenome = input("Digite o Sobrenome Civil do Personagem: ")
        afiliacao = input("Digite a Affiliation do Personagem: ")
        size = input("Escolha o Tamanho:  \n"
                     "0 - Fine\n"
                     "1 - Diminutive\n"
                     "2 - Tiny\n"
                     "3 - Small\n"
                     "4 - Medium\n"
                     "5 - Large\n"
                     "6 - Huge\n"
                     "7 - Gargantuan\n"
                     "8 - Colossal\n")
        tam = vt.size_esc(size)
        tam_name = vt.name_size(tam)

        new_char['Alt. Identity'] = nickname.capitalize()
        new_char['Nome'] = nome.capitalize()
        new_char['Sobrenome'] = sobrenome.capitalize()
        new_char['Affiliation'] = afiliacao.capitalize()
        new_char['Size'] = tam_name.capitalize()
        new_char['Jogador'] = nome_jogador.capitalize()

        personagens.append(new_char)  # Adiciona o dicionário do personagem à lista

        fim_game = input('Deseja acabar com o preenchimento? (Y/N): ')
        if fim_game.upper() == 'Y':
            break

    return personagens
