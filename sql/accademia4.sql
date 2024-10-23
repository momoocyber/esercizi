

begin transaction;
--1
select distinct Persona.cognome
from Persona;

--2
select nome, cognome
from Persona
where posizione = 'Ricercatore';


--3
select cognome, nome
from Persona
where posizione <> 'Ricercatore' and cognome like 'V%';
--3
select cognome, nome
from Persona
where posizione = 'Professore Associato' or posizione = 'Professore Ordinario' and cognome like 'V%';


select nome
from Progetto
where fine < CURRENT_DATE;


select nome
from Progetto
order by inizio asc;


select nome
from WP
order by nome;



select distinct Assenza.tipo
from Assenza;


select distinct attivitaprogetto.tipo
from attivitaprogetto

select distinct attivitanonprogettuale.giorno
from attivitanonprogettuale
where attivitanonprogettuale.tipo= 'Didattica'
