import numpy as np


def read_matrix(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        n = len(lines) - 1
        A = np.zeros((n, n))
        B = np.zeros(n)
        for i in range(n):
            row = lines[i + 1].split()
            for j in range(n):
                A[i][j] = float(row[j])
            B[i] = float(row[n])
        return A, B


def is_diagonally_dominant(matrix):
    n = len(matrix)
    for i in range(n):
        if not (
            2 * abs(matrix[i][i]) > sum(abs(matrix[i][j]) for j in range(n) if j != i)
        ):
            return False
    return True


def jacobi_method(A, B, iterations):
    n = len(A)
    x = np.zeros(n)
    L_plus_U = A - np.diag(np.diag(A))
    D_inv = np.diag(1 / np.diag(A))
    for i in range(iterations):
        x = np.dot(D_inv, B - np.dot(L_plus_U, x))
    return x


def gauss_method(A, B):
    return np.linalg.solve(A, B)


def absolute_error(x1, x2):
    return np.linalg.norm(x1 - x2)


def print_matrices(L_plus_U, D_inv):
    print("L + U:")
    print(L_plus_U)
    print("\nD^-1:")
    print(D_inv)


def print_solution(x, iterations):
    print("\nSolution after", iterations, "iterations:")
    print(x)


def main():
    file_name = input("Enter the file name containing the matrix: ")
    iterations = int(input("Enter the number of iterations: "))
    A, B = read_matrix(file_name)

    print("\nMatrix A (augmented):")
    print(np.column_stack((A, B)))

    if not is_diagonally_dominant(A):
        print("Matrix A is not diagonally dominant.")
        return

    L_plus_U = A - np.diag(np.diag(A))
    D_inv = np.diag(1 / np.diag(A))

    print_matrices(L_plus_U, D_inv)

    jacobi_x = jacobi_method(A, B, iterations)
    print_solution(jacobi_x, iterations)

    gauss_x = gauss_method(A, B)
    print("\nSolution using Gauss method:")
    print(gauss_x)

    error = absolute_error(jacobi_x, gauss_x)
    print("\nAbsolute error between Jacobi and Gauss solutions:", error)


if __name__ == "__main__":
    main()