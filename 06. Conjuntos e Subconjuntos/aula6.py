    # CONJUNTO {}

# CONJUNTO = {1, 2, 3, 4, 4, 2}
# CONJUNTO.add(5)
# CONJUNTO.discard(2)
# print(CONJUNTO)

CONJUNTO = {1, 2, 3, 4, 5}
CONJUNTO2 = {5, 6, 7, 8}

    # UNIÃO DE CONJUNTO:
CONJUNTO_UNIAO = CONJUNTO.union(CONJUNTO2)
print('União: {}'.format(CONJUNTO_UNIAO))

    # INTERSECÇÃO DE CONJUNTOS:
CONJUNTO_INTERSECCAO = CONJUNTO.intersection(CONJUNTO2)
print('Intersecção: {}'.format(CONJUNTO_INTERSECCAO))

    # DIFERENÇA DE CONJUNTO:
CONJUNTO_DIFERENCA1 = CONJUNTO.difference(CONJUNTO2)
CONJUNTO_DIFERENCA2 = CONJUNTO2.difference(CONJUNTO)
print('Diferença entre 1 e 2: {}'.format(CONJUNTO_DIFERENCA1))
print('Diferença entre 2 e 1: {}'.format(CONJUNTO_DIFERENCA2))

    # DIFERENÇA SIMÉTRICA:
CONJUNTO_SIMETRICA = CONJUNTO.symmetric_difference(CONJUNTO2)
print('Diferença simétrica: {}'.format(CONJUNTO_SIMETRICA))

    # PERTINÊNCIA - SUBCONJUNTO

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}

conjunto_subconj = conjunto_a.issubset(conjunto_b)
print('A é subconjunto de B: {}'.format(conjunto_subconj))

CONJUNTO_superset = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A: {}'.format(CONJUNTO_superset))

    # CONVERTENDO LISTA PARA CONJUNTO

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
conjunto_animal = set(lista)
print(conjunto_animal)

lista_animal = list(conjunto_animal)
print(lista_animal)