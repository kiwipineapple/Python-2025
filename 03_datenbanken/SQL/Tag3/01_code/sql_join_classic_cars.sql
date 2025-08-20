use classicmodels;

/*
SELECT 
	c.customerName, o.orderNumber, o.status
FROM
	customers AS c
LEFT JOIN
	orders as o
ON
	c.customerNumber = o.customerNumber;
*/
    
-- DELETE from orders Where customerNumber = 103;

-- Selektiere alle Bestellungen mit dem Status shipped (orders).
-- Kundennamen im Ergebnis ausgeben (o.orderNumber, o.orderDate, c.customerName)
/*
SELECT 
	o.orderNumber, o.orderDate, c.customerName
FROM
	customers AS c
INNER JOIN
	orders AS o
ON 
	c.customerNumber = o.customerNumber
WHERE
	o.status = 'shipped';
*/

-- von Allen Kunden (From customers) die Anzahl der Bestellung (JOIN auf orders)
-- um die Bestellungen für jeden KUnden darzustellen, muss nach Kunde gruppiert werden
SELECT
	c.customerName, COUNT(*) as anzahl_bestellungen
FROM
	customers AS c
LEFT JOIN
	orders AS o
ON
	o.customerNumber = c.customerNumber
GROUP BY
	o.customerNumber;  