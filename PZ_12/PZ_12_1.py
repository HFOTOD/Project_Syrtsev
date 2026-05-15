#В матрице элементы последней строки заменить на 0.
#В матрице элементы столбца N (N задать с клавиатуры) увеличить в дв

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Исходная матрица:")
print(*matrix, sep="\n")

N = int(input("Введите номер столбца N (с 0): "))

matrix = [
    ([0 for _ in row] if i == len(matrix) - 1 else row)
    for i, row in enumerate(matrix)
]

matrix = list(map(
    lambda row: [
        (x * 2 if j == N else x)
        for j, x in enumerate(row)
    ],
    matrix
))

print("\nРезультирующая матрица:")
print(*matrix, sep="\n")
