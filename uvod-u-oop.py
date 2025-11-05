
class Učenik:
    def _init_(self,ime,prezime,razred):
        self.ime=ime
        self.prezime=prezime
        self.razred=razred

        self.ocjene=[]
        #self.prosjek=prosjek

    def dodaj_ocjenu(self,ocjena):
        if isinstance(ocjena,int) and 1<=ocjena<=5:
            self.ocjene.append(ocjena)
            print(f'INFO: Učeniku {self.ime} {self.prezime} upisana je ocjena {ocjena}')
        else:
            print('Nevažeća ocjena. Upišite broj od 1 do 5') 


    def izračunaj_prosjek(self):
        if not self.ocjene:
            return 0.0
        else:
            return sum(self.ocjene)/len(self.ocjene)
            return prosjek   

    def info(self):
        print('<>'*15)
        print(f'Ime:'{self.ime})
        print(f'Prezime:'{self.prezime})
        print(f'Razred:'{self.razred})
        
        if self.ocjene:
            print(f'Ocjene:'{self.ocjene})
        else:
            print('Učenik nema upisanih ocjena.')
        
        prosjek=self.izračunaj_prosjek()
        print('Prosjek:'prosjek)
        print('<>'*15)
    
učenik1=Učenik('Ana','Anić','4.b OG')
učenik2=Učenik('Tin','Tinić','4.c OG')

učenik1.dodaj_ocjenu(5)
učenik1.dodaj_ocjenu(5)
učenik1.dodaj_ocjenu(4)

učenik2.dodaj_ocjenu(5)
učenik2.dodaj_ocjenu(3)
učenik2.dodaj_ocjenu(4)

učenik1.info()
učenik2.info()
    
