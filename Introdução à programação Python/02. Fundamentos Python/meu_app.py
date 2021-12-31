# AULA 1 - VARIÁVEIS

# INTERAÇÃO COM O USUÁRIO
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
print(type(a))

# OPERADORES ARITMÉTICOS
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(resto)

# CONVERSÃO DE TIPO

print(type(soma))
soma = str(soma)
print(type(soma))

#EXEMPLO

print('soma: ' + str(soma))

print(type(divisao))
print(int(divisao))
print(divisao)

x = '1'
soma2 = int(x) + 1 #converter o tipo do X para não dar erro 
print(soma2)

# FORMAT CONSEGUE CONCATENAR INDEPENDENTE DO TIPO
# O \n é como se fosse o enter

print('Soma: {}. \nSubtração: {}. \nDivisão {}. \nResto {}' .format(soma, subtracao, divisao, resto)) 