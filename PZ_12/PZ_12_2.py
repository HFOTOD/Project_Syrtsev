import random

# 1. Автоматическая генерация матрицы (задаем сами)
rows = 4
cols = 4

matrix = [[random.randint(1, 9) for _ in range(cols)] for _ in range(rows)]

print("Исходная матрица:")
print(*matrix, sep="\n")

N = int(input(f"\nВведите номер столбца N (от 0 до {cols - 1}): "))

# 2. ЗАДАНИЕ 1: Замена последней строки на 0
matrix = [
    ([0 for _ in row] if i == len(matrix) - 1 else [x for x in row])
    for i, row in enumerate(matrix)
]

# 3. ЗАДАНИЕ 2: Увеличение элементов столбца N в два раза
matrix = list(map(
    lambda row: [
        (x * 2 if j == N else x)
        for j, x in enumerate(row)
    ],
    matrix
))

print("\nРезультирующая матрица:")
print(*matrix, sep="\n")
