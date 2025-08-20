
-- AUFGABEN für Datenbank classicCars

/*
Erstelle eine SQL-Abfrage, die die Anzahl der bestellten Mengen
für jede Bestellung zusammenfasst.

Tabelle orders, orderdetails

Group BY ist wichtig, welches
aggregiert wird, wenn auf anzahl bezogen wird
und die quantityOrdered pro Order addiert.

Ergebnis:
OrderID, Anzahl der bestellten Produkte
orderID, GesamtsummeQuantity
10100   151
10101   142
10102   80
10103   541
10104   443
10105   545
[..]
*/




/*
Aufgabe: Gesamtssumme aller Orders  (products.buyPrice * quantityOrdered)

Tabellen orders, orderdetails, products

Ergebnis:
orderID, GesamtsummeOrder
10100   6283.47
10101   5312.27
10102   3358.84
10103   31391.84
10104   24525.40
10105   32584.88
[..]

*/





/*

Erstelle eine SQL-Abfrage, die den Gesamtbestellwert für eine spezifische Bestellung mit der Bestellnummer "10101" berechnet  (products.buyPrice * quantityOrdered)

Tabelle orders, orderdetails, products

Ergebnis:
orderid,total_order_price
10101,5312.27
*/



