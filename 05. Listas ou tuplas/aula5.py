# LISTA É MUTÁVEL A TUPLA É IMUTÁVEL

lista = [12, 10, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

lista_animal[0] = 'macaco'
print(lista_animal)

tupla = (1, 10, 12, 14)
print(len(tupla)) #CONTADOR

    #CONVERTENDO LISTA PARA TUPLA

tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)


#print(min(lista_animal))

# nova_lista = lista_animal * 3
# print(nova_lista)

    #   ordenando lista

# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista_animal.reverse()
# print(lista_animal)

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)

    # VERIFICA SE JÁ TEM UM ELEMENTO NA LISTA

# if 'lobo' in lista_animal:
#     print('existe um gato na lista')
# else:
#     print('não existe na lista, mas será incluído')
#     lista_animal.append('lobo')
#     print(lista_animal)

# lista_animal.pop() #tira o ultimo elemento da lista (POP)
# print(lista_animal)

# lista_animal.remove('elefante')
# print(lista_animal)