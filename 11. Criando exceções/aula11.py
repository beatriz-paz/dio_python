# TRATAMENTO DE EXCEÇÃO/ERRO

lista = [1, 10]

try:
    numero = lista[1]
    divisao = 10 / 0
    #x = a

except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
except IndexError:
    print('Erro ao acessar indice invalida da lista')
except Exception as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))

else:
    print('Executa quando não ocorre exceção')

finally:
    print('Sempre executa, mesmo após o erro')

