def criar_atributo(nome_atributo, base, misc, temp):
    novo_atributo = {}  # Dicionário para armazenar os dados do novo atributo

    atributo_atual = int(base) + int(misc) + int(temp)
    novo_atributo['nome'] = nome_atributo
    novo_atributo['valor'] = atributo_atual
    novo_atributo['base'] = base
    novo_atributo['misc'] = misc
    novo_atributo['temp'] = temp

    if atributo_atual > 10:
        att_mod = (atributo_atual - 10) // 2
    else:
        att_mod = 0
    novo_atributo['modificador'] = att_mod

    print(f"{atributo_atual} - {nome_atributo}")
    print(att_mod)

    return novo_atributo

