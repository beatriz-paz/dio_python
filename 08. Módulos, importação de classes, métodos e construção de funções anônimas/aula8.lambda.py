# LAMBDA É UMA FUNÇÃO ANÔNIMA

contador_letras = lambda lista: [len(x) for x in lista]
lista_animal = ['cachorro', 'gato', 'elefante']

print(contador_letras(lista_animal))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

print(soma(5, 10))
print(subtracao(5, 10))

    # DICIONÁRIO

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}

print(type(calculadora))
soma = calculadora['soma']
multiplicacao = calculadora['multiplicacao']
print('A soma é: {}'.format(soma(10, 5)))
print('A multiplicação é: {}'.format(multiplicacao(10, 2)))