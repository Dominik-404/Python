#stvorimo klasu Knjiga
class Knjiga:
    #pridružujemo argumente
    def __init__(self, naslov, autor, godina_izdanja):
        self.naslov=naslov
        self.autor=autor
        self.godina_izdanja= godina_izdanja

        #ispisujemo podatke
        print(f'Naslov: {naslov}, autor: {autor}, godina izdanja: {godina_izdanja}')

#stvaramo objekte
knjiga1 = Knjiga("Uliks", "James Joyce", '1924')
knjiga2 = Knjiga("Gospodar prstenova", "J.R.R. Tolkien", '1954')
