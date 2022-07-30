DROP DATABASE IF EXISTS c_tunes_db;
CREATE DATABASE c_tunes_db;

\c c_tunes_db

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;

-- reset tables (erase data)
TRUNCATE TABLE artists CASCADE;
TRUNCATE TABLE users CASCADE;

-- add some data 

-- Users
INSERT INTO users (email, password,  first_name,  last_name)
VALUES ('chris@chris.com', 'password123', 'Chris', 'Bowen');

INSERT INTO users (email, password,  first_name,  last_name)
VALUES ('you@domain.com', 'password', 'Andy', 'lastname');

INSERT INTO users (email, password,  first_name,  last_name)
VALUES ('other@place.com', 'mypassword', 'Chris', 'Jones');

-- artists
INSERT INTO artists (name)
VALUES ('Metallica');

INSERT INTO artists (name)
VALUES('Pink Floyd');

INSERT INTO artists (name)
VALUES('Beatles');

INSERT INTO artists (name)
VALUES('Missy Elliot');