import numpy as np


def read_matrix(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        n = len(lines)
        A = np.zeros((n, n))
        B = np.zeros(n)
        for i in range(n):
            row = lines[i].split()
            for j in range(n):
                A[i][j] = float(row[j])
            B[i] = float(row[n])
        return A, B


def is_diagonally_dominant(matrix):
    n = len(matrix)
    waunek1 = True
    warunek2 = 0
    for i in range(n):
        left = abs(matrix[i][i])
        right = sum(abs(matrix[i][j]) for j in range(n) if j != i)
        if left < right:
            warunek1 = False
        if left > right:
            warunek2 += 1

    return warunek2 or warunek1


def jacobi_method(A, B, iterations):
    n = len(A)
    x = np.zeros(n)

    D = np.diag(np.diag(A))

    L_plus_U = A - D

    D_inv = np.diag(1 / np.diag(D))

    for i in range(iterations):
        x = np.dot(D_inv, B - np.dot(L_plus_U, x))
    return x


def gauss_method(A, B):
    return np.linalg.solve(A, B)


def absolute_error(x1, x2):
    return np.linalg.norm(x1 - x2)


def print_matrices(L_plus_U, D_inv):
    print("\nMacierz L + U:")
    print(L_plus_U)
    print("\nMacierz D^-1:")
    print(D_inv)


def print_solution(x):
    i = 0
    for sol in x:
        print(f"x[{i}] = {sol}")
        i += 1


def main():
    file_name = input("Wpisz nazwe pliku: ")
    iterations = int(input("Wpisz liczbe iteracji: "))
    A, B = read_matrix(file_name)

    print("\nMacierz A (Rozszerzona):")
    print(np.column_stack((A, B)))

    if not is_diagonally_dominant(A):
        print("Macierz A nie jest diagonalnie dominujaca.")
        return

    L_plus_U = A - np.diag(np.diag(A))
    D_inv = np.diag(1 / np.diag(A))

    print_matrices(L_plus_U, D_inv)

    print("\nRozwiazanie po ", iterations, "iteracjach:")
    jacobi_x = jacobi_method(A, B, iterations)
    print_solution(jacobi_x)

    gauss_x = gauss_method(A, B)
    print("\nRozwiazanie metoda Gaussa:")
    print_solution(gauss_x)

    error = absolute_error(jacobi_x, gauss_x)
    print("\nBlad bezwzgledny:", error)


if __name__ == "__main__":
    main()
