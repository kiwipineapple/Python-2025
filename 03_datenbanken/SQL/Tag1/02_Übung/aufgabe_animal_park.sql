/*
# Aufgabe Animal Park(LEICHT)

## 1. Lege eine Datenbank an
Erstelle eine neue Datenbank "animal_park" und nutze sie (use).

## 2. Erstelle eine Tabelle Animal
- id: Primärschlüssel (Autoincrement)
- name: Varchar
- description: Text
- species_id: Foreign Key (auf Tabelle  Species)
- birthdate: Date


## 3. Erstelle eine Tabelle Species
- id: Primärschlüssel (Autoincrement)
- name: Varchar
- description: Text


## 4. Füge Testdaten ein
- Füge zwei Species ein (Lion, Penguin)
- Füge 5 Tiere ein
*/


CREATE DATABASE IF NOT EXISTS animal_park;
USE animal_park;

-- delet Table
-- DROP TABLE Animal;


CREATE TABLE IF NOT EXISTS Species(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS Animal(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    Species_id INT NOT NULL,
    FOREIGN KEY(Species_id) REFERENCES Species(id)
);

INSERT INTO
	Species
(name, description)
VALUES
('Lion', 'eat meat'),
('Penguin', 'can swim');

INSERT INTO
	Animal
(name, description, Species_id)
VALUES
('cat', 'cute', 1),
('dog', 'love', 2),
('wolf', 'wild', 1);

