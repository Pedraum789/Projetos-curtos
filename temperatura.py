import requests
import json

iTOKEN = "c359895b284cc5821769dd22281582b8"
iTIPOCONSULTA = 1
#http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=São Paulo&state=SP&token=your-app-token

if iTIPOCONSULTA == 1:
    iCITY = "Salvador"
    iURL = "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=" + iCITY + "&token=" + iTOKEN
    iRESPONSE = requests.get(iURL)
    iRETORNO_REQ = json.loads(iRESPONSE.text)
    for chave in iRETORNO_REQ:
        id = chave['id']
        if chave["name"] == iCITY:
            name = chave["name"]
            break
    
    iURL = "http://apiadvisor.climatempo.com.br/api-manager/user-token/"+ iTOKEN +"/locales"
    payload = "localeId[]=" + str(id)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    iRESPONSE = requests.put(iURL, headers=headers, data=payload)

    iURL = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/"+ str(id) +"/current?token=" + str(iTOKEN)
    iRESPONSE = requests.get(iURL)
    iRETORNO_REQ = json.loads(iRESPONSE.text)
    print("Cidade: {}\n".format(iRETORNO_REQ["name"]))
    print("Temperatura: {} graus".format(iRETORNO_REQ["data"]["temperature"]))