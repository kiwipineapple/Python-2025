CREATE DATABASE IF NOT EXISTS geo;
USE geo;

CREATE TABLE IF NOT EXISTS Continent(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    population BIGINT
);

/*
INSERT INTO
	Continent 
(name, population)
VALUES
	("Europa", 800343),
    ("Antarktis", 50);
*/
CREATE TABLE IF NOT EXISTS City (
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    continent_id INT NOT NULL,
    FOREIGN KEY (continent_id) REFERENCES Continent(id)
);

INSERT INTO
	City
(name, continent_id)
VALUES
	('Hamburg', 1),
	("Berlin", 1),
    ("Forschungstation Süd", 2);