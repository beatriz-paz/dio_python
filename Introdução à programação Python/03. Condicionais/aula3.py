# CONDICIONAIS IF/ELSE/ELIF

    # PARA FAZER UMA COMPARAÇÃO, PRECISO CONVERTER O TIPO, PORT QUE O a E b JÁ VEM COMO STR

# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# if a > b and a > c:
#     print('O maior número é {}'.format(a))
# elif b> a and b > c:
#     print('O maior número é {}'.format(b))
# else:
#     print(('O maior número é {}'.format(c)))
#
# print('Final do Programa')

    # VERIFICANDO SE O NÚMERO É PAR:

# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or not resto_b > 0:
#     print('Foi digitado um Número é par')
# else:
#     print('Nenhum Número par foi digitado')

    # PROGRAMA PARA FAZER A MÉDIA DA NOTA DO ALUNO:

a = int(input('primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou errado. Segundo bimestre: '))
c = int(input('terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou errado. Terceiro bimestre: '))
d = int(input('quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou errado. Quarto bimestre: '))

media = (a + b + c + d) / 4
print('Média: {}'.format(media))

# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('Média: {}'.format(media))
# else:
#     print('Foi informado alguma nota errada')

