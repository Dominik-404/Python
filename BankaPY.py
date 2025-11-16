class BankRačun:
    def __init__(self, vlasnik, broj_računa):
        self.vlasnik = vlasnik
        self.broj_računa = broj_računa
        
        self.stanje = 0.0
        return self.info()

    def uplata(self, iznos):
        self.iznos=iznos
        if iznos>=0:
            self.stanje=self.stanje + iznos
            print('Uplata uspješna.')

        else:
            print('Nevažeći iznos! Molimo upišite pozitivan broj.')

        


    def isplata(self, iznos):
        self.iznos=iznos
        if iznos>=0:
            if self.stanje>=iznos:
                self.stanje=self.stanje - iznos
                print('Isplata uspješna.')

            else:
                print('Isplata neuspješna! Upišite vrijednost manju ili jednaku trenutnom stanju.')

        else:
            print('Nevažeći iznos! Molimo upišite pozitivan broj.')

            

    def info(self):
        print('>---INFORMACIJE---<')
        print(f'Vlasnik računa: {self.vlasnik}')
        print(f'Broj računa: {self.broj_računa}')
        print(f'Stanje: {self.stanje:.2f}')
        print('>-----------------<')
        print('1. Uplata')
        print('2. Isplata')

        try:
            izbor = int(input("Unesite izbor (1/2): "))

            if izbor == 1:
                    iznos=float(input('Iznos uplate: '))
                    
                    self.uplata(iznos)

            if izbor == 2:
                    iznos=float(input('Iznos isplate: '))
                    
                    self.isplata(iznos)

            
        except ValueError:
            print('Greška! Nevažeći unos.')

        return self.info()

        
            
                    

račun= BankRačun('Mate Rimac', '12320302')




