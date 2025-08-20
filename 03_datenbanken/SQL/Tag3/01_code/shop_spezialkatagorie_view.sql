CREATE VIEW SpezialKategorie AS
SELECT name 
FROM category 
WHERE id in (1, 2);