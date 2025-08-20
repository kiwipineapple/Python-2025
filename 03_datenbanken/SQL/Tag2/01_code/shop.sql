drop database shop;
CREATE DATABASE shop;
use shop;

-- Produkt Kategorie
DROP TABLE IF EXISTS product_tag;
DROP TABLE IF EXISTS product; -- erst die Produkt löschen, dann die Category löschen
DROP TABLE IF EXISTS category;  -- Tabelle category löschen, falls existiert
DROP TABLE IF EXISTS tag; 

-- Tabelle category anlegen
CREATE TABLE IF NOT EXISTS category (
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

INSERT INTO 
	category 
	(name)
VALUES 
	("Spielzeug"),
    ("Technik"),
    ("Hifi");
    
-- Produkt Tabelle
CREATE TABLE IF NOT EXISTS product (
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    category_id INT NOT NULL,  -- NUll ist default
    FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE CASCADE
);

-- Was passiert, wenn Kategorie gelöscht wird. 3 Möglichkeiten
-- ON DELETE RESTRICT => (default) Kategorie kann nicht gelöscht werden, solange noch ein Produkt
-- darauf zeigt.

-- ON DELETE CASCADE => Wenn Kategorie gelöscht wird, werden alle Produkte dieser Kategorie gelöscht
-- ON DELETE SET NULL => Wenn Kategorie gelöscht wird, werden die Produkt auf Null gesetzt


INSERT INTO 
	product
	(name, category_id)
VALUES 
	("Star Wars Legobox", 1),
    ("Playmobil Bauernhof", 1),
    ("Bose Lautsprecher X3", 3);

-- das hier geht nur, wenn category_id NULL sein darf (default)
-- INSERT INTO product (name) VALUES ("test produkt");  -- Produkt ohne Kategorie
-- DELETE from category WHERE id = 1;

-- Tabelle für Tags (neu, fun, summer)
CREATE TABLE tag (
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

INSERT INTO 
	tag
	(name)
VALUES 
	("Summer"),
    ("für Kinder"),
    ("fun");

CREATE TABLE product_tag (
	product_id INT,
    tag_id INT,
    PRIMARY KEY (product_id, tag_id),
    FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tag(id) ON DELETE CASCADE
);

-- Tags für Produkte festlegen
INSERT INTO 
	product_tag (product_id, tag_id) 
VALUES 
	(1, 3),
    (1, 2),
    (3, 1),
    (3, 2);


