class Libro:
    def __init__(self, titolo: str, autore: str, stato: bool= True) -> None:
        self.titolo=titolo
        self.autore=autore
        self.stato=stato

class Biblioteca:
    def __init__(self) -> None:
        self.list_libri = []

    def aggiungi_libro(self, libro : Libro):
        self.list_libri.append(libro)
        return "LIBRO AGGIUNTO"
                        
    def presta_libro(self, titolo : str):
        for i in self.list_libri:
            if i.titolo == titolo and i.stato == True:
                i.stato= False
                
                return "Libro disponibile"
            else:
                return "libro non disponibile"

    def restituisci_libro(self, titolo: str):
        for i in self.list_libri:
            if i.titolo == titolo and i.stato == False:
                i.stato = True 
                return "Libro restituito"
            else:
                return "libro non prestato o non presente"
            
    def mostra_libri_disponibili(self):
        libri_disponibili=[]
        for libro  in self.list_libri:
            if libro.stato==True:
                libri_disponibili.append(libro.titolo)
                return libri_disponibili
            else:
                return "ERRORE"      


libro_1: Libro=Libro("Pinocchio", "Collodi")
libro_2 : Libro=Libro("libro 2", "giacomino")
libro_3 : Libro=Libro("libro 3", "peppe")

biblioteca_1: Biblioteca=Biblioteca()

print(biblioteca_1.aggiungi_libro(libro_1))
print(biblioteca_1.aggiungi_libro(libro_2))
print(biblioteca_1.aggiungi_libro(libro_3))

print(biblioteca_1.presta_libro("libro 2"))
print(biblioteca_1.restituisci_libro("libro 2"))
print(biblioteca_1.mostra_libri_disponibili())

