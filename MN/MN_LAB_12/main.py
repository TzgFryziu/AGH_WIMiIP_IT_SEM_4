# Przykład użycia
from math import cos,sin

def f1(x):
    return cos(x**3 - 2*x)

def f2(x):
    return sin(x**2 - 1000)

def f3(x):
    return x-1


def bisection_method(f, a, b, epsilon, max_iterations):
    # Sprawdzamy, czy funkcja zmienia znak na końcach przedziału
    if f(a) * f(b) >= 0:
        raise ValueError("Funkcja nie zmienia znaku na końcach przedziału [a, b].")

    iterations = 0
    while (b - a) / 2 > epsilon and iterations < max_iterations:
        x0 = (a + b) / 2
        print(f"Iteracja {iterations}: a = {a}, b = {b}, x0 = {x0}, f(x0) = {f(x0)}")

        if abs(f(x0)) < epsilon:
            return( x0, iterations)
        
        if f(a) * f(x0) < 0:
            b = x0
        else:
            a = x0

        iterations += 1

    return ((a + b) / 2, iterations)


def regula_falsi_method(f, a, b, epsilon, max_iterations):
    if f(a) * f(b) >= 0:
        raise ValueError("Funkcja nie zmienia znaku na końcach przedziału [a, b].")

    x1 = a
    iterations = 0
    while abs(f(x1)) > epsilon and iterations < max_iterations:
        x1 = a - f(a) * (b - a) / (f(b) - f(a))
        print(f"Iteracja {iterations}: a = {a}, b = {b}, x1 = {x1}, f(x1) = {f(x1)}")

        if abs(f(x1)) < epsilon:
            return (x1, iterations)
        
        if f(x1) * f(a) < 0:
            b = x1
        else:
            a = x1

        iterations += 1

    return (x1,iterations)



print("\nMetoda bisekcji dla funkcji cos(x^3 - 2x)")
rozwiazanie_f1_bisekcja = bisection_method(f1, 0, 2, 0.01, 100)
print(f"Znalezione rozwiązanie: x = {rozwiazanie_f1_bisekcja[0]}, f(x) = {f1(rozwiazanie_f1_bisekcja[0])}, liczba iteracji: {rozwiazanie_f1_bisekcja[1]}")

print("\nMetoda bisekcji dla funkcji sin(x^2 - 1000)")
rozwiazanie_f2_bisekcja = bisection_method(f2, 0, 2, 0.01, 100)
print(f"Znalezione rozwiązanie: x = {rozwiazanie_f2_bisekcja[0]}, f(x) = {f2(rozwiazanie_f2_bisekcja[0])}, liczba iteracji: {rozwiazanie_f2_bisekcja[1]}")

print("\nMetoda bisekcji dla funkcji x - 1")
rozwiazanie_f3_bisekcja = bisection_method(f3, -1, 2, 0.01, 100)
print(f"Znalezione rozwiązanie: x = {rozwiazanie_f3_bisekcja[0]}, f(x) = {f3(rozwiazanie_f3_bisekcja[0])}, liczba iteracji: {rozwiazanie_f3_bisekcja[1]}")



print("\nMetoda regula falsi dla funkcji cos(x^3 - 2x)")
rozwiazanie_f1_falsi = regula_falsi_method(f1, 0, 2, 0.01, 100)
print(f"Znalezione rozwiązanie: x = {rozwiazanie_f1_falsi}, f(x) = {f1(rozwiazanie_f1_falsi[0])}, liczba iteracji: {rozwiazanie_f2_bisekcja[1]}")

print("\nMetoda regula falsi  dla funkcji sin(x^2 - 1000)")
rozwiazanie_f2_falsi = regula_falsi_method(f2, 0, 2, 0.01, 100)
print(f"Znalezione rozwiązanie: x = {rozwiazanie_f2_falsi[0]}, f(x) = {f2(rozwiazanie_f2_falsi[0])}, liczba iteracji: {rozwiazanie_f2_bisekcja[1]}")

print("\nMetoda regula falsi  dla funkcji x - 1")
rozwiazanie_f3_falsi = regula_falsi_method(f3, -1, 2, 0.01, 100)
print(f"Znalezione rozwiązanie: x = {rozwiazanie_f3_falsi[0]}, f(x) = {f3(rozwiazanie_f3_falsi[0])}, liczba iteracji: {rozwiazanie_f3_bisekcja[1]}")
