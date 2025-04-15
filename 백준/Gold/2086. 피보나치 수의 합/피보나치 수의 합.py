import sys

MOD = 1000000000

def matrix_multiply(a, b):
    return [
        [(a[0][0] * b[0][0] + a[0][1] * b[1][0]) % MOD, (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % MOD],
        [(a[1][0] * b[0][0] + a[1][1] * b[1][0]) % MOD, (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % MOD]
    ]

def matrix_power(matrix, n):
    if n == 1:
        return matrix
    if n % 2 == 0:
        half = matrix_power(matrix, n // 2)
        return matrix_multiply(half, half)
    else:
        return matrix_multiply(matrix, matrix_power(matrix, n - 1))

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    result_matrix = matrix_power([[1, 1], [1, 0]], n - 1)
    return result_matrix[0][0]

def fibonacci_sum(n):
    return (fibonacci(n + 2) - 1 + MOD) % MOD

def range_sum(a, b):
    return (fibonacci_sum(b) - fibonacci_sum(a - 1) + MOD) % MOD

input = sys.stdin.readline
print = sys.stdout.write

a, b = map(int, input().split())

result = range_sum(a, b)
print(f"{result}\n")