import requests
import json

all = {"Estados Unidos":"USD", "Europa":"EUR", "Bitcoin":"BTC", "Canada":"CAD", "Argentina":"ARS"}

def inicio():
    print("Opções: \n")
    for i in all:
        print(i)

    entrada = input("Digite o pais que deseja converter: \n")
    lock = 0
    for i in all:
        if entrada == i:
            lock = 1
            break
    if lock == 0:
        return 0
    
    valor = input("Digite o valor que deseja converter: \n")
    if not valor.isnumeric:
        return 0
    valor = float(valor)
    url = "https://economia.awesomeapi.com.br/last/" + all[entrada] + "-BRL"
    
    response = requests.get(url)
    resposta = json.loads(response.text)
    conversao(entrada, valor, resposta)

def conversao(entrada, valor, resposta):
    conv = valor*((float(resposta[all[entrada] + "BRL"]["high"]) + float(resposta[all[entrada] + "BRL"]["low"])) / 2)

    print("Convertido de: R${:.2f} para: {} {:.2f}\n\n".format(valor, all[entrada], conv))
    #print(resposta)


if __name__ == "__main__":
    while True:
        inicio()