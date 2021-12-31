import requests

def retorna_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json'.format(cep))
    print(response.status_code)
    print(response.json()) # JSON É UM FORMATO DE DICIONÁRIO
    print(type(response.json()))
    dado_cep = response.json()
    print(dado_cep['logradouro'])
    print(dado_cep['uf'])
    return dado_cep

def retorna_dado_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dado_pokemon = response.json()
    return dado_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    response = retorna_response('https://globallabs.academy/')
    print(response)
    #retorna_cep('88106710')
    #dado_pokemon = retorna_dado_pokemon('pikachu')
    #print(dado_pokemon['sprites']['front_shiny']) # TRÁS O LINK DA IMG DO POKEMON
