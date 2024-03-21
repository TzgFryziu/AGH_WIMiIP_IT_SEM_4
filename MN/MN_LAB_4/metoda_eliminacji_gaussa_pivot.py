import sys
macierz_rozszerzona = list()


with open("test_a.txt","r") as f:
    for line in f:
        line = line.strip()
        macierz_rozszerzona.append([float(x) for x in line.split(" ")])

with open("test_b.txt","r") as f:
    i = 0
    for line in f:
        line = line.strip()
        macierz_rozszerzona[i].append(float(line))
        i += 1

for line in macierz_rozszerzona:
    print(line)

print("=====================================")






for i in range(len(macierz_rozszerzona)):

    for j in range(i+1, len(macierz_rozszerzona)):

        # if macierz_rozszerzona[i][i] == 0:
        #     print("Dzielenie przez 0")
        #     sys.exit(1)
        if macierz_rozszerzona[i][i] == 0:
            for k in range(i+1, len(macierz_rozszerzona)):
                if macierz_rozszerzona[k][i] != 0:
                    macierz_rozszerzona[i], macierz_rozszerzona[k] = macierz_rozszerzona[k], macierz_rozszerzona[i]
                    break

        

        wspolczynnik = macierz_rozszerzona[j][i] / macierz_rozszerzona[i][i]

        for k in range(len(macierz_rozszerzona[i])):
            macierz_rozszerzona[j][k] -= wspolczynnik * macierz_rozszerzona[i][k]   


for line in macierz_rozszerzona:
    print(line)


print("=====================================")


wynik = [0 for i in range(len(macierz_rozszerzona))]

for i in range(len(macierz_rozszerzona)-1, -1, -1):
    wynik[i] = macierz_rozszerzona[i][-1]

    for j in range(i+1, len(macierz_rozszerzona)):
        wynik[i] -= macierz_rozszerzona[i][j] * wynik[j]

    wynik[i] = wynik[i] / macierz_rozszerzona[i][i]

for line in enumerate(wynik):
    print(f"x{line[0]}: {line[1]}")