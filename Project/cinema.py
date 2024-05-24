class Film:
    def __init__(self, titolo: str, durata: int) -> None:
        self.titolo=titolo
        self.duarata=durata


class Sala:
    def __init__(self, n_identificativo: int, film: Film, p_tot: int, p_prenotati: int) -> None:
        self.n_identificativo=n_identificativo
        self.film= film
        self.p_tot=p_tot
        self.p_prenotati=p_prenotati
        self.posti_disp= p_tot- p_prenotati
        


    def prenota_posti(self, p_da_prenotare):
        if (self.p_tot- self.p_prenotati)>= p_da_prenotare:
            print("PRENOTAZIONE EFFETTUATA!")
            self.p_prenotati+=p_da_prenotare
        else:
            print("IMPOSSIBILE PRENOTARE")

        return self.p_prenotati
    
    def posti_disponibili(self):
        self.posti_disp= self.p_tot - self.p_prenotati
        print(f"I posti disponibili sono: {self.posti_disp}")

        return self.posti_disp


class Cinema:
    def __init__(self, sale : list[Sala]) -> None:
        self.sale=sale        
        
    def aggiungi_sala(self, sala_da_aggiungere : Sala):

        self.sale.append(sala_da_aggiungere)
        print(f"sala aggiunta! ")
        for i in self.sale:
            print(f"Numero identificativo sala :{i.n_identificativo}")

        return self.sale

    def prenota_film(self, title_film : str, num_posti: int ): 
        for i in self.sale:
            if (i.film.titolo == title_film) and (num_posti <= i.posti_disponibili()):
                return  print("PRENOTAZIONE EFFETTUATA")
            else:
                return print("non possibile")
            

film : Film= Film("Pinocchio", 120)
film_2 : Film= Film("Shrek", 130)
sala:Sala = Sala(2, film, 20, 10)
sala_2: Sala= Sala(3, film_2, 30, 20)
cinema : Cinema= Cinema([sala, sala_2])
sala_3: Sala= Sala(4, film_2, 30, 20)
sala.prenota_posti(2)
sala_2.prenota_posti(2)
sala.posti_disponibili()
sala_2.posti_disponibili()
cinema.aggiungi_sala(sala_3)
cinema.prenota_film("Pinocchio", 3)




