
class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True: # O WHILE, ENQUANDO O RESULTADO FOR VERDADEIRO ELE FICA EXECUTANDO

    try:
        x = int(input('Entre com um número de 0 a 10: '))
        print(x)

        if x > 10: # COMANDO RAISE FORÇA UMA EXCEÇÃO
            raise InputError('Nota não pode ser maior que 10')
        else x < 0:
            raise InputError('Nota não pode ser menor que 0')
        break # O BREAK FORÇA SAIR DO WHILE, QUANDO FOR DIGITADO UM VALOR VERDADEIRO

    except ValueError:
        print('Valor inválido. Deve-se digitar apenas número')
    except InputError as ex:
        print(ex)   
