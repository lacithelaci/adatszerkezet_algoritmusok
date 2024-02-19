def binkereses():
    rendezett_tomb = [2, 5, 11, 23, 56, 89, 124]
    also_korlat = 0
    felso_korlat = len(rendezett_tomb) - 1
    keresett_ertek = int(input("kérek egy számot"))
    while also_korlat <= felso_korlat:
        kozepso_ertek = (also_korlat + felso_korlat) // 2
        if rendezett_tomb[kozepso_ertek] == keresett_ertek:
            return kozepso_ertek
        if rendezett_tomb[kozepso_ertek] > keresett_ertek:
            felso_korlat = kozepso_ertek - 1
        else:
            also_korlat = kozepso_ertek + 1
    return -1


def main():
    print(binkereses())


if __name__ == "__main__":
    main()
