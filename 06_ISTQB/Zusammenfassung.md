# Chapter 1

**Test vs. Debuggen**  
Test ist Code zu *bewerten*, reduzieren Fehlerwirkung  
Debuggen ist Code zu *verbessern*  

**Test Defination**  
Der Prozess innerhalb des Softwareentwicklungslebenszyklus, der die Qualität einer Komponente oder eines Systems und der zugehörigen Arbeitsergebnisse bewertet.

**Test(Qualität Steuerung) vs. Qualitätsicherung (QA)**  
**Test**: Produktorientierung, zur Erreichung eines angemessenen Qualitätsniveaus  
**QA**: Prozessorientierung, Implementierung und verbesserung Prozess

## Grundsätze des Testens  
1. Testen zeigt das Vorhandensein, nicht die Abwesenheit von Fehlerzuständen  
2. Vollständiges Testen ist unmöglich  
3. Frühes Testen spart Zeit und Geld
4. Fehlerzustände treten gehäuft auf
5. Tests nutzen sich ab
6. Testen ist kontextabhängig
7. Trugschluss: „Keine Fehler“ bedeutet ein brauchbares System


**Validierung** ist Kundenoritieren, von draußen  
**Varifizierung** ist von innen  

**Authentizierung**  
**Authorizierung**: permission  

---

**Software Serve is basiert auf Hardware-Server.**  
Zugriff auf SW-Serve durch Ports-Nummer.

## Test activities
1. Testplanung: Ziel des Test
2. Testanalyse: Analyse was soll getestet. 
3. Test Entwurf: Testplan wie die Test zu machen. 
4. Test Realisierung: prepare Test Hardware, Test Data, Test case
5. Test excecution: machen die Tests. 
6. Testabschluss: Bericht für Test erstellen. 

## V-Modell
Unit Test -> Integration Test -> System Test -> Abnahme Test



## Agile
**Kanban**: Backlog, in progress, done  
**Scrum**: Sprint, schätz Point, Review, Retro  
**Product Owner**: Entscheiden was machen sollten  
**Scrum Master**: Vertretung der Kunden in Projekt   
**Dev**: Wie das machen sollten  

[Scrum guides Link](https://scrumguides.org/)

**DevOps**: Software Infastruktur, Kombi aus *IT* und *Dev*, z.B. Jira, Git Server, CI/CD  
**IT**: Hareware Infastruktur, z.B. Username, Computer vorbereiten

## Virtuelle Maschinen (WM)
Host O.S. -> isolierte Subsystem  
Selbst Versuch: Win10 WM / Ubuntu VW -> Mithilfe [Youtube](https://www.youtube.com/watch?v=F5MMhNQ3C3I)

---
# Chapter 2
## Teststufen
**Softwaretest/Komponententest/Unittest**: testen isolierte Baustein  
**Komponentintegrationtest**: Test Schnittstelle zwischen Komponenten  
**Systemtest**  
**Systemintegrationtest**  
**Abnahmetest**: -> Alpha Test: mit Umgebung von Entwickler  
                ->Beta Test: mit Umgebung von End User  
 **Shift-Left-Ansatz**

## Testarten
funktinale Test  
Nicht funktinale Test: Leistungtest, Security, Performance(z.B. Zeit)

**Blace-Box**: Akzeptanz Test  
**White-Box**: guck von innen  


**Fehlernachtest** Test ob Fehler behoben ist, keine Nebenauswirkung mehr.  
**Regressionstest**  Test nach Fehlernachtest, mit Umgebung.


1. objekt-orientirert-programmieren
miro project in Modul schreiben

2. Datenbank Design
   
3. Try Except

4. Warum for-Schleifen / While-Schleifen
   
4. Quizzes Chapter 1

[]
1. Definition: Anlegen von list
2. Index, Key

()
1. Anlegen von Turple
2. Calling Function

## Test Excetion
~~~python
print('Hallo World')
~~~