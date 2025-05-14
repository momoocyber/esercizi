import requests


base_url = "http://127.0.0.1:8080"  

def cerca_casa_vendita():
    filtri = {"stato": "LIBERO" }
    try:
        response = requests.post(f"{base_url}/cerca_casa_vendita", json={"filtri": filtri})
        response.raise_for_status()  
        print("Risultati case in vendita:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Errore nella richiesta: {e}")

def cerca_casa_affitto():
    filtri = {"tipo_affitto": "TOTALE"}
    try:
        response = requests.post(f"{base_url}/cerca_casa_affitto", json={"filtri": filtri})
        response.raise_for_status() 
        print("Risultati case in affitto:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Errore nella richiesta: {e}")

def venduta_casa():
    catastale = input("Inserisci il codice catastale della casa venduta: ")
    try:
        response = requests.post(f"{base_url}/venduta_casa", json={"catastale": catastale})
        response.raise_for_status()
        print(response.json()["message"])
    except requests.exceptions.RequestException as e:
        print(f"Errore nella richiesta: {e}")

def affittata_casa():
    catastale = input("Inserisci il codice catastale della casa affittata: ")
    try:
        response = requests.post(f"{base_url}/affittata_casa", json={"catastale": catastale})
        response.raise_for_status()
        print(response.json()["message"])
    except requests.exceptions.RequestException as e:
        print(f"Errore nella richiesta: {e}")

def menu():
    print("Scegli un'opzione:")
    print("1. Cerca case in vendita")
    print("2. Cerca case in affitto")
    print("3. Segna casa come venduta")
    print("4. Segna casa come affittata")
    print("5. Esci")

    scelta = input("Inserisci il numero dell'opzione: ")

    if scelta == '1':
        cerca_casa_vendita()
    elif scelta == '2':
        cerca_casa_affitto()
    elif scelta == '3':
        venduta_casa()
    elif scelta == '4':
        affittata_casa()
    elif scelta == '5':
        print("Uscita dal programma.")
        exit()
    else:
        print("Opzione non valida. Riprova.")
        menu()

if __name__ == "__main__":
    menu()
