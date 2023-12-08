import c_personagem as cp,c_atributos as ca

# Criar Personagem
lista_personagens = cp.criar_personagem()
print("Lista de Personagens:")
for personagem in lista_personagens:
    print(personagem)

# Preencher atributo
'''
ca.atributos = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']

for atributo in ca.atributos:
    print(f'Entre com {atributo}')
    atrib = atributo[:3]
    base = input(f"Base {atributo}: ")
    misc = input("Misc: ")
    temp = input("Temp: ")

    atributo_criado = ca.criar_atributo(atributo, base, misc, temp)
    print(atributo_criado)  # Aqui você pode usar ou armazenar os atributos criados conforme necessário
'''