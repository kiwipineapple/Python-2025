"""
MDI (Multi Document Interface) – Tabbed + Fenster-Menü

Diese Version zeigt:
- Tab-Ansicht für Unterfenster
- Menüleiste mit Datei- und Fenster-Optionen
- Dokumente beim Start + neue Dokumente
"""

# ----- Bibliotheken importieren -----
import sys

from PyQt5.QtWidgets import (
    QApplication,  # Grundbaustein jeder PyQt-Anwendung (Ereignisschleife, Ressourcenverwaltung)
    QMainWindow,   # Hauptfenster-Grundklasse: bietet Menüleiste, Toolbars, Statusleiste, zentralen Bereich
    QMdiArea,      # Container für mehrere Unterfenster (MDI: Multi-Document-Interface)
    QMdiSubWindow, # Einzelnes Unterfenster innerhalb der QMdiArea (hier indirekt genutzt)
    QTextEdit,      # Einfaches mehrzeiliges Textfeld (dient als Beispiel-"Dokument")
    QInputDialog  # Neu: Dialog zur Namensabfrage
)

class MDIExample(QMainWindow):
    """
     Unsere Hauptfenster-Klasse. Wir erben von QMainWindow, um
     - eine Menüleiste (menuBar),
     - einen zentralen Inhaltsbereich (setCentralWidget),
     - und später optional Statusleiste/Toolbars
     nutzen zu können.
     """
    def __init__(self):
        # Eltern-Konstruktor aufrufen (initialisiert das QMainWindow sauber)
        super().__init__()

        # Fenster-Titel & Größe setzen
        self.setWindowTitle("MDI mit Tabs & Fenster-Menü")
        self.resize(800, 600)

        # ----- MDI-Bereich einrichten -----
        # Die QMdiArea ist ein spezieller Bereich, in dem mehrere "Dokumente" (Unterfenster) verwaltet werden.
        self.mdi = QMdiArea()

        # Standardmäßig zeigt eine QMdiArea frei schwebende Unterfenster (SubWindowView).
        # Wir stellen auf Tab-Ansicht um, weil es  übersichtlicher ist:
        self.mdi.setViewMode(QMdiArea.TabbedView)

        # Tabs dürfen geschlossen und per Drag&Drop umsortiert werden:
        self.mdi.setTabsClosable(True)  # Tabs können geschlossen werden
        self.mdi.setTabsMovable(True)   # Tabs können per Drag&Drop verschoben werden

        # Die MDI-Area wird als "zentraler Bereich" des Hauptfensters gesetzt.
        # Alles, was wir der MDI-Area hinzufügen, erscheint somit im Hauptfenster.
        self.setCentralWidget(self.mdi)

        # Statusleiste anlegen/anzeigen und Starttext setzen
        self.statusBar().showMessage("Bereit")

        # ----- Zähler für sprechende Dokumentnamen -----
        # Wir zählen, wie viele Dokumente erstellt wurden, um sie durchnummerieren zu können.
        self.doc_count = 0

        # ----- Menüleiste aufbauen (Datei/Fenster) -----
        self.create_menus()

        # ----- Zwei Start-Dokumente anzeigen -----
        #for _ in range(2):
        #    self.create_document()

    def create_menus(self):
        """
        Erstellt die Menüleiste mit 'Datei' und 'Fenster'.
        - Datei: Neues Dokument anlegen, Beenden der Anwendung
        - Ansicht: Umschalten zwischen Tabbed/SubWindow
        - Fenster: Fenster anordnen (Kacheln/Kaskadieren) und zwischen Fenstern wechseln
        """
        menubar = self.menuBar()  # QMainWindow stellt automatisch eine menuBar() bereit.

        # ----- Datei-Menü -----
        file_menu = menubar.addMenu("Datei")

        # Eintrag: Neues Dokument
        new_action = file_menu.addAction("Neues Dokument") # Menüpunkt erzeugen
        new_action.setShortcut("Ctrl+N")  # Tastenkürzel (Strg+N)
        new_action.triggered.connect(self.create_document)  # Aktion: neues Unterfenster/Dokument anlegen

        # Beenden
        exit_action = file_menu.addAction("Beenden")
        exit_action.setShortcut("Ctrl+Q")  # Tastenkürzel (Strg+Q)
        exit_action.triggered.connect(self.close) # schließt das Hauptfenster (und beendet die App)

        # --- in create_menus() ---
        view_menu = menubar.addMenu("Ansicht")

        toggle_tabs = view_menu.addAction("TabbedView an/aus")
        toggle_tabs.setCheckable(True)  # Schalter mit Häkchen
        toggle_tabs.setChecked(True)  # Start: TabbedView aktiv
        toggle_tabs.setStatusTip(
            "Zwischen Tab-Ansicht und frei schwebenden Fenstern umschalten. "
        )
        toggle_tabs.toggled.connect(self.toggle_view_mode)

        # ----- Fenster-Menü -----
        window_menu = menubar.addMenu("Fenster")

        window_menu.addAction("Kacheln", self.mdi.tileSubWindows)
        window_menu.addAction("Kaskadieren", self.mdi.cascadeSubWindows)
        window_menu.addAction("Nächstes", self.mdi.activateNextSubWindow)
        window_menu.addAction("Vorheriges", self.mdi.activatePreviousSubWindow)

        # Aktives Unterfenster schließen.
        close_act = window_menu.addAction("Aktives schließen")
        close_act.triggered.connect(self.mdi.closeActiveSubWindow)

    def toggle_view_mode(self, on: bool):
        """
        Wechselt nur die Darstellung:
        True  -> TabbedView (Tabs bleiben schließbar/verschiebbar)
        False -> SubWindowView (frei schwebende Fenster)
        """
        # Nur den Modus umschalten – Tabs-Einstellungen NICHT ändern
        self.mdi.setViewMode(QMdiArea.TabbedView if on else QMdiArea.SubWindowView)
        mode = "TabbedView" if on else "SubWindowView"
        self.statusBar().showMessage(f"Ansicht: {mode}")


    def create_document(self):
        """
         Erstellt ein neues Text-Dokument als Unterfenster (Tab).
        - Wir nutzen einen QTextEdit als einfachen Dokument-Inhalt.
        - Fragt einen Namen ab.
        - Cancel (ok == False) -> bricht ab, erstellt KEIN Dokument.
        - Leere Eingabe -> vergibt automatisch den nächsten Nummern-Namen (1, 2, 3, …).
        """

        # Nächste Nummer berechnen (ohne doc_count sofort zu erhöhen)
        next_number = self.doc_count + 1

        # Namen abfragen
        title, ok = QInputDialog.getText(
            self,
            "Dokumentname",
            "Geben Sie den Namen des Dokuments ein (leer lassen für automatische Nummerierung):"
        )

        # ok == True, wenn Benutzer "OK" geklickt hat.
        # ok == False, wenn Benutzer den Dialog mit "Abbrechen" geschlossen hat.
        # ok kommt aus dem Rückgabewert der Funktion QInputDialog.getText(),
        # die ein Tupel (eingabetext, ok-boolean) zurückgibt.
        if not ok:
            return

        # Leere Eingabe -> Nummer
        final_title = title.strip() or str(next_number)

        # Zähler fortschreiben
        self.doc_count = next_number

        # Inhalt vorbereiten
        editor = QTextEdit()   # Einfache Textfläche als "Dokument"
        editor.setPlainText(f"Inhalt von {final_title}")  # Beispieltext

        # addSubWindow gibt das erzeugte QMdiSubWindow zurück.
        # Vorteil: weniger Code als explizit QMdiSubWindow() zu erzeugen und setWidget(...) aufzurufen.
        # (sehe 1_mdi_grundlagen umsetzung für QMdiSubWindow() version)
            # BRÜCKE: QMdiArea (self.mdi) <—> QMdiSubWindow
            # Wir rufen addSubWindow(...) von QMdiArea() auf. Dabei passiert Folgendes:
            # 1) Die QMdiArea() ERZEUGT intern ein QMdiSubWindow(),
            # 2) setzt unser Widget (hier: editor) als INHALT dieses Subwindows,
            # 3) NIMMT dieses Subwindow in ihre VERWALTUNG auf (aktivieren, kacheln, kaskadieren, schließen …),
            # 4) und GIBT uns das Subwindow-Objekt zurück, damit wir z.B. den Titel setzen können.
        # Das ist kürzer und weniger fehleranfällig, als ein QMdiSubWindow manuell zu erzeugen und danach setWidget(...) aufzurufen (siehe 01_mdi_grundlagen für die lange Variante).
        sub = self.mdi.addSubWindow(editor)  # Direkter Weg, ohne extra QMdiSubWindow()

        # Der Fenstertitel erscheint in der Tab-Leiste (TabbedView) bzw. im Rahmen (SubWindowView).
        sub.setWindowTitle(final_title)

        # Unterfenster anzeigen (ohne show() wäre es erstellt, aber nicht sichtbar).
        sub.show()

# ----- Programmstart (Bootstrapping der Qt-Anwendung) -----
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MDIExample()
    window.show()
    sys.exit(app.exec_())
