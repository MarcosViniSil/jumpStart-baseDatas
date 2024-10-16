import yfinance as yf 
from datetime import datetime, timedelta
from API.consumeGoogleSheets import *
from datetime import datetime
from dataBase.insertDatas import *
from dataBase.updateDatas import *

dateActual = datetime.now()
dateBeforeActual = dateActual - timedelta(days=1)

dateFormated = dateBeforeActual.strftime('%Y-%m-%d')

def fetchInformationAction(dataBase,action):

    data = yf.download(action, start=dateFormated, progress=False)
    if len(data.values) != 0:
        date = getDateActual()
        open = data.values[0][0].round(4)
        high = data.values[0][1].round(4)
        low = data.values[0][2].round(4)
        close = data.values[0][3].round(4)
        volume = data.values[0][5].round(0)
        try:
            insertDatasActions(dataBase,action,date,open,high,low,close,volume)
        except:
            # TODO - handle the exception
            print("erro")
    else:    
        # TODO - handle the case when len(data.values) is 0
        manipluationErrorGetCryptos(action,"400")
    
def fetchAllInformationActions(dataBase):
    actions = ["PETR4.SA","BBAS3.SA","ITSA4.SA","TRPL4.SA","VALE3.SA","CMIG4.SA","SANB11.SA","USIM5.SA","ABEV3.SA","MGLU3.SA"]
    #
    for action in actions:
        fetchInformationAction(dataBase,action)
    try:
        manipulationAcoes(dataBase)
    except Exception as e:
        # TODO - handle the exception
        print("Erro ao manipular acoes, verificação de exclusão:", str(e))


def manipluationErrorGetCryptos(crypto,status):
     datas = {
            "Data": "",
            "Crypto": "Crypto: "+crypto,
            "Status": status
             }
     insertErrorGoogleSheets(datas) 

def getDateActual():
    dateActualFormated = dateActual.strftime('%Y-%m-%d')
    return dateActualFormated

# se len(data_vale.values) ==2 sinal que possui dados das ações do dia atual, se len() ==1 informações do dia anterior

# data.values[0][0] => open
# data.values[0][1] => high
# data.values[0][2] => low
# data.values[0][3] => close
# data.values[0][5] => volume
#print("name-action",action,"Open: ",data.values[1][0].round(2),"High: ",data.values[1][1].round(2),"\t ","LOW: ",data.values[1][2].round(2),"\t ","Close: ",data.values[1][3].round(2),"\t ","\t ","Volume: ",data.values[1][5].round(0))
#print("name-action",action,"Open: ",data.values[0][0].round(2),"High: ",data.values[0][1].round(2),"\t ","LOW: ",data.values[0][2].round(2),"\t ","Close: ",data.values[0][3].round(2),"\t ","\t ","Volume: ",data.values[0][5].round(0))