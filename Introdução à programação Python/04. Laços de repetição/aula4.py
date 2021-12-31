# FOR

    # PROGRAMA QUE VERIFICA SE O NÚMERO É PRIMO

# a = int(input('Entre com um valor: '))

# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div = div + 1
        
# if div == 2:
#     print('Número {} é primo'. format(a))
# else:
#     print('número {} não é primo'.format(a))


    # LAÇO DENTRO DE LAÇO

# a = int(input('Entre com um valor: '))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div = div + 1

#     if div == 2:
#         print(num)

  
    # WHILE - ESTRUTURA DE REPETIÇÃO

# nota = int(input('Entre com a nota: '))
# while nota > 10:
#     nota = int(input('Nota inválida. Entre com a nota: '))


    # PROGRAMA PARA FAZER A MÉDIA DA NOTA DO ALUNO, VALIDANDO SE A NOTA FOI DIGITADA CORRETAMENTE:

a = int(input('primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou errado. Segundo bimestre: '))
c = int(input('terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou errado. Terceiro bimestre: '))
d = int(input('quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou errado. Quarto bimestre: '))

media = (a + b + c + d) / 4
print('Média: {}'.format(media))

