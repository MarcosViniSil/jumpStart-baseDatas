from api.consumeApi import *
from api.consumeGoogleSheets import *
from datetime import datetime

def cripto(crypto):

    response = getApiCrypto(crypto)


    if response.status_code == 200:
        resp = response.json()
        if resp != []:
            print("------------------ \n")
            high = round(float(resp[0]['high']),4)
            low = round(float(resp[0]['low']),4)
            vol = round(float(resp[0]['vol']),4)
            last = round(float(resp[0]['last']),4)
            sell = round(float(resp[0]['sell']),4)
            buy = round(float(resp[0]['buy']),4)
            date = resp[0]['date']
            open = round(float(resp[0]['open']),4)
        else:
            dateActual = datetime.now()
            dados = {
            "Data": dateActual,
            "Ativo": f"Crypto: {crypto}",
            "Status": "400"
            }
            insertDatasCoins(dados)
    else:
            dateActual = datetime.now()
            dados = {
            "Data": dateActual,
            "Crypto": "Crypto: "+crypto,
            "Status": response.status_code
            }
            insertDatasCoins(dados)    
    #print("coin: ",crypto,"high :",high,"low :",low,"vol :",vol,"last :",last,"buy :",buy,"sell :",sell,"date :",date,"open :",open)

def getAndPrintAllCryptos():
    cryptos = ["BTC","LTC","ETH","UIO","XRP","BCH","USDT","LINK","DOGE","ADA","EOS","XLM","CHZ","AXS"]
    index =1
    for crypto in cryptos:
        index +=1
        print("--------Crypto-------")
        cripto(crypto)
        print("--------Crypto-------")