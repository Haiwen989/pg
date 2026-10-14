def cislo_text(cislo):
    cislo = int(cislo)

    jednotky = {
        0: "nula",
        1: "jedna",
        2: "dva",
        3: "tri",
        4: "ctyri",
        5: "pet",
        6: "sest",
        7: "sedm",
        8: "osm",
        9: "devet",
        10: "deset",
        11: "jedenact",
        12: "dvanact",
        13: "trinact",
        14: "ctrnact",
        15: "patnact",
        16: "sestnact",
        17: "sedmnact",
        18: "osmnact",
        19: "devatenact"
    }

    desitky = {
        20: "dvacet",
        30: "tricet",
        40: "ctyricet",
        50: "padesat",
        60: "sedesat",
        70: "sedmdesat",
        80: "osmdesat",
        90: "devadesat"
    }

    if cislo in jednotky:
        return jednotky[cislo]

    elif cislo in desitky:
        return desitky[cislo]

    elif cislo < 100:
        desitka = (cislo // 10) * 10
        jednotka = cislo % 10
        return desitky[desitka] + " " + jednotky[jednotka]

    elif cislo == 100:
        return "sto"

    else:
        return "Cislo je mimo rozsah 0 az 100"


if __name__ == "__main__":
    cislo = input("Zadej cislo: ")
    text = cislo_text(cislo)
    print(text)