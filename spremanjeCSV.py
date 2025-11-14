import csv
class Ucenik:
    """
    Nacrt (klasa) za stvaranje objekata koji predstavljaju učenike.
    Svaki učenik ima ime, prezime, razred i listu ocjena.
    """

    # 1. Konstruktor: Poziva se SVAKI PUT kad stvaramo novog učenika
    # 'self' predstavlja konkretnog učenika (objekt) koji se stvara
    def __init__(self, ime, prezime, razred):
        """Inicijalizira novi objekt Učenik s početnim podacima."""
        # Spremi podatke koje smo dobili u atribute (varijable) tog objekta
        self.ime = ime
        self.prezime = prezime
        self.razred = razred
        # Važno: Svaki učenik dobiva SVOJU VLASTITU praznu listu za ocjene
        self.ocjene = []  

    # 2. Metode: Funkcije unutar klase (što objekt može raditi)
    
    def dodaj_ocjenu(self, ocjena):
        """Dodaje novu ocjenu u listu ocjena učenika."""
        # Provjeravamo je li ocjena ispravan broj (cijeli broj između 1 i 5)
        if isinstance(ocjena, int) and 1 <= ocjena <= 5:
            self.ocjene.append(ocjena)
            print(f"INFO: Učeniku {self.ime} {self.prezime} je upisana ocjena {ocjena}.")
        else:
            print(f"GREŠKA: Ocjena '{ocjena}' nije važeća. Molimo unesite broj od 1 do 5.")

    def izracunaj_prosjek(self):
        """Vraća prosjek svih ocjena učenika."""
        # Provjera ako je lista ocjena prazna da se izbjegne dijeljenje s nulom
        if not self.ocjene:
            return 0.0
        
        # Izračunaj prosjek
        return sum(self.ocjene) / len(self.ocjene)

    def info(self):
        """Ispisuje sve dostupne informacije o učeniku na konzolu."""
        print("-" * 30)
        print(f"Ime i prezime: {self.ime} {self.prezime}")
        print(f"Razred: {self.razred}")
        
        if self.ocjene:
            print(f"Ocjene: {self.ocjene}")
        else:
            print("Ocjene: (nema upisanih ocjena)")
            
        # Pozivamo jednu metodu unutar druge
        prosjek = self.izracunaj_prosjek()
        # Formatiranje ispisa na 2 decimale
        print(f"Prosjek ocjena: {prosjek:.2f}") 
        print("-" * 30)

def ispisi_izbornik():
    """Jednostavno ispisuje glavni izbornik."""
    print ("-"*50)
    print ("Glavni izbornik")
    print ("-"*50)
    print ("0. Izlaz iz programa")
    print ("1. Unos nove učenice")
    print ("2. Unos ocjena za učenicu")
    print ("3. Ispis podataka o učenici")
    print ('4. Spremanje podataka')
    print ('5. učitavanje podataka')
    print ("-"*50)

def upisUcenice(ime, prezime, razred):
    """Prima podatke i VRAĆA novi OBJEKT Ucenik."""
    # Ovdje se poziva __init__ konstruktor klase
    ucenik = Ucenik(ime, prezime, razred)
    return ucenik

def upisOcjene(ucenik, ocjena):
    """Prima objekt učenika i ocjenu te poziva metodu nad tim objektom."""
    ucenik.dodaj_ocjenu(ocjena)

def ispisPodataka(ucenik):
    """Prima objekt učenika i poziva njegovu info metodu."""
    ucenik.info()

def podaciSpremi_csv(lista_ucenika,PodaciUčenika):
    with open(PodaciUčenika, mode='w', newline='', encoding='utf-8') as datoteka:
        polja = ['ime', 'prezime', 'razred']
        writer = csv.DictWriter(datoteka, fieldnames=polja)
        writer.writeheader()
        for p in lista_ucenika:
            writer.writerow({'ime': p.ime, 'prezime': p.prezime, 'razred': p.razred})
    print(f'Spremljeno u {PodaciUčenika}')

def podaciUčitaj_csv(PodaciUčenika):
    
    with open(PodaciUčenika, mode='r', encoding='utf-8') as datoteka:
        reader = csv.DictReader(datoteka)
        for red in reader:
            p = Ucenik(red['ime'], red['prezime'],red['razred'])
            lista_ucenika.append(p)
    print(f"Učitano iz {PodaciUčenika}")
    return lista_ucenika

global lista_ucenika
lista_ucenika = []

provjera = False # Pomoćna varijabla za provjeru je li učenik pronađen

while True:
    ispisi_izbornik()
    try:
        # 2. Pitamo korisnika za odabir
        izbor = int(input("Unesite izbor (0/1/2/3/4/5): "))
        
        if izbor == 1:
            # 1. Unos nove učenice
            print ("Unos nove učenice")
            # Pitamo korisnika za podatke
            ime = input("Unesite ime učenika: ")
            prezime = input("Unesite prezime učenika: ")
            razred = input("Unesite razred učenika: ")
            # Stvaramo novi objekt pomoću naše funkcije
            ucenik = upisUcenice(ime, prezime, razred)
            # Dodajemo novi objekt u našu glavnu listu
            lista_ucenika.append(ucenik)

        elif izbor == 2:
            # 2. Unos ocjena za učenicu
            ime = input("Unesite ime učenika: ")
            # Prolazimo kroz listu i tražimo učenika po imenu
            for ucenik in lista_ucenika:
                if ucenik.ime == ime:
                    provjera = True # Našli smo ga
                    break # Prekidamo petlju
                else:
                    provjera = False # Još ga nismo našli
            
            # Nakon petlje, provjeravamo je li pronađen
            if provjera:
                ocjena = int(input("Unesite ocjenu: "))
                # Prosljeđujemo objekt 'ucenik' i ocjenu funkciji
                upisOcjene(ucenik, ocjena)
            else:
                print ("Učenik nije pronađen.")

        elif izbor == 3:
            # 3. Ispis podataka o učenici
            ime = input("Unesite ime učenika: ")
            # Slična logika kao za unos ocjene
            for ucenik in lista_ucenika:
                if ucenik.ime == ime:
                    ispisPodataka(ucenik) # Pozivamo ispis za pronađenog
                    break # Prekidamo petlju
                else:
                    print ("Učenik nije pronađen.") # Ova poruka će se ispisati za svakog tko NIJE traženi

        elif izbor == 4:
            podaciSpremi_csv(lista_ucenika, 'PodaciUčenika')

        elif izbor == 5:
            podaciUčitaj_csv('PodaciUčenika')

        elif izbor == 0:
            # 0. Izlaz
            print ("Hvala na korištenju programa.")
            break # Prekida while petlju
            
        else: 
            print ("Greška")
            
    except ValueError:
        print ("Molimo unesite ispravan odabir (0/1/2/3).")





