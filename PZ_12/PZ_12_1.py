import random

rows, cols = 4, 4
matrix = [[random.randint(1, 9) for _ in range(cols)] for _ in range(rows)]

print("Исходная матрица:")
for row in (r for r in matrix):
    print(row)

matrix = [[(0 if i == len(matrix) - 1 else matrix[i][j])
           for j in range(cols)]
          for i in range(len(matrix))]

N = int(input(f"\nВведите номер столбца N (от 0 до {cols - 1}): "))

matrix = [[(row[j] * 2 if j == N else row[j])
           for j in range(cols)]
          for row in matrix]

print("\nРезультирующая матрица:")
for row in (r for r in matrix):
    print(row)
