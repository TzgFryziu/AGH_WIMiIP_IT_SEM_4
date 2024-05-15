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


def jacobi_method(A, B, epsilon, max_iterations):
    iterations = 0
    n = len(A)
    x = np.zeros(n)

    D = np.diag(np.diag(A))

    L_plus_U = A - D

    D_inv = np.diag(1 / np.diag(D))

    for _ in range(max_iterations):
        iterations += 1
        x_new = np.dot(D_inv, B - np.dot(L_plus_U, x))
        if np.linalg.norm(x_new - x) < epsilon:
            break
        x = x_new
    return x, iterations


def absolute_error(x1, x2):
    return np.linalg.norm(x1 - x2)


def print_matrices(L_plus_U, D_inv):
    print("\nMcierz L + U:")
    print(L_plus_U)
    print("\nMacierz D^-1:")
    print(D_inv)


def print_solution(x, iterations, epsilon):
    print("\nRozwiazanie po ", iterations, "iteracjach gdzie epsilon =", epsilon, ":")
    i = 0
    for sol in x:
        print(f"x[{i}] = {sol}")
        i += 1


def main():
    file_name = input("Wpisz nazwe pliku: ")
    epsilon_values = [0.001, 0.000001]
    max_iterations = 1000000
    A, B = read_matrix(file_name)

    print("\nMacierz A (Rozszerzona):")
    print(np.column_stack((A, B)))

    if not is_diagonally_dominant(A):
        print("Macierz A nie jest diagonalnie dominujaca.")
        return

    L_plus_U = A - np.diag(np.diag(A))
    D_inv = np.diag(1 / np.diag(A))

    print_matrices(L_plus_U, D_inv)

    for epsilon in epsilon_values:
        jacobi_x, jacobi_iterations = jacobi_method(A, B, epsilon, max_iterations)
        print_solution(jacobi_x, jacobi_iterations, epsilon)


if __name__ == "__main__":
    main()
