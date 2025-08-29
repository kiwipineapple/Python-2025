// db.getMongo().getDBs()
// db.dropDatabase()
db.createCollection("weather2")

db.weather2.insertMany([
    {
        city: "Berlin",
        date: "2023-07-01",
        phenomena: ["sunny", "dry"],
        measurements: [25, 26, 27, 29]
    },
    {
        city: "Paris",
        date: "2023-07-01",
        phenomena: ["cloudy", "windy"],
        measurements: [23, 22, 24, 25]
    },
    {
        city: "London",
        date: "2023-07-01",
        phenomena: ["rain", "storm", "cold"],
        measurements: [17, 16, 18, 15]
    }
])


// Aufgaben

// 1. Füge bei Berlin das Phänomen "breezy" dem Array `phenomena` hinzu.
// 2. Füge "sunny" nur hinzu, wenn es noch nicht existiert.
// 3. Entferne "dry" aus dem Phänomen-Array von Berlin.
// 4. Entferne das erste Phänomen bei London.
// 5. Entferne das letzte Phänomen bei Paris.
// 6. Füge bei Paris die Messwerte `26` und `27` zum `measurements`-Array hinzu.
// 7. Suche alle Einträge, bei denen das Phänomen "storm" enthalten ist.
// 8. Suche alle Einträge, bei denen es **nicht** "sunny" war.
// 9. Suche alle Einträge, bei denen im `measurements`-Array der Wert `29` enthalten ist.
// 10. Gib alle Städte zurück, bei denen das `measurements`-Array **mehr als 3 Werte** enthält.

// ## Bonus

// 11. Füge bei jedem Dokument ein neues Feld `tags` hinzu, das ein leeres Array ist.
// 12. Füge bei Berlin dem Feld `tags` die Einträge `"summer"` und `"dry"` gleichzeitig hinzu.
// 13. Entferne `"dry"` wieder aus dem `tags`-Feld von Berlin.