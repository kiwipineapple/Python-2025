"""(MITTEL - SCHWER)
Erstelle eine einfache Todo-Liste.

1) die Klasse TodoListe verwaltet Todos (Strings).
2) Dazu wird ein User-Interface in einem While-Loop benötigt.
Das User-Interface ist NICHT Teil der Klasse TodoListe!

Diese drei Kommandos muss das Programm mindestens unterstützen:
Hinzufügen von einem todo (add)
Löschen von einem todo (del)
Anzeigen aller Todos (show)


# BEISPIEL-EINGABE:

ADD Text   → fügt ein ToDo hinzu
DEL Text   → entfernt ein ToDo
SHOW       → zeigt alle ToDos
QUIT       → beendet das Programm
Benutze ADD, DEL, SHOW oder QUIT zum Beenden.
Eingabe: ADD Wäsche waschen
'Wäsche waschen' hinzugefügt.

Benutze ADD, DEL, SHOW oder QUIT zum Beenden.
Eingabe: ADD Kochen
'Kochen' hinzugefügt.

Benutze ADD, DEL, SHOW oder QUIT zum Beenden.
Eingabe: SHOW
1. Wäsche waschen
2. Kochen

Benutze ADD, DEL, SHOW oder QUIT zum Beenden.
Eingabe: XYZ
Unbekanntes Kommando. Bitte benutze ADD, DEL, SHOW oder QUIT.

Benutze ADD, DEL, SHOW oder QUIT zum Beenden.
Eingabe: QUIT
Goodbye!

# Code-Beispiel (Interaktion mit der Todo-Liste):

liste = ToDoList("Meine Aufgaben")
liste.add("Wäsche waschen)
liste.add("Einkaufen")
todos = liste.get_list()
print(todos)  # Ausgabe: ['Wäsche waschen', 'Einkaufen']

"""


class ToDoList:
    def __init__(self, name: str) -> None:
        self.name = name
        self.list = []

    def add(self, text: str):
        self.list.append(text)
        return self.list

    def delet(self, text: str):
        if text in self.list:
            self.list.remove(text)
            return self.list
        else:
            print('Diese Aufgabe is nicht in ToDoList.')

    def get_list(self):
        for i in self.list:
            print(f'{self.list.index(i) + 1}. {i}')

    def quit(self):
        print('Goodbye!')


def main():

    liste = ToDoList('Meine Aufgaben')

    while True:
        print('Benutze ADD, DEL, SHOW oder QUIT zum Beenden.')
        word = input('Eingabe: ')
        command_word = word.split(' ', 1)[0]

        if command_word == 'ADD':
            todo_word = word.split(' ', 1)[1]
            liste.add(todo_word)
        elif command_word == 'DEL':
            todo_word = word.split(' ', 1)[1]
            liste.delet(todo_word)
        elif command_word == 'SHOW':
            liste.get_list()
        elif command_word == 'QUIT':
            liste.quit
            break
        else:
            print('Unbekanntes Kommando. Bitte benutze ADD, DEL, SHOW oder QUIT.')


if __name__ == "__main__":
    main()
