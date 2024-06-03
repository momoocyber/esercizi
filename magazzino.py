<<<<<<< HEAD
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
=======
class MovieCatalog:
    def __init__(self):
        self.catalog = {}

    def add_movie(self, director_name, movies):
        if director_name in self.catalog:
            self.catalog[director_name].extend(movies)
        else:
            self.catalog[director_name] = movies
        return f"Film aggiunti a {director_name}"

    def remove_movie(self, director_name, movie_name):
        if director_name in self.catalog:
            if movie_name in self.catalog[director_name]:
                self.catalog[director_name].remove(movie_name)
                if not self.catalog[director_name]:
                    del self.catalog[director_name]
                return f"{movie_name} rimosso da {director_name}"
            else:
                return f"{movie_name} non trovato nella lista di {director_name}"
        else:
            return f"{director_name} non trovato nel catalogo"

    def list_directors(self):
        return list(self.catalog.keys())

    def get_movies_by_director(self, director_name):
        if director_name in self.catalog:
            return self.catalog[director_name]
        else:
            return f"{director_name} non trovato nel catalogo"

    def search_movies_by_title(self, title):
        found_movies = {}
        for director, movies in self.catalog.items():
            matched_movies = [movie for movie in movies if title.lower() in movie.lower()]
            if matched_movies:
                found_movies[director] = matched_movies
        
        if found_movies:
            return found_movies
        else:
            return "Nessun film trovato con il titolo specificato"
>>>>>>> abc38b4 (new)
