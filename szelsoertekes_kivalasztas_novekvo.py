tomb = [5, 8, 3, 11, 9, 6, 4]
tomb_hossza = len(tomb)
for i in range(0, tomb_hossza - 1):
    minimum = i
    for j in range(i + 1, tomb_hossza):
        if tomb[minimum] > tomb[j]:
            minimum = j

    tomb[i], tomb[minimum] = tomb[minimum], tomb[i]

print(tomb)
