
CREATE DOMAIN Email AS VARCHAR(100) 
    CHECK (VALUE ~'[a-z…');

CREATE DOMAIN IntegerGZ AS INTEGER
    CHECK (VALUE > 0);

CREATE DOMAIN Reale AS REAL 
    CHECK (VALUE BETWEEN 0 AND 1);


CREATE TABLE Cliente(
    email Email PRIMARY KEY,    
    nome VARCHAR(100) NOT NULL,      
    cognome VARCHAR(100) NOT NULL    
);

CREATE TABLE Ristorante(
    id_ristorante SERIAL PRIMARY KEY, 
    nome VARCHAR(100) NOT NULL,       
    partitaIVA VARCHAR(100) NOT NULL  
);

CREATE TABLE Promozione(
    nome VARCHAR(100) PRIMARY KEY,   
    sconto RealeIn01 NOT NULL,          
    n_coperti_g INTEGER CHECK (n_coperti_g > 0) 
);

CREATE TABLE Prenotazione(
    id_prenotazione SERIAL PRIMARY KEY,       
    istanteUt TIMESTAMP,                      
    istante_pren TIMESTAMP NOT NULL,       
    istante_app TIMESTAMP NOT NULL,          
    n_coperti INTEGER CHECK (n_coperti > 0), 
    IS_utilizzata BOOLEAN,      
    email_cliente Email NOT NULL,             
    id_ristorante INTEGER NOT NULL,          
    nome_promozione VARCHAR(100),             

    FOREIGN KEY (email_cliente) REFERENCES Cliente(email),
    FOREIGN KEY (id_ristorante) REFERENCES Ristorante(id_ristorante),
    FOREIGN KEY (nome_promozione) REFERENCES Promozione(nome)
);
