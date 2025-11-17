class Vozilo:
    def __init__(self, marka,model,godište,cijena):
        self.marka=marka
        self.model=model
        self.godište=godište
        self.cijena=cijena

    def info(self):
        print('--INFORMACIJE-------->>>')
        print(f'Marka: {self.marka}')
        print(f'Model: {self.model}')
        print(f'Godina proizvodnje: {self.godište}')
        print(f'Cijena: {self.cijena} EUR')

    def promjenacijene(self,nova_cijena):
        self.nova_cijena=nova_cijena
        self.cijena=nova_cijena
        print(f'Cijena promijenjena. Nova cijena je {self.cijena}')


class ELvozilo(Vozilo):
    def __init__(self, marka,model,godište,cijena, dometBaterije):
        super().__init__(marka,model,godište,cijena)
        self.dometBaterije=dometBaterije

    def info(self):
        super().info()
        print(f'Domet: {self.dometBaterije} km')

def izbornik():
    print('---AUTOSALON ŠTREBAONA---')
    print('0. Izlaz')
    print('1. Unos novog vozila(obično)')
    print('2. Unos novog vozila(električno)')
    print('3. Informacije o vozilu')
    print('4. Promjena cijene vozila')
    print('5. Ispiši sva vozila')
    print('-------------------------')

def unosVozila():
    print('Unos novog vozila.')
    marka=input('Marka: ')
    model=input('Model: ')
    godište=input('Godina proizvodnje: ')
    cijena=input('Cijena (eur): ')
    vozilo=Vozilo(marka,model,godište,cijena)
    autosalon.append(vozilo)
    vozilo.info()

def unosElVozila():
    print('Unos novog električnog vozila.')
    marka=input('Marka: ')
    model=input('Model: ')
    godište=input('Godina proizvodnje: ')
    cijena=input('Cijena: ')
    dometBaterije=input('Domet baterije (km): ')
    vozilo=ELvozilo(marka,model,godište,cijena,dometBaterije)
    autosalon.append(vozilo)
    vozilo.info()

def nađiVozilo(autosalon):
    print('Pronađi vozilo.')
    marka=input('Marka: ')
    model=input('Model: ')
    if izbor==3:
        for i in autosalon:
                if i.marka==marka and i.model==model:
                    i.info()
    if izbor==4:
        for i in autosalon:
                if i.marka==marka and i.model==model:
                    nova_cijena=int(input('Nova cijena(eur): '))
                    i.promjenacijene(nova_cijena)
    
autosalon=[]

while True:
    izbornik()
    try:
        izbor=int(input('Unesite izbor (0/1/2/3/4/5): '))
        if izbor==0:
            break
        elif izbor==1:
            unosVozila()
        elif izbor==2:
            unosElVozila()
        elif izbor==3:
            nađiVozilo(autosalon)
            
        elif izbor==4:
            nađiVozilo(autosalon)
            

        elif izbor==5:
            for i in autosalon:
                i.info()

        else:
            print('Greška! Unesite valjani odabir (0/1/2/3/4/5)')
    except ValueError:
        print('Greška! Unesite valjani odabir (0/1/2/3/4/5)')





    
    
    
