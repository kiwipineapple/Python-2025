class ArtikelListe:
    def __init__(self, artikellist) -> None:
        self.artikellist = artikellist

    def __len__(self):
        return len(self.artikellist)


p = ArtikelListe(['Buch', 'Film', 'Kopfhörer'])
print(len(p))
