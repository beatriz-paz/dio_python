    # CRIANDO UM ARQUIVO

def escrever_arquivo(texto):
    diretorio = '09. Trabalhando com arquivos externos/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write('texto')
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write('texto')
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open('nome_arquino', 'r')
    texto = arquivo.read()
    print(texto)

if __name__ == '_main_':
    escrever_arquivo('Primeira linha.\n')
    #atualizar_arquivo('Segunda linha.\n')
