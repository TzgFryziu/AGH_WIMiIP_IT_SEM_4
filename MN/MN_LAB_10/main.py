import numpy as np
import matplotlib.pyplot as plt

# Definiowanie funkcji dla równań różniczkowych
def funkcja1(x, y):
    return 2 * y * (x + 1)

def funkcja2(x, y):
    return x + y

def exact_f1(x):
    return np.exp(x**2+2*x)

def exact_f2(x):
    return -x -1 + 1.1*np.exp(x)

# Metoda Eulera
def metoda_eulera(f, x0, y0, x_koniec, N):
    h = (x_koniec - x0) / N
    x = x0
    y = y0
    for _ in range(N):
        y += h * f(x, y)
        x += h
    return y

# Metoda Rungego-Kutty 2. rzędu
def metoda_rk2(f, x0, y0, x_koniec, N):
    h = (x_koniec - x0) / N
    x = x0
    y = y0
    for _ in range(N):
        k1 = f(x, y)
        k2 = f(x + h, y + h * k1)
        y += h * 0.5 * (k1 + k2)
        x += h
    return y

# Metoda Rungego-Kutty 4. rzędu
def metoda_rk4(f, x0, y0, x_koniec, N):
    h = (x_koniec - x0) / N
    x = x0
    y = y0
    for _ in range(N):
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h / 2 * k1)
        k3 = f(x + h / 2, y + h / 2 * k2)
        k4 = f(x + h, y + h * k3)
        y += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x += h
    return y

# Funkcja do rozwiązywania i wyświetlania wyników
def rozwiaz_rownanie(f, x0, y0, x_koniec, N, dokladne_rozwiazanie):
    rozwiazanie_eulera = metoda_eulera(f, x0, y0, x_koniec, N)
    rozwiazanie_rk2 = metoda_rk2(f, x0, y0, x_koniec, N)
    rozwiazanie_rk4 = metoda_rk4(f, x0, y0, x_koniec, N)
    print(f"Warunek początkowy: y({x0}) = {y0}")
    print(f"Punkt końcowy: x = {x_koniec}")
    print(f"Krok obliczeń: h = {(x_koniec - x0) / N}")
    print(f"Rozwiązanie metodą Eulera: y({x_koniec}) = {rozwiazanie_eulera}")
    print(f"Rozwiązanie metodą RK2: y({x_koniec}) = {rozwiazanie_rk2}")
    print(f"Rozwiązanie metodą RK4: y({x_koniec}) = {rozwiazanie_rk4}")
    print(f"Rozwiązanie dokładne: {dokladne_rozwiazanie(x_koniec)}")


# Rozwiązywanie danych problemów
print("Rozwiązywanie y' = 2y(x+1), y(0) = 1.0 przy x = 1 dla N = 10")
rozwiaz_rownanie(funkcja1, 0, 1.0, 1, 10,exact_f1)

print("\nRozwiązywanie y' = x + y, y(0) = 0.1 przy x = 1 dla N = 10")
rozwiaz_rownanie(funkcja2, 0, 0.1, 1, 10,exact_f2)

# Badanie zbieżności
def badanie_zbieznosci(f, x0, y0, x_koniec, dokladne_rozwiazanie):
    wartosci_N = [10, 20, 50, 100, 150,200,300,500,1000]
    wyniki_eulera = []
    wyniki_rk2 = []
    wyniki_rk4 = []
    ex = [dokladne_rozwiazanie(x_koniec) for _ in wartosci_N]
    for N in wartosci_N:
        rozwiazanie_eulera = metoda_eulera(f, x0, y0, x_koniec, N)
        rozwiazanie_rk2 = metoda_rk2(f, x0, y0, x_koniec, N)
        rozwiazanie_rk4 = metoda_rk4(f, x0, y0, x_koniec, N)
        wyniki_eulera.append(rozwiazanie_eulera)
        wyniki_rk2.append(rozwiazanie_rk2)
        wyniki_rk4.append(rozwiazanie_rk4)
    plt.plot(wartosci_N, wyniki_eulera, label='Metoda Eulera')
    plt.plot(wartosci_N, wyniki_rk2, label='Metoda RK2')
    plt.plot(wartosci_N, wyniki_rk4, label='Metoda RK4')
    plt.plot(wartosci_N, ex, label='Dokładne rozwiązanie')
    plt.xlabel('N')
    plt.ylabel('Rozwiązanie')
    plt.title('Badanie zbieżności')
    plt.legend()
    plt.show()


badanie_zbieznosci(funkcja1, 0, 1.0, 1, exact_f1)

badanie_zbieznosci(funkcja2, 0, 0.1, 1, exact_f2)
