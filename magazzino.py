#Gestione di un magazzino
#Scrivi un programma in Python che gestisca un magazzino.
#Il programma deve permettere di aggiungere prodotti al magazzino, 
#cercare prodotti per nome e verificare la disponibilità di un prodotto.

#Definisci una classe Prodotto con i seguenti attributi:
#- nome (stringa)
#- quantità (intero)
 
#Definisci una classe Magazzino con i seguenti metodi:
#- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
#- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
#- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.

class Prodotto:
    def __init__(self, nome: str, quantità: int) -> None:
        self.nome: str = nome
        self.quantità: int = quantità

class Magazzino:
    def __init__(self, prodotti: list[Prodotto] = []) -> None:
        self.prodotti: list = prodotti
    def aggiungi_prodotto(self, prodotto: Prodotto):
        self.prodotto.append(prodotto)
    def cerca_prodotto(self, nome: str) -> Prodotto:
        self.nome: str = nome
        for prodotti in Prodotto:
            if prodotti.nome in Prodotto:
                return prodotti.nome
    def verifica_disponibilità(self, nome: str) -> str:
        self.nome: str = nome
        if self.nome in Prodotto:
            return "disponibile"