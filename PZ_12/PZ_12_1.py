# Ввод матрицы
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Вывод исходной матрицы
print("Исходная матрица:")
print(*matrix, sep="\n")

# Ввод номера столбца
N = int(input("Введите номер столбца N (с 0): "))

# 1. Замена последней строки на нули (list comprehension)
matrix = [
    ([0 for _ in row] if i == len(matrix) - 1 else row)
    for i, row in enumerate(matrix)
]

# 2. Увеличение элементов столбца N в 2 раза (map + lambda)
matrix = list(map(
    lambda row: [
        (x * 2 if j == N else x)
        for j, x in enumerate(row)
    ],
    matrix
))

# Вывод результата
print("\nРезультирующая матрица:")
print(*matrix, sep="\n")
