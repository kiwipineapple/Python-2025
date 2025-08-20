class Buch:
    def __init__(self, autor, titel, seite) -> None:
        self.autor = autor
        self.titel = titel
        self.seite = seite

    def __len__(self):
        return self.seite

    def __del__(self):
        print(f'Lösche {self.titel!r}')

    def __str__(self) -> str:
        return f'Das Buch {self.titel!r} ist von {self.autor} geschrieben und hat {self.seite} Seiten.'


p = Buch('Thomas', 'Wind', 150)
# print(p)
print(len(p))
del p
