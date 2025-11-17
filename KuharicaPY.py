class Recept:
    def __init__(self, naziv):
        self.naziv = naziv
        self.sastojci = []  

    def dodaj_sastojak(self, sastojak, količina):
        self.sastojci.append({'sastojak': sastojak, 'količina': količina})

    def prikaži(self):
        print(f"{self.naziv}")
        for sastojak_dict in self.sastojci: 
                print(f"- {sastojak_dict['sastojak']}: {sastojak_dict['količina']}")
        print("--------------------------")


class Kuharica(): 
    def __init__(self, naziv):
        self.naziv = naziv 
        self.recepti = [] 

    def dodaj_recept(self, recept_objekt):
        self.recepti.append(recept_objekt)


    def pronađi_recept(self, naziv_recepta): 
        found = False 
        for recept_objekt in self.recepti: 
            if naziv_recepta == recept_objekt.naziv: 
                recept_objekt.prikaži() 
                found = True
        
        if not found: 
            print(f"Hmm... Recept nije pronađen u kuharici.")




juha = Recept('Juha')
karbonara = Recept('Karbonara')


juha.dodaj_sastojak('voda', '1L')
juha.dodaj_sastojak('meso', '250g')
juha.dodaj_sastojak('peršin', 'prstohvat')

karbonara.dodaj_sastojak('Tjestenina', 'po želji')
karbonara.dodaj_sastojak('Vrhnje za kuhanje', '100mL')
karbonara.dodaj_sastojak('Šunka', '50g')


moja_kuharica = Kuharica('Kuharica') 

moja_kuharica.dodaj_recept(karbonara)
moja_kuharica.dodaj_recept(juha)

moja_kuharica.pronađi_recept("Karbonara")
moja_kuharica.pronađi_recept("Juha")
moja_kuharica.pronađi_recept("Kolač") 


