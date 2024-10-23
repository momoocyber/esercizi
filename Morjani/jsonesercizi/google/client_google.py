import requests, json, sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import subprocess
from myjson import *


base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key="
google_api_key= "AIzaSyCGLj-V4R-4aa_QxPAlzZnL68mliZmLPeA"

api_url = base_url + google_api_key

def ComponiJsonPerImmagine(sImagePath):
    subprocess.run(["rm", "./image.jpg"])
    subprocess.run(["rm", "./request.json"])
    subprocess.run(["cp", sImagePath,"./image.jpg"])
    subprocess.run(["bash", "./creajsonpersf.sh"])


def EseguiOperazione(iOper, sServizio, dDatiToSend):
    try:
        if iOper == 1:
            response = requests.post(sServizio, json=dDatiToSend)
        if iOper == 2:
            response = requests.get(sServizio)
        if iOper == 3:
            response = requests.put(sServizio, json=dDatiToSend)
        if iOper == 4:
            response = requests.delete(sServizio, json=dDatiToSend)

        if response.status_code==200:
            print(response.json())
        else:
            print("Attenzione, errore " + str(response.status_code))
    except:
        print("Problemi di comunicazione con il server, riprova più tardi.")




print("Benvenuti nella mia generativa AI")


iFlag = 0
while iFlag==0:
    print("\nOperazioni disponibili:")
    print("1. Creare una favola")
    print("2. Rispondere ad una domanda")
    print("3. Rispondere a una domanda su un file img")
    print("4. Esci")


    try:
        iOper = int(input("Cosa vuoi fare? "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue


    if iOper == 1:
        sArgomento= input("Inserisci l'argomento della favola")
        
        jsonDataRequest={"contents": [{"parts":[{"text": sArgomento}]}]}
        #jsonDataRequest = ["contents"][0]["parts"][0]["text"]= sArgomento
        #EseguiOperazione(1, api_url, jsonDataRequest)
        response= requests.post(api_url, json=jsonDataRequest, verify= False)
        if response.status_code == 200:
            response = response.json()
            listaContenuti = response["candidates"][0]
            testoPrimaRisposta = listaContenuti["content"]["parts"][0]["text"]
            print(testoPrimaRisposta)    


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    elif iOper == 2:
        print("Richiesta dati cittadino")
        
    elif iOper == 3:
        sFile= input("inserisci il path completo del file che vuoi analizzare:")
        ComponiJsonPerImmagine(sFile)
        #sDomanada= input("inserisci la domanda:")
        dJsonRequest= JsonDeserialize("request.json")
        response=requests.post(api_url, json= dJsonRequest, verify=False)
        if response.status_code==200:
            print(response.json())
        
    
    elif iOper == 4:
        print("Buona giornata!")
        iFlag = 1

    else:
        print("Operazione non disponibile, riprova.")



