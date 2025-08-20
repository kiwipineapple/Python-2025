use join_test;

-- INNER JOIN
SELECT 
	k.vorname, b.datum, b.product
FROM
	Kunde AS k  -- Ursprünlich Tabelle
INNER JOIN 
	Bestellung AS b 
ON 
	k.id = b.kunden_id
WHERE
	k.id = 1;
    
-- LEFT JOIN (zeige alle Einträge der linken Tabelle  und fülle auf mit NULL, wenn
-- der Eintrag in der rechten Tabelle fehlt
SELECT 
	k.vorname, b.datum, b.product
FROM
	Kunde AS k
Left JOIN 
	Bestellung AS b 
ON 
	k.id = b.kunden_id;