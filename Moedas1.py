# pegando variações de cotação
# para isso precisamos importar o requests e o json
# coins é a variavel que recebe o comando request e o get (o link da onde vem a intel)
# todo arquivo json precisa ser transformado (coins.json)
# para que possamos salvar arquivos diferentes precisamos usar o append, somente o write sobrescreve 
# onde json_str e a string recebe o dumps para que recebe a lista coins com a identação 6


import requests
import json

coins = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
coins = coins.json()

list_coins = []

list_coins.append(coins)

json_str = json.dumps(list_coins, indent=6)
with open ("moedas_2", "w") as arquivo: arquivo.write(json_str)

# price_real = coins['USDBRL']

# price_dolar = coins['EURBRL']

price_btc = coins['BTCBRL'] ['bid']

print(price_btc)


# with e uma opção na qual por mais que o programa não tenha o DIE com o with ele fecha sozinho
# open para abrir o arquivo (nome do arquivo, w e para escrever) que recebe arquivo
# arquivo sobrescreve o que tem na string json_str
# pegando alguns parametros do arquivo json, declaramos uma variavel e atribuimos a variavel com a lista
# entre conchetes declaramos os parametros 