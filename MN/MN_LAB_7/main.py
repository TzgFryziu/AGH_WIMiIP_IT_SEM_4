from math import sin, exp


def f1(x):
    return sin(x)


def f2(x):
    return x**2 + 2 * x + 5


def f3(x):
    return exp(x)


def metoda_prostokatow(f, a, b, n):
    suma = 0
    s = (b - a) / n
    for i in range(n):
        suma += f((a + i * s) + 0.5 * s)
    return s * suma


def metoda_trapezow(f, a, b, n):
    suma = 0
    s = (b - a) / n

    for i in range(n):
        x = a + i * s
        suma += (x + s - x) / 2 * (f(x) + f(x + s))
    return suma


def metoda_simpsona(f, a, b, n):
    suma = 0
    s = (b - a) / n
    for i in range(n):
        x = a + i * s
        suma += (s / 6) * (f(x) + 4 * f(x + 0.5 * s) + f(x + s))
    return suma


# print("Rozwiazanie calki 1 metoda prostokatow: ", end="")
# print(metoda_prostokatow(f1, 0.5, 2.5, 4))
# print("Rozwiazanie calki 1 metoda trapezow: ", end="")
# print(metoda_trapezow(f1, 0.5, 2.5, 4))
# print("Rozwiazanie calki 1 metoda simpsona: ", end="")
# print(metoda_simpsona(f1, 0.5, 2.5, 4))
# print("Rozwiazanie calki 2 metoda prostokatow: ", end="")
# print(metoda_prostokatow(f2, 0.5, 5, 4))
# print("Rozwiazanie calki 2 metoda trapezow: ", end="")
# print(metoda_trapezow(f2, 0.5, 5, 4))
# print("Rozwiazanie calki 2 metoda simpsona: ", end="")
# print(metoda_simpsona(f2, 0.5, 5, 4))
# print("Rozwiazanie calki 3 metoda prostokatow: ", end="")
# print(metoda_prostokatow(f3, 0.5, 5, 4))
# print("Rozwiazanie calki 3 metoda trapezow: ", end="")
# print(metoda_trapezow(f3, 0.5, 5, 4))
# print("Rozwiazanie calki 3 metoda simpsona: ", end="")
# print(metoda_simpsona(f3, 0.5, 5, 4))

# for i in range(1, 11):
#     print(metoda_prostokatow(f3, 0.5, 5, i * 5))

# print("\n")
# for i in range(1, 11):
#     print(metoda_trapezow(f3, 0.5, 5, i * 5))
# print("\n")
# for i in range(1, 11):
#     print(metoda_simpsona(f3, 0.5, 5, i * 5))
print("Funkcja sin(x) na przedziale [0.5, 2.5] n = 20:")
print("Metoda prostokatow: ", metoda_prostokatow(f1, 0.5, 2.5, 20))
print("Metoda trapezow: ", metoda_trapezow(f1, 0.5, 2.5, 20))
print("Metoda simpsona: ", metoda_simpsona(f1, 0.5, 2.5, 20))
print("\n")
print("Funkcja x^2 + 2x + 5 na przedziale [0.5, 5] n = 20:")
print("Metoda prostokatow: ", metoda_prostokatow(f2, 0.5, 5, 20))
print("Metoda trapezow: ", metoda_trapezow(f2, 0.5, 5, 20))
print("Metoda simpsona: ", metoda_simpsona(f2, 0.5, 5, 20))
print("\n")
print("Funkcja exp(x) na przedziale [0.5, 5] n = 20:")
print("Metoda prostokatow: ", metoda_prostokatow(f3, 0.5, 5, 20))
print("Metoda trapezow: ", metoda_trapezow(f3, 0.5, 5, 20))
print("Metoda simpsona: ", metoda_simpsona(f3, 0.5, 5, 20))
# print("Dokladne rozwiazanie calki sin(x) na przedziale [0.5, 2.5]: ")
# print("1.67873")
# print("Dokladne rozwiazanie calki x^2 + 2x + 5 na przedziale [0.5, 5]: ")
# print("88.875")
# print("Dokladne rozwiazanie calki exp(x) na przedziale [0.5, 5]: ")
# print("146.764")
