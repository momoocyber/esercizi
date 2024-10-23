CREATE TABLE Nazione (
    nome varchar not null,
    PRIMARY KEY(nome)
);


CREATE TABLE Regione (
    nome varchar not null,
    nazione varchar not null,
    PRIMARY KEY(nome, nazione),
    FOREIGN KEY nazione references Nazione(nome)
);

CREATE TABLE Citta(
    nome varchar not null,
    regione varchar not null,
    nazione varchar not null,
    PRIMARY KEY(nome, regione, nazione),
    FOREIGN KEY(regione, nazione) references Regione(nome, nazione)
);


CREATE TABLE Officina(
    nome varchar not null,
    indirizzo indirizzo not null,
    id integer not null,
    citta varchar not null,
    regione varchar not null,
    nazione varchar not null,
    PRIMARY KEY(id)
    FOREIGN KEY(citta, regione, nazione) references  Citta(nome, regione, nazione)
);

CREATE TABLE Riparazione(
    riconsegna timestamp,
    codice  integer not null,
    inizio  timestamp not null,
    officina integer not null.
    PRIMARY KEY(codice),
    FOREIGN KEY(officina) references Officina(id)
);

CREATE TABLE Marca(
    nome varchar not null,
    PRIMARY KEY(nome)
);

CREATE TABLE  Modello(
    nome varchar not null,
    marca varchar not null,
    tipoveicolo varchar not null,
    PRIMARY KEY(nome, marca)
    FOREIGN KEY(marca) references Marca(nome)
    FOREIGN KEY(tipoveicolo) references TipoVeicolo(nome)
);    

CREATE TABLE TipoVeicolo(
    nome varchar not null,
    PRIMARY KEY(nome)
);