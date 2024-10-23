CREATE TABLE Nazione (
nome varchar not null,
PRIMARY KEY(nome)
);

CREATE TABLE Regione (
nome varchar not null,
nazione varchar not null,
PRIMARY KEY(nome, nazione),
FOREIGN KEY nazione 
references Nazione (nome)
);

CREATE TABLE Citta (
nome varchar not null,
regione varchar not null,
nazione varchar not null
PRIMARY KEY(nome, regione, nazione),
FOREIGN KEY(regione, nazione)
references Regione(nome, nazione)
);

CREATE TABLE Sede (
id serial primary key not null,
nome varchar not null,
indirizzo Indirizzo not null,
citta varchar not null,
regione varchar not null, 
nazione varchar not null,
FOREIGN KEY(citta, regione, nazione)
references Citta(nome ,regione, nazione)
);

CREATE TABLE Sala (
nome varchar not null,
sede Integer no null,
PRIMARY KEY(nome, sede)
FOREIGN KEY(sede) references Sede(id)
);

CREATE TABLE Settore (
id serial PRIMARY KEY not null,
nome varchar not null,
sala varchar not null,
sede Integer not null
UNIQUE(nome, sala, sede)
FOREIGN KEY(sala, sede)
references Sala(nome, sede)
);

CREATE TABLE Posto (
fila Integer not null,
colonna Integer not null,
settore Integer not null,
FOREIGN KEY settore references Settore(id),
PRIMARY KEY(fila, colonna, settore)
);

CREATE TABLE Artista (
id serial PRIMARY KEY not null,
nome varchar not null,
cognome varchar not null,
nome_arte varchar
);

CREATE TABLE TipologiaSpettacolo (
nome varchar not null,
PRIMARY KEY(nome)
);

CREATE TABLE Genere (
nome varchar not null,
PRIMARY KEY(nome)
)

CREATE TABLE TipoTariffa (
nome varchar not null,
PRIMARY KEY(nome)
);

CREATE TABLE Tariffa (
prezzo Denaro not null,
tipotariffa varchar not null,
settore Integer not null,
evento Integer not null,
PRIMARY KEY(tipotariffa, settore, evento),
FOREIGN KEY settore references Settore(id),
FOREIGN KEY tipotariffa
references TipoTariffa(nome)
FOREIGN KEY evento references Evento(id)
);

CREATE TABLE Spettacolo (
id serial PRIMARY KEY not null,
nome varchar not null,
durata_min PosInteger not null,
tipologiaspettacolo varchar not null,
genere varchar not null,
FOREIGN KEY tipologiaspettacolo references TipologiaSpettacolo(nome),
FOREIGN KEY genere references Genere(nome)
--v.incl id occorre in Partecipa(spettacolo)
);

CREATE TABLE Partecipa (
spettacolo Integer not null,
artista Integer not null,
PRIMARY KEY(spettacolo, artista),
FOREIGN KEY spettacolo references Spettacolo(id),
FOREIGN KEY artista references Artista(id)
);

CREATE TABLE Evento (
id serial PRIMARY KEY not null,
data date not null,
orario time not null,
spettacolo integer not null,
sala varchar not null,
sede varchar not null,
PRIMARY KEY(id, spettacolo, sala, sede),
FOREIGN KEY (sala, sede) references Sala(nome, sede),
FOREIGN KEY spettacolo references Spettacolo(id)
);

CREATE TABLE Pre_Posto (
prenotazione Integer not null,
fila Integer not null,
colonna Integer not null, 
settore  Integer not null,
tipotariffa varchar not null,
PRIMARY KEY(prenotazione, fila, colonna)
FOREIGN KEY tipotariffa references TipoTariffa(nome)
FOREIGN KEY prenotazione references Prenotazione(id)
FOREIGN KEY (fila, colonna, settore) references Posto(fila, colonna, settore)
);

CREATE TABLE Prenotazione (
id serial PRIMARY KEY not null,
evento Integer not null,
utente CF not null,
FOREIGN KEY evento references Evento(id),
FOREIGN KEY utente references Utente(cf)
);

CREATE TABLE Utente (
nome varchar not null,
cognome varchar not null,
cf CF not null,
PRIMARY KEY(cf),
);
