use classicmodels;

-- SELECT * FROM products;   -- Selektiere alle Spalten / alle Zeilen von der Tabelle products
-- SELECT productCode, productName FROM products;  -- Selektiere Spaltenliste productCode, productName
-- SELECT * FROM products WHERE (productLine = "classic Cars" or productLine = "Motorcycles")

-- Alle Produkte selektieren die teurer als 100 sind
-- SELECT productName, buyPrice FROM  products WHERE buyPrice > 100;
-- SELECT productName, buyPrice, quantityInStock FROM  products WHERE buyPrice > 10 AND quantityInStock > 2000;
-- SELECT * FROM products WHERE productDescription IS NULL;
-- SELECT * from products WHERE NOT (productLine = "classic Cars" or productLine = "Motorcycles")
-- 1. Aufgabe
-- Selektiere alle Produkt mit productLine Planes, die einen buyPrice über 50 haben
SELECT * FROM products WHERE productLine = "Planes" AND buyPrice > 50;

-- 2.Aufgabe
-- Alle Produkte, die (teurer sind als 90 und mindest 18 mal auf Lager)
-- ODER aus dem Produktscale 1:10
-- SELECT * FROM products WHERE ((buyPrice > 90 AND quantityInStock > 17) OR productScale = "1:10");

-- Alle Produkte mit Moto im Namen
-- SELECT * FROM products WHERE productName LIKE "%Moto%";

-- Alle Produkte mit Helicopter am Ende
-- SELECT * FROM products WHERE productName LIKE "%Helicopter";

-- Alle Produkte zwischen 30 und 40 Euro
-- SELECT * FROM products WHERE buyPrice BETWEEN 30 AND 40;

-- IN-Operator: Alle Produkte aus den Linien Classic Cars, Motorcycles oder Planes
-- SELECT * FROM products WHERE productLine IN ("Classic Cars", "Motorcycles", "Planes");

-- Aggregatsfunktion count()
-- SELECT COUNT(*) AS anzahl FROM products WHERE productLine IN ("Classic Cars", "Motorcycles", "Planes");

-- Summiere die einzelnen buyPrices aller Produkt;
-- SELECT SUM(buyPrice) AS gesamtpreis from products;
-- SELECT SUM(buyPrice) AS gesamtpreis, productLine  from products GROUP BY productLine;

-- Durchschnittspreis 
-- SELECT AVG(buyPrice) AS durchschnittspreis, productLine  from products GROUP BY productLine;

-- Aufgabe: den Min und Maxpreis jeder Kategorie
-- SELECT MIN(buyPrice) AS minpreis, MAX(buyPrice) AS maxpreis, productLine from products GROUP BY productLine;
-- SELECT SUM(buyPrice * quantityInStock) as gesamtwert FROM products GROUP BY productLine;

-- Verbinde Strings zu einem neuen String (unter dem Alias new_name)
-- SELECT *, CONCAT(productLine, "_", productName) AS new_name FROM products;

-- Substring (von Zeichen 1 bis 4)
-- SELECT substring(productName, 1, 4) AS new_name FROM products;

-- ORDER BY (Aufsteigend nach ProductLine)
-- SELECT * FROM products ORDER BY productLine ASC;

-- ORDER BY (Gruppiert nach ProductLine, Absteigend nach ProductLine sortiert)
-- SELECT * FROM products GROUP BY productLine ORDER BY productLine DESC;

SELECT * from payments WHERE YEAR(paymentDate) = 2004 and MONTH(paymentDAte) = 12;



