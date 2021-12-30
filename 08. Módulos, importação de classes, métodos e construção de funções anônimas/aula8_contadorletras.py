# MÉTODO QUE CONTAS PALAVRAS

def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

if _name_ == '_main_':
    lista = ['cachorro', 'gato']
    print(contador_letras(lista))