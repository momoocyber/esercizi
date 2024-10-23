begin transaction;

--1
select codice, comp
from Volo
where durataMinuti>180;

--2
select distinct comp
from  Volo
where durataMinuti> 189;

--3
select codice, comp
from ArrPart
where partenza='CIA';

--4
select distinct codice, comp
from ArrPart
where partenza='FCO';

--5
select codice, comp
from ArrPart
where  partenza='FCO' and arrivo='JFK';

--6
select distinct comp
from ArrPart
where partenza='FCO' and arrivo='JFK';

--7
SELECT DISTINCT comp
FROM Volo
JOIN comp ON  Volo.comp = comp.codice
WHERE partenza IN ('FCO', 'CIA')  
  AND arrivo IN ('JFK');  
