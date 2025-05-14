-- QUERY 1:

SELECT  p.nome,p.cognome, COUNT(distinct ap.progetto) as num_progetti
FROM Persona p, AttivitaProgetto ap
WHERE  p.id = ap.persona and p.posizione = 'Professore Ordinario'
GROUP BY  p.nome, p.cognome;

-- QUERY 2:

SELECT p.nome, p.cognome, AVG(ap.oreDurata) as media_ore
FROM  Persona p, AttivitaProgetto ap
WHERE p.id = ap.persona and p.posizione = 'Ricercatore'
GROUP BY  p.nome, p.cognome;

-- QUERY 3:

SELECT nome,cognome,stipendio
FROM Persona
WHERE stipendio >= 60000;


-- QUERY 4: non risposto


-- QUERY 5:

SELECT p.nome, p.cognome, COUNT(a.giorno) as n_giorni_assenza
FROM  Persona p, Assenza a
WHERE  p.id = a.persona and p.posizione = 'Ricercatore' and a.tipo = 'Maternita'
GROUP BY  p.nome, p.cognome;


-- QUERY 6:

SELECT  AVG(budget) as media_budget
FROM  Progetto;


-- QUERY 7:

SELECT p.nome, p.cognome, SUM(ap.oreDurata) as tot_ore
FROM  Persona p, AttivitaProgetto ap
WHERE  p.id = ap.persona  and ap.progetto = 3
GROUP BY  p.nome, p.cognome;


-- QUERY 8:

SELECT p.nome, p.cognome, SUM(ap.oreDurata) as tot_ore
FROM Persona p, AttivitaProgetto ap
WHERE p.id = ap.persona and p.posizione = 'Professore Ordinario' and ap.progetto = 4 and ap.wp = 3
GROUP BY p.nome, p.cognome;


-- QUERY 9:

SELECT DISTINCT p.nome, p.cognome, p.stipendio
FROM Persona p, AttivitaProgetto ap
WHERE p.id = ap.persona and p.posizione = 'Professore Ordinario' and p.stipendio >= 60000;


-- QUERY 10: 

SELECT p.nome, p.cognome, AVG(anp.oreDurata) as media_ore
FROM Persona p, AttivitaNonProgettuale anp
WHERE p.id = anp.persona and anp.tipo = 'Didattica'
GROUP BY p.nome, p.cognome;
