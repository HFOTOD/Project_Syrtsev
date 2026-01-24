# Дан список A размера N. Найти максимальный элемент из его элементов с нечетными номерами: A₁, A₃, A₅, ...

import random

while True:
    try:
        n = int(input('Введите размер списка: '))
        if n < 0:
            print('Пожалуйста, введите неотрицательное число.')
            continue
        break
    except ValueError:
        print('Ошибка: пожалуйста, введите целое число.')

A = [random.randint(1, 100) for _ in range(n)]
print('Исходный список:', A)
odd_index_elements = [A[i] for i in range(0, n, 2)]

try:
    max_val = max(odd_index_elements)
    print('Максимальный элемент с нечётным номером:', max_val)
except ValueError:
    print('Нет элементов с нечетным номером для поиска.')
