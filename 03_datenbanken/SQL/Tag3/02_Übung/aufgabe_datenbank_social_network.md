# Datenbank Social network

Erstelle eine Datenbank für ein soziales Netzwerk oder Blogging-Plattform. Beschreibe dieser Datenbank und die Beziehungen zwischen den Tabellen.

- Zeichne ein ER-Diagramm für die Datenbank (zb. mit mermaid.js oder draw.io)
- Lege dazu die Tabellen und Beziehungen in einer SQL-Datei an.

In dieser Umgebung gibt es Benutzer, die sich registrieren und Profile erstellen.

Benutzer (Users): Benutzer sind Personen, die sich in dieser Plattform
registrieren. Jeder Benutzer hat einen eindeutigen Benutzernamen, eine
E-Mail-Adresse und ein Passwort, um sich anzumelden.

Rollen (Roles): Die Plattform verfügt über verschiedene Benutzerrollen, wie zum
Beispiel "Standardbenutzer" und "Moderator". Die Rollen können bestimmte
Berechtigungen und Zugriffe auf die Plattform steuern.

Benutzer können in dieser Umgebung folgende Aktionen ausführen:

    Beiträge (Posts): Benutzer können eigene Blog-Beiträge oder Nachrichten
erstellen. Diese Beiträge haben Titel, Inhalt und werden von einem bestimmten
Benutzer erstellt. Das Erstellungsdatum wird ebenfalls gespeichert.

    Kommentare (Comments): Benutzer können Kommentare zu Beiträgen
hinterlassen. Jeder Kommentar hat einen Inhalt, einen Autor und ist einem
bestimmten Beitrag zugeordnet. Das Erstellungsdatum des Kommentars wird
festgehalten.

    Freunde (Friends): Benutzer können Freundschaften mit anderen Benutzern
eingehen. Die Datenbank speichert die Freundschaftsbeziehungen zwischen
Benutzern, wobei der Status der Freundschaft (aktiv oder inaktiv) verfolgt
wird.

Hier ist ein einfaches Beispiel für eine Datenbank mit 5 Tabellen und Beziehungen zwischen ihnen:

    Benutzer (Users):
        Tabelle zur Speicherung von Benutzerinformationen.
        Attribute: UserID (Primärschlüssel), Benutzername, E-Mail

    Rollen (Roles):
        Tabelle zur Verwaltung der Benutzerrollen im System.
        Attribute: id (Primärschlüssel), Rollenname

    Beiträge (Posts):
        Tabelle zur Speicherung von Blog-Beiträgen oder Nachrichten.
        Attribute: id (Primärschlüssel), Titel, Inhalt, Autor (Fremdschlüssel zu User), Erstellungsdatum

    Kommentare (Comments):
        Tabelle zur Speicherung von Kommentaren zu Beiträgen.
        Attribute: id (Primärschlüssel), Inhalt, Autor (Fremdschlüssel zu UserID), Bezug auf Beitrag (Fremdschlüssel zu PostID), Erstellungsdatum

    Freunde (Friends):
        Tabelle zur Verwaltung von Benutzerfreundschaften.
        Attribute: id (Primärschlüssel), Benutzer1 (Fremdschlüssel zu UserID), Benutzer2 (Fremdschlüssel zu UserID), Freundschaftsstatus

Beziehungen zwischen den Tabellen:

    Die Tabelle "Posts" hat eine Beziehung zur Tabelle "Users" über das Attribut "Author" (Fremdschlüssel zu UserID). Jeder Beitrag wird einem Benutzer zugeordnet.

    Die Tabelle "Comments" hat ebenfalls eine Beziehung zur Tabelle "Users" über das Attribut "Author" (Fremdschlüssel zu UserID) und eine Beziehung zur Tabelle "Posts" über das Attribut "Bezug auf Beitrag" (Fremdschlüssel zu PostID). Jeder Kommentar ist einem Benutzer und einem Beitrag zugeordnet.

    Die Tabelle "Friends" hat zwei Beziehungen zur Tabelle "Users" über die Attribute "Benutzer1" und "Benutzer2" (beide sind Fremdschlüssel zu UserID). Dies ermöglicht die Verwaltung von Freundschaftsbeziehungen zwischen Benutzern. Kann man verhindern,
    dass ein Benutzer eine Freundschaftsanfrage an sich selbst sendet?

