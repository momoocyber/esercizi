class Pagamento:
    def __init__(self) -> None:
        self.__pagamento= 0.0
    def set_pagamento(self, pagamento):
        self.__pagamento= pagamento

    def get_pagamento(self):
        return self.__pagamento
    
    def dettagli_pagamento(self):
        print(f"Importo del pagamento: €{self.get_pagamento():.2f}")

class PagamentoContanti(Pagamento):
    def __init__(self, importo) -> None:
        super().__init__()
        self.set_pagamento(importo)
    
    def dettagli_pagamento(self):
        print(f"Pagamento in contanti di: €{self.get_pagamento():.2f}") 

    def inPezziDa(self):
        importo = self.get_pagamento()
        banconote = [500, 200, 100, 50, 20, 10, 5]
        monete = [2, 1, 0.50, 0.20, 0.10, 0.05, 0.01]

        for banconota in banconote:
            num_banconote = int(importo / banconota)
            if num_banconote > 0:
                print(f"{num_banconote} banconota  da {banconota} euro")
                importo -= num_banconote * banconota
        for moneta in monete:
            num_monete = int(importo / moneta)
            if num_monete > 0:
                print(f"{num_monete} moneta da {moneta} euro")
                importo -= num_monete * moneta

class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, nome, data_scadenza, numero_carta):
        super().__init__()
        self.nome = nome
        self.data_scadenza = data_scadenza
        self.numero_carta = numero_carta
    
    def dettagliPagamento(self):
        super().dettagli_pagamento()
        print(f"Pagamento effettuato con la carta di credito")
        print(f"Nome sulla carta: {self.nome}")
        print(f"Data di scadenza: {self.data_scadenza}")
        print(f"Numero della carta: {self.numero_carta}")




pagamento_contanti1 = PagamentoContanti(100)
pagamento_contanti1.set_pagamento(150.00)
pagamento_contanti2 = PagamentoContanti(100)
pagamento_contanti2.set_pagamento(95.25)

pagamento_carta1 = PagamentoCartaDiCredito("Mario Rossi", "12/24", "1234567890123456")
pagamento_carta1.set_pagamento(200.00)
pagamento_carta2 = PagamentoCartaDiCredito("Luigi Bianchi", "01/25", "6543210987654321")
pagamento_carta2.set_pagamento(500.00)


pagamento_contanti1.dettagli_pagamento()
pagamento_contanti1.inPezziDa()
print()

pagamento_contanti2.dettagli_pagamento()
pagamento_contanti2.inPezziDa()
print()

pagamento_carta1.dettagli_pagamento()
print()

pagamento_carta2.dettagli_pagamento()
