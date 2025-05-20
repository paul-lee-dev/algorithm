MOD = 1000000007

def matrix_multiply(a, b):
    return [[(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % MOD, (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % MOD],
            [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % MOD, (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % MOD]]

def matrix_power(matrix, n):
    if n == 1:
        return matrix
    if n % 2 == 0:
        half = matrix_power(matrix, n // 2)
        return matrix_multiply(half, half)
    return matrix_multiply(matrix, matrix_power(matrix, n - 1))

def fibonacci_square_sum(n):
    if n == 0:
        return 0
    matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(matrix, n)
    fib_n = result_matrix[0][0]
    fib_n_plus_1 = result_matrix[0][1]
    return (fib_n * fib_n_plus_1) % MOD

n = int(input())
print(fibonacci_square_sum(n))