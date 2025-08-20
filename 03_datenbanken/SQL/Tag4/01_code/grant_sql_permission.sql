-- neuen User erstellen
DROP USER 'alice'@'localhost';
CREATE USER 'alice'@'localhost' IDENTIFIED BY 'abcd1234';

-- Alice darf auf allen Datenbank / allen Daten (*.*) arbeiten
-- Weiter einschränken, z.B. nur Datenbank shop, wäre dann: ON shop
GRANT SELECT, INSERT, UPDATE, DELETE ON *.* TO 'alice'@'localhost';

FLUSH PRIVILEGES;

select * from mysql.user;
