
import random

def Posizioni(posTart:int,posLepre:int)->list:
    lunghezza_lista=70
    percorso:list[int]=["_"]*lunghezza_lista
    percorso[posLepre-1]="H"
    percorso[posTart-1]="T"
    if posLepre==posTart:
        percorso[posLepre-1]="OUCH!!!"
    return percorso
def Tartaruga(i:int)->str:
    mossa=""
    if 1 <= i <= 5:
        mossa="Passo veloce"
        posTart=3
    elif 6 <= i <= 7:
        mossa="Scivolata"
        posTart=6
    elif 8 <= i <= 10:
        mossa="Passo lento"

    return mossa

def Lepre(j:int)->str:
    mossa=""
    if 1 <= j <= 2:
        mossa="Riposo"
    elif 3 <= j <= 4:
        mossa="Grande balzo"
    elif j == 5:
        mossa="Grande scivolata"
    elif 6 <= j <= 8:
        mossa="Piccolo balzo"
    elif 9 <= j <= 10:
        mossa="Piccola scivolata"
    return mossa

posLepre=1
posTart=1
conta=0
energiaTart=100
energiaLepre=100    
while posTart != 70 and posLepre != 70:
    i=random.randint(1, 10)
    j=random.randint(1, 10)
    a=random.randint(1, 2)
    tempo=""
    if conta==10:
        if a==1:
            tempo="Soleggiato"
        elif a==2:
            tempo="Piovoso"
        conta=0
    print(f"Tartaruga = {Tartaruga(i)}")
    print(f"Lepre = {Lepre(j)}")
    if Tartaruga(i)== "Passo veloce":
        if energiaTart>5:
            posTart=posTart+3
            energiaTart=energiaTart-5
            if energiaTart<=0:
                energiaTart=0
            if posTart>70:
                posTart=70
            print(posTart)
            if tempo=="Piovoso":
                posTart=posTart-1
                print(f"Tempo piovoso,Tartaruga penalità -1: {posTart}")
        else:
            print(f"Energia non sufficiente \n Energia guadagnata: +10")
            energiaTart=energiaTart+10
            if energiaTart>=100:
                energiaTart=100
    elif Tartaruga(i)== "Scivolata":
        if energiaTart>10:
            posTart=posTart-6
            energiaTart=energiaTart-10
            if energiaTart<=0:
                energiaTart=0
            if posTart<1:
                posTart=1
            print(posTart)
            if tempo=="Piovoso":
                posTart=posTart-1
                print(f"Tempo piovoso,Tartaruga penalità -1: {posTart}")
        else:
            print(f"Energia non sufficiente \n Energia guadagnata: +10")
            energiaTart=energiaTart+10
            if energiaTart>=100:
                energiaTart=100
    elif Tartaruga(i)== "Passo lento":
        if energiaTart>3:
            posTart=posTart+1
            energiaTart=energiaTart-3
            if energiaTart<=0:
                energiaTart=0
            if posTart>70:
                posTart=70
            print(posTart)
            if tempo=="Piovoso":
                posTart=posTart-1
                print(f"Tempo piovoso,Tartaruga penalità -1: {posTart}")
        else:
            print(f"Energia non sufficiente \n Energia guadagnata: +10")
            energiaTart=energiaTart+10
            if energiaTart>=100:
                energiaTart=100


    if Lepre(j)== "Riposo":
        posLepre=posLepre+0
        energiaLepre=energiaLepre+10
        if energiaLepre>=100:
            energiaLepre=100
        print(posLepre)
        if tempo=="Piovoso":
            posLepre=posLepre-2
            print(f"Tempo piovoso,Lepre penalità -2: {posLepre}")
    elif Lepre(j)== "Grande balzo":
        posLepre=posLepre+9
        energiaLepre=energiaLepre-15
        if energiaLepre<=0:
            energiaLepre=0
        if posLepre>70:
            posLepre=70
        print(posLepre)
        if tempo=="Piovoso":
            posLepre=posLepre-2
            print(f"Tempo piovoso,Lepre penalità -2: {posLepre}")

    elif Lepre(j)== "Grande scivolata":
        posLepre=posLepre-12
        energiaLepre=energiaLepre-20
        if energiaLepre<=0:
            energiaLepre=0
        if posLepre<1:
            posLepre=1
        print(posLepre)
        if tempo=="Piovoso":
            posLepre=posLepre-2
            print(f"Tempo piovoso,Lepre penalità -2: {posLepre}")

    elif Lepre(j)== "Piccolo balzo":
        posLepre=posLepre+1
        energiaLepre=energiaLepre-5
        if energiaLepre<=0:
            energiaLepre=0
        if posLepre>70:
            posLepre=70
        print(posLepre)
        if tempo=="Piovoso":
            posLepre=posLepre-2
            print(f"Tempo piovoso,Lepre penalità -2: {posLepre}")

    elif Lepre(j)== "Piccola scivolata":
        posLepre=posLepre-2
        energiaLepre=energiaLepre-8
        if energiaLepre<=0:
            energiaLepre=0
        if posLepre<1:
            posLepre=1
        print(posLepre)
        if tempo=="Piovoso":
            posLepre=posLepre-2
            print(f"Tempo piovoso,Lepre penalità -2: {posLepre}")
    print(Posizioni(posTart,posLepre))
    conta=conta+1
if posLepre >= 70:
    print("HARE WINS || YUCH!!!")
elif posTart >= 70:
    print("TORTOISE WINS! || VAY!!!")
elif posTart==posLepre:
    print("IT'S A TIE")