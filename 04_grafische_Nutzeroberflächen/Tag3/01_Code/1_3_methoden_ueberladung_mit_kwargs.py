class Nachricht:
    @staticmethod
    def senden(**kwargs):
        if "empfänger" in kwargs and "inhalt" in kwargs:
            print(f"Nachricht an {kwargs['empfänger']}: {kwargs['inhalt']}")
        elif "empfänger" in kwargs:
            print(f"Nachricht an {kwargs['empfänger']} ohne Inhalt.")
        else:
            print("Keine Empfängerangabe – Nachricht wurde nicht gesendet.")

# Aufrufe – ohne Objektinstanz möglich
Nachricht.senden(empfänger="Max", inhalt="Hallo!")
Nachricht.senden(empfänger="Lisa")
Nachricht.senden()
