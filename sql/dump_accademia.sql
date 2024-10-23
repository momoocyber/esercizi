--
-- PostgreSQL database dump
--

-- Dumped from database version 16.4 (Debian 16.4-1.pgdg120+1)
-- Dumped by pg_dump version 16.4 (Debian 16.4-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: causa_assenza; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.causa_assenza AS ENUM (
    'Chiusura Universitaria',
    'Maternita',
    'Malattia'
);


ALTER TYPE public.causa_assenza OWNER TO postgres;

--
-- Name: denaro; Type: DOMAIN; Schema: public; Owner: postgres
--

CREATE DOMAIN public.denaro AS double precision
	CONSTRAINT denaro_check CHECK ((VALUE >= (0)::double precision));


ALTER DOMAIN public.denaro OWNER TO postgres;

--
-- Name: lavoro_non_progettuale; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.lavoro_non_progettuale AS ENUM (
    'Didattica',
    'Ricerca',
    'Missione',
    'Incontro Dipartimentale',
    'Incontro
Accademico',
    'Altro'
);


ALTER TYPE public.lavoro_non_progettuale OWNER TO postgres;

--
-- Name: lavoro_progetto; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.lavoro_progetto AS ENUM (
    'Ricerca e sviluppo',
    'dimostrazione',
    'Management',
    'Altro'
);


ALTER TYPE public.lavoro_progetto OWNER TO postgres;

--
-- Name: numero_ore; Type: DOMAIN; Schema: public; Owner: postgres
--

CREATE DOMAIN public.numero_ore AS integer
	CONSTRAINT numero_ore_check CHECK (((VALUE >= 0) AND (VALUE <= 8)));


ALTER DOMAIN public.numero_ore OWNER TO postgres;

--
-- Name: pos_integer; Type: DOMAIN; Schema: public; Owner: postgres
--

CREATE DOMAIN public.pos_integer AS integer
	CONSTRAINT pos_integer_check CHECK ((VALUE >= 0));


ALTER DOMAIN public.pos_integer OWNER TO postgres;

--
-- Name: stringa_m; Type: DOMAIN; Schema: public; Owner: postgres
--

CREATE DOMAIN public.stringa_m AS character varying(100);


ALTER DOMAIN public.stringa_m OWNER TO postgres;

--
-- Name: strutturato; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.strutturato AS ENUM (
    'Ricercatore',
    'Professore Associato',
    'Professore Ordinario'
);


ALTER TYPE public.strutturato OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: assenza; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.assenza (
    id public.pos_integer NOT NULL,
    persona public.pos_integer NOT NULL,
    tipo public.causa_assenza NOT NULL,
    giorno date NOT NULL
);


ALTER TABLE public.assenza OWNER TO postgres;

--
-- Name: attivita_non_progettuale; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.attivita_non_progettuale (
    id public.pos_integer NOT NULL,
    persona public.pos_integer NOT NULL,
    tipo public.lavoro_non_progettuale NOT NULL,
    giorno date NOT NULL,
    ore_dur public.numero_ore NOT NULL
);


ALTER TABLE public.attivita_non_progettuale OWNER TO postgres;

--
-- Name: attivita_progetto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.attivita_progetto (
    id public.pos_integer NOT NULL,
    persona public.pos_integer NOT NULL,
    progetto public.pos_integer NOT NULL,
    giorno date NOT NULL,
    tipo public.lavoro_progetto NOT NULL,
    wp public.pos_integer NOT NULL,
    ore_dur public.numero_ore NOT NULL
);


ALTER TABLE public.attivita_progetto OWNER TO postgres;

--
-- Name: persona; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.persona (
    id public.pos_integer NOT NULL,
    nome public.stringa_m NOT NULL,
    cognome public.stringa_m NOT NULL,
    posizione public.strutturato NOT NULL,
    stipendio public.denaro NOT NULL
);


ALTER TABLE public.persona OWNER TO postgres;

--
-- Name: progetto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.progetto (
    id public.pos_integer NOT NULL,
    nome public.stringa_m NOT NULL,
    inizio date NOT NULL,
    fine date NOT NULL,
    budget public.denaro NOT NULL,
    CONSTRAINT progetto_check CHECK ((fine > inizio))
);


ALTER TABLE public.progetto OWNER TO postgres;

--
-- Name: wp; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.wp (
    progetto public.pos_integer NOT NULL,
    id public.pos_integer NOT NULL,
    nome public.stringa_m NOT NULL,
    inizio date NOT NULL,
    fine date NOT NULL,
    CONSTRAINT wp_check CHECK ((fine > inizio))
);


ALTER TABLE public.wp OWNER TO postgres;

--
-- Data for Name: assenza; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.assenza (id, persona, tipo, giorno) FROM stdin;
\.


--
-- Data for Name: attivita_non_progettuale; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.attivita_non_progettuale (id, persona, tipo, giorno, ore_dur) FROM stdin;
\.


--
-- Data for Name: attivita_progetto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.attivita_progetto (id, persona, progetto, giorno, tipo, wp, ore_dur) FROM stdin;
\.


--
-- Data for Name: persona; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.persona (id, nome, cognome, posizione, stipendio) FROM stdin;
\.


--
-- Data for Name: progetto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.progetto (id, nome, inizio, fine, budget) FROM stdin;
\.


--
-- Data for Name: wp; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.wp (progetto, id, nome, inizio, fine) FROM stdin;
\.


--
-- Name: assenza assenza_persona_giorno_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assenza
    ADD CONSTRAINT assenza_persona_giorno_key UNIQUE (persona, giorno);


--
-- Name: assenza assenza_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assenza
    ADD CONSTRAINT assenza_pkey PRIMARY KEY (id);


--
-- Name: attivita_non_progettuale attivita_non_progettuale_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attivita_non_progettuale
    ADD CONSTRAINT attivita_non_progettuale_pkey PRIMARY KEY (id);


--
-- Name: attivita_progetto attivita_progetto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attivita_progetto
    ADD CONSTRAINT attivita_progetto_pkey PRIMARY KEY (id);


--
-- Name: persona persona_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.persona
    ADD CONSTRAINT persona_pkey PRIMARY KEY (id);


--
-- Name: progetto progetto_nome_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.progetto
    ADD CONSTRAINT progetto_nome_key UNIQUE (nome);


--
-- Name: progetto progetto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.progetto
    ADD CONSTRAINT progetto_pkey PRIMARY KEY (id);


--
-- Name: wp wp_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.wp
    ADD CONSTRAINT wp_pkey PRIMARY KEY (id, progetto);


--
-- Name: wp wp_progetto_nome_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.wp
    ADD CONSTRAINT wp_progetto_nome_key UNIQUE (progetto, nome);


--
-- Name: assenza assenza_persona_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assenza
    ADD CONSTRAINT assenza_persona_fkey FOREIGN KEY (persona) REFERENCES public.persona(id);


--
-- Name: attivita_non_progettuale attivita_non_progettuale_persona_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attivita_non_progettuale
    ADD CONSTRAINT attivita_non_progettuale_persona_fkey FOREIGN KEY (persona) REFERENCES public.persona(id);


--
-- Name: attivita_progetto attivita_progetto_persona_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attivita_progetto
    ADD CONSTRAINT attivita_progetto_persona_fkey FOREIGN KEY (persona) REFERENCES public.persona(id);


--
-- Name: attivita_progetto attivita_progetto_progetto_wp_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attivita_progetto
    ADD CONSTRAINT attivita_progetto_progetto_wp_fkey FOREIGN KEY (progetto, wp) REFERENCES public.wp(progetto, id);


--
-- Name: wp wp_progetto_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.wp
    ADD CONSTRAINT wp_progetto_fkey FOREIGN KEY (progetto) REFERENCES public.progetto(id);


--
-- PostgreSQL database dump complete
--

