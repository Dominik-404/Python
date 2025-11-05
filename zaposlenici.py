class Zaposlenik:
    def __init__(self,ime,prezime,plaća):
        self.ime=ime
        self.prezime=prezime
        self.plaća=plaća

    def prikaži_info(self):
        print(f'Ime: {self.ime}')
        print(f'Prezime: {self.prezime}')
        print(f'Plaća: {self.plaća} EUR')

class Programer(Zaposlenik):
    def __init__(self, ime, prezime, plaća, programski_jezici):
        super().__init__(ime,prezime,plaća)
        self.programski_jezici=programski_jezici

    def prikaži_info(self):
        super().prikaži_info()
        print(f'Programski jezici: {self.programski_jezici}')

class Upravitelj(Zaposlenik):
    def __init__(self,ime,prezime,plaća,tim):
        super().__init__(ime,prezime,plaća)
        self.tim=tim
    
    def prikaži_info(self):
        super().prikaži_info()
        print(f'Tim: {self.tim}')


# Kreiranje objekata
z1 = Zaposlenik("Ana", "Anić", 1200)
p1 = Programer("Petar", "Perić", 1800, ["Python", "JavaScript"])
m1 = Upravitelj("Iva", "Ivić", 2500, ["Ana Anić", "Petar Perić"])

# Pozivanje metoda
print("--- Podaci o zaposleniku ---")
z1.prikaži_info()

print("\n--- Podaci o programeru ---")
p1.prikaži_info()

print("\n--- Podaci o menadžeru ---")
m1.prikaži_info()


        
