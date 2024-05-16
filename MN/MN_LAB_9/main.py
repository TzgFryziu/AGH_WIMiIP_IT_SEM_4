import numpy as np


def eliminacja_gaussa(A, B):
    n = len(A)

    # Eliminacja wspolczynnikow
    for i in range(n):
        element_pivot = A[i][i]
        for k in range(i + 1, n):
            wspolczynnik = A[k][i] / element_pivot
            for j in range(i, n):
                A[k][j] -= wspolczynnik * A[i][j]
            B[k] -= wspolczynnik * B[i]

    # Ustalanie wartosci zmiennych
    X = [0] * n
    for i in range(n - 1, -1, -1):
        X[i] = B[i] / A[i][i]
        for k in range(i - 1, -1, -1):
            B[k] -= A[k][i] * X[i]

    return X


def wczytaj_dane(sciezka_pliku):
    wezly = []
    wartosci = []
    with open(sciezka_pliku, "r") as plik:
        for linia in plik:
            wezel, wartosc = map(float, linia.split())
            wezly.append(wezel)
            wartosci.append(wartosc)
    return wezly, wartosci


def obliczanie_wspolczynnikow(stopien, x_nodes, y_nodes, weights):
    n = stopien
    m = len(x_nodes) - 1

    g = np.zeros((n + 1, n + 1))
    F = np.zeros(n + 1)

    for k in range(n + 1):
        for j in range(n + 1):
            g[k, j] = sum(
                weights[i] * (x_nodes[i] ** k) * (x_nodes[i] ** j) for i in range(m + 1)
            )

    for k in range(n + 1):
        F[k] = sum(weights[i] * y_nodes[i] * (x_nodes[i] ** k) for i in range(m + 1))

    a = eliminacja_gaussa(g.tolist(), F.tolist())
    return a


def aproksymacja_wielomianowa(x, wspolczynniki):
    n = len(wspolczynniki) - 1
    return sum(wspolczynniki[j] * (x**j) for j in range(n + 1))


def main():
    # wczytaj dane z pliku lab9.txt
    x_nodes, y_nodes = wczytaj_dane("lab9.txt")
    stopien = 1  # aproksymacja liniowa
    weights = [1] * len(x_nodes)

    wspolczynniki = obliczanie_wspolczynnikow(stopien, x_nodes, y_nodes, weights)

    print(f"Liczba węzłów: {len(x_nodes)}")
    print(f"Współczynniki wielomianu aproksymującego: {wspolczynniki}")

    print(f"\nWęzły aproksymacji i wartości w węzłach:")
    for x, y in zip(x_nodes, y_nodes):
        approx_value = aproksymacja_wielomianowa(x, wspolczynniki)
        print(f"x = {x}, y = {y}, F({int(x)}) = {approx_value}")


if __name__ == "__main__":
    main()
