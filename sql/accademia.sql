create type strutturato as 
enum('Ricercatore','Professore Associato','Professore Ordinario');
create type lavoro_progetto as 
enum('Ricerca e sviluppo','dimostrazione', 'Management', 'Altro');
create type lavoro_non_progettuale as 
enum('Didattica','Ricerca','Missione','Incontro Dipartimentale','Incontro
Accademico','Altro');
create type causa_assenza as 
enum('Chiusura Universitaria','Maternita','Malattia');
create domain  pos_integer as integer
check (value >=0);
create domain stringa_m as varchar(100);
create domain  numero_ore as integer
check (value >= 0 and value <= 8);
create domain  denaro as float
check (value >=0);

create table persona (
    id pos_integer not null, nome stringa_m not null, 
    cognome stringa_m not null, posizione strutturato not null,
    stipendio denaro not null,
    primary key(id)
);
create table progetto (
    id pos_integer not null, nome stringa_m not null, 
    inizio date not null , fine date not null check(fine>inizio),
    budget denaro not null,
    unique (nome),
    primary key(id)
);
create table wp(
    progetto pos_integer not null, id pos_integer not null, 
    nome stringa_m not null, inizio date not null, 
    fine date not null check(fine>inizio),
    unique (progetto, nome),
    foreign key(progetto) references progetto(id),
    primary key(id, progetto)
    
); 
create table attivita_progetto( 
    id pos_integer not null, 
    persona pos_integer not null, 
    progetto pos_integer not null, 
    giorno date not null, 
    tipo lavoro_progetto not null, 
    wp pos_integer not null, 
    ore_dur numero_ore not null, 
    foreign key (persona) references persona(id), 
    foreign key(progetto, wp) references wp(progetto, id),
    primary key(id)
);
create table attivita_non_progettuale(
    id pos_integer not null, persona pos_integer not null,
    tipo lavoro_non_progettuale not null, giorno date not null,
    ore_dur numero_ore not null, 
    foreign key (persona) references persona(id),
    primary key(id)
);
create table assenza(
    id pos_integer not null, persona pos_integer not null,
    tipo causa_assenza not null, giorno date not null,
    unique(persona, giorno),
    foreign key (persona) references persona(id),
    primary key(id)

);





