# Pega o valor de 1 a 8 para entrar com tamanho
def size_esc(escolha):
    if escolha.isdigit():
        valor_escolhido = int(escolha)
        if 0 <= valor_escolhido <= 8:
            print("Valor escolhido:", valor_escolhido)
        else:
            print("Por favor, escolha um valor dentro do intervalo de 0 a 8.")
        return valor_escolhido
    else:
        print("Entrada inválida. Por favor, insira um número de 0 a 8.")

# Pega o valor de 1 a 8 e checa no dicionario o nome, retornando
def name_size(tam):
    nomes_tamanho = {
        0: 'Fine',
        1: 'Diminutive',
        2: 'Tiny',
        3: 'Small',
        4: 'Medium',
        5: 'Large',
        6: 'Huge',
        7: 'Gargantuan',
        8: 'Colossal'
    }
    return(nomes_tamanho[tam])

