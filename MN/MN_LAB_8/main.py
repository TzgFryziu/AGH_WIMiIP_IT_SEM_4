from math import sin, exp, sqrt


def f1(x):
    return sin(x)


def f2(x):
    return x**2 + 2 * x + 5


def f3(x):
    return exp(x)


def kwadratura_gaussa(f, a, b, n, m):
    mnoznik = (b - a) / 2
    if n == 2:
        wezly = [-sqrt(1 / 3), sqrt(1 / 3)]
        wagi_wezlow = [1, 1]
    elif n == 3:
        wezly = [-sqrt(3 / 5), 0, sqrt(3 / 5)]
        wagi_wezlow = [5 / 9, 8 / 9, 5 / 9]
    elif n == 4:
        wezly = [
            -(1 / 35) * sqrt(525 + 70 * sqrt(30)),
            -(1 / 35) * sqrt(525 - 70 * sqrt(30)),
            (1 / 35) * sqrt(525 - 70 * sqrt(30)),
            (1 / 35) * sqrt(525 + 70 * sqrt(30)),
        ]
        wagi_wezlow = [
            1 / 36 * (18 - sqrt(30)),
            1 / 36 * (18 + sqrt(30)),
            1 / 36 * (18 + sqrt(30)),
            1 / 36 * (18 - sqrt(30)),
        ]
    else:
        raise ValueError("Invalid value of n")

    calka = 0
    dlugosc_podprzedzialu = (b - a) / m
    for i in range(m):
        suma = 0
        a_i = a + i * dlugosc_podprzedzialu
        b_i = a_i + dlugosc_podprzedzialu
        for wezel in wezly:
            ti = (a_i + b_i) / 2 + (b_i - a_i) / 2 * wezel
            suma += wagi_wezlow[wezly.index(wezel)] * f(ti)
        calka += suma

    return calka * dlugosc_podprzedzialu / 2


print("Funkcja sin(x) na przedziale [0.5, 2.5]:")
print(kwadratura_gaussa(f1, 0.5, 2.5, 2, 20))
print(kwadratura_gaussa(f1, 0.5, 2.5, 3, 20))
print(kwadratura_gaussa(f1, 0.5, 2.5, 4, 20))

print("Funkcja x^2 + 2x + 5 na przedziale [0.5, 5]:")
print(kwadratura_gaussa(f2, 0.5, 5, 2, 20))
print(kwadratura_gaussa(f2, 0.5, 5, 3, 20))
print(kwadratura_gaussa(f2, 0.5, 5, 4, 20))

print("Funkcja exp(x) na przedziale [0.5, 5]:")
print(kwadratura_gaussa(f3, 0.5, 5, 2, 20))
print(kwadratura_gaussa(f3, 0.5, 5, 3, 20))
print(kwadratura_gaussa(f3, 0.5, 5, 4, 20))
