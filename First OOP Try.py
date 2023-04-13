def licznik_osob():
    if Osoba.licznik == 1:
        odpowiedz = f"dodales juz {Osoba.licznik} osobe"
    elif Osoba.licznik in range(2, 5):
        odpowiedz = f"dodales juz {Osoba.licznik} osoby"
    else:
        odpowiedz = f"dodales juz {Osoba.licznik} osob"
    return odpowiedz


class Osoba():
    licznik = 0
    def __init__(self, imie, nazwisko, wiek, wzrost, kolor_oczu, znamiona):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.wzrost = wzrost
        self.kolor_oczu = kolor_oczu
        self.znamiona = znamiona
        Osoba.licznik += 1

    def get_imie(self):
        return self.imie

    def get_nazwisko(self):
        return self.nazwisko

    def get_wiek(self):
        return self.wiek

    def get_wzrost(self):
        return self.wzrost

    def get_kolor_oczu(self):
        return self.kolor_oczu

    def get_znamiona(self):
        return self.znamiona


Marcin = Osoba("Marcin", "Giemza", 24, "184", "niebieskie", "brak")
Karolina = Osoba("Karolina", "Wozny", 23, "176", "brazowe", "pieprzyk tu i tu mam takie pojebane")

print(Marcin.wiek)
print(Marcin.znamiona)
print(licznik_osob())
