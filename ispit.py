class Nekretnina:
    def __init__(self, adresa, kvadratura, bazna_cijena):
        self.adresa = adresa
        self.kvadratura = kvadratura
        self.bazna_cijena = bazna_cijena

    def izračunaj_cijenu(self, cijena):
        self.cijena=self.bazna_cijena*self.kvadratura
        
    def info(self):
        print( f"Adresa: {self.adresa}, kvadratura: {self.kvadratura} m2, cijena: {self.cijena:.2f} EUR.")

class Stan(Nekretnina):
    def __init__(self, adresa, kvadratura, bazna_cijena, kat, lift):
        super().__init__(adresa, kvadratura, bazna_cijena)
        self.kat = kat
        self.lift = lift 
        lift=liftDN

    def izračunaj_cijenu(self):
        super().izračunaj_cijenu(self)
        if self.kat > 2 and self.lift==True:
            self.cijena = self.cijena - (self.cijena * 0.1)

        if self.lift==True:
            self.cijena = self.cijena + self.cijena*0.05

    def info(self):
        super().info()
        print(f"Kat: {self.kat}, lift: {'da' if self.lift==True else 'ne'}.")

class Kuća(Nekretnina):
    def __init__(self, adresa, kvadratura, bazna_cijena, površina_okućnice):
        super().__init__(adresa, kvadratura, bazna_cijena)
        self.površina_okućnice = površina_okućnice
        
    def izračunaj_cijenu(self):
        super().izračunaj_cijenu(self)
        self.cijena=self.bazna_cijena*self.kvadratura + (self.površina_okućnice*100)

    def info(self):
        super().info()
        print(f"Površina okućnice: {self.površina_okućnice} m2.")

nekretnine=[]

def izbornik():
    print('>>>NEKRETNINE<<<')
    print('1. Unesi stan')
    print('2. Unesi kuću')
    print('3. Ispiši sve nekretnine')
    print('4. Prodaja nekretnine')
    print('5. Pretraga po budžetu' )
    print('6. Izlaz')



while True:
    izbornik()
    try:
        izbor=int(input('Odaberite opciju: '))
        if izbor==1:
            adresa=input('Adresa stana: ')
            kvadratura=float(input('Kvadratura stana (m2): '))
            bazna_cijena=float(input('Bazna cijena po m2 (EUR): '))
            kat=int(input('Kat na kojem se stan nalazi: '))
            
            liftDN=input('Ima li zgrada lift (da/ne): ').lower()
            liftDN=True if liftDN=='da' else False
            stan=Stan(adresa, kvadratura, bazna_cijena, kat, liftDN)
            stan.izračunaj_cijenu()
            nekretnine.append(stan)
            print('Stan je uspješno unesen.')
        elif izbor==2:
            adresa=input('Adresa kuće: ')
            kvadratura=float(input('Kvadratura kuće (m2): '))
            bazna_cijena=float(input('Bazna cijena po m2 (EUR): '))
            površina_okućnice=float(input('Površina okućnice (m2): '))
            kuća=Kuća(adresa, kvadratura, bazna_cijena, površina_okućnice)
            kuća.izračunaj_cijenu()
            nekretnine.append(kuća)
            print('Kuća je uspješno unesena.')

        elif izbor==3:
            for i in nekretnine:
                i.info()
                
        elif izbor==4:
            adresa=input('Unesite adresu nekretnine koju želite prodati: ')
            for i in nekretnine:
                if i.adresa==adresa:
                    nekretnine.remove(i)
                    print('Nekretnina je uspješno prodana.')
                    
        elif izbor==6:
            print('Izlaz iz programa.')
            break

        elif izbor==5:
            budžet=float(input('Unesite svoj budžet (EUR): '))
            for i in nekretnine:
                if i.cijena <= budžet:
                    i.info()

        else:
            print('Pogrešan unos, birajte ponovno (1/2/3/4/5).')
    except ValueError:
        print('Pogrešan unos, pokušajte ponovo.')


        