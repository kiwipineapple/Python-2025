-- create database if not exists join_test;
use join_test;

create table if not exists Kunde (
    id INT PRIMARY KEY AUTO_INCREMENT,
    vorname Varchar(100),
    nachname Varchar(100)
);

create table if not exists Bestellung (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product Varchar(100),
    kunden_id INT NOT NULL,
    datum Date
);

INSERT INTO Kunde (vorname, nachname) VALUES ("John", "von Neumann"), ("Grace", "Hopper"), ("Donald", "Knuth"), ("Dennis", "Richie");
INSERT INTO Bestellung (product, kunden_id, datum) VALUES ("Teekanne", 1, "2024-12-12"),("Snickers XXL", 1, "2024-12-12"),("Lightbulp", 2, "2024-12-12"),("CPU", 1, "2024-12-12"),("Hut", 2, "2024-12-12"),("TV", 3, "2024-12-12");