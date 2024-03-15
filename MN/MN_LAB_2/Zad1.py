dane = []
with open("Dane.txt", 'r') as f:
    for wezel in f:
        temp = wezel.strip().split(" ")
        dane.append([float(temp[0]), float(temp[1])])

n = len(dane)

wspolczynniki = []

p0 = 1


def oblicz_pk(k, user_input):
    result = 1
    for i in range(0, k):
        result *= (user_input - dane[i][0])
    return result


b0 = dane[0][1]


def oblicz_mianownik_bk(k, i):
    result = 1
    for j in range(0, k+1):
        if j != i:
            result *= (dane[i][0] - dane[j][0])
    return result


def oblicz_bk(k):
    result = 0
    for i in range(0, k+1):
        result += (dane[i][1] / oblicz_mianownik_bk(k, i))
    wspolczynniki.append(result)
    return result


def interpolacja_newtona(val):
    result = b0 * p0
    for i in range(1, n):
        result += (oblicz_bk(i) * oblicz_pk(i, val))
    return result


user_input = float(input("Wpisz x: "))

output = interpolacja_newtona(user_input)

print(f"Liczba wezlow: {n}")
print("Dane: ")
for x in dane:
    print(x)
print(f"Punkt w ktorym liczymy wartosc wielomianu: {user_input}")
print(f"Wartosc wielomianu Newtona w punkcie {user_input}: {output}")
print(f"Wspolczynniki:",end=" ")
for x in wspolczynniki:
    print(x,end=" ")
