class Okno(object):
    def __init__(self, wys, szer):
        self.wys = wys
        self.szer = szer
        self.opened = False

    def __str__(self):
        return "Wysokosc " + str(self.wys) + ", Szerokosc " + str(self.szer) + self.if_opened()

    def open(self):
        if self.opened == False:
            self.opened = True

    def close(self):
        if self.opened == True:
            self.opened = False

    def if_opened(self):
        if self.opened == True:
            return " Okno jest otwarte"
        else:
            return " Okno jest zamkniete"

class Pokoj(object):
    def __init__(self, windows, name):
        #self.n_o_walls = n_o_walls
        #self.n_o_doors = n_o_doors
        self.windows = windows
        self.name = name

    def __str__(self):
        part1 = "Nazwa pokoju: " + str(self.name) + ", Liczba okien: " + str(len(self.windows)) + ", "
        part2 = " , ".join([str(window) for window in self.windows])
        return part1 + part2

    def ilosc_okien(self):
        return len(self.windows)

bedroom = Pokoj([Okno(200, 100), Okno(200, 80)], "Bedroom")
living_room = Pokoj([Okno(200, 60), Okno(200, 60), Okno(200, 60)], "Living room")

rooms = [bedroom, living_room]




rooooms = []
n_o_rooms = int(input("Ile pomieszczeń, mordo? "))
for numer_pokoju in range(n_o_rooms):
    type = str(input("Podaj nazwę " + str(numer_pokoju + 1) + " pomieszczenia: "))
    n_o_windows = int(input("Ile jest okien w tym pomieszczeniu? "))
    oookna = []
    for numer_okna in range(n_o_windows):
        szer = input("Podaj szerokość " + str(numer_okna + 1) + " okna w milimetrach: ")
        wys = input("Podaj wysokość " + str(numer_okna + 1) + " okna w milimetrach: ")
        oookna.append(Okno(wys, szer))
    rooooms.append(Pokoj(oookna, type))

for room in rooooms:
    print(room)
