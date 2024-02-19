def linearis_kereses():
    tomb = [3, 5, 11, 23, 56, 78]
    hossz = len(tomb)
    a = int(input("kérek egy számot"))
    for i in range(hossz):
        if tomb[i] == a:
            return i
    return -1


def main():
    print(linearis_kereses())


if __name__ == "__main__":
    main()
