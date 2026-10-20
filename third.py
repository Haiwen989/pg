
def je_prvocislo(cislo):
    if cislo < 2:
        return False

    for i in range(2, cislo):
        if cislo % i == 0:
            return False
    return True

def vrat_prvocisla(maximum):
    seznam = []
    for cislo in range(1, maximum + 1):
        if je_prvocislo(cislo):
            seznam.append(cislo)
    return seznam

#----------------------------------------

if __name__ == "__main__":
    print(je_prvocislo(1))
    print(je_prvocislo(2))
    print(je_prvocislo(3))
    print(je_prvocislo(100))
    print(je_prvocislo(101))

    print(vrat_prvocisla(1))
    print(vrat_prvocisla(2))
    print(vrat_prvocisla(3))
    print(vrat_prvocisla(10))
