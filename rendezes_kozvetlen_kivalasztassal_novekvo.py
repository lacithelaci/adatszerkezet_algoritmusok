tomb = [5, 8, 3, 11, 9, 6, 4]
tomb_hossza = len(tomb)
for i in range(0, tomb_hossza - 1):
    for j in range(i + 1, tomb_hossza):
        if tomb[i] > tomb[j]:
            tomb[i], tomb[j] = tomb[j], tomb[i]

print(tomb)
