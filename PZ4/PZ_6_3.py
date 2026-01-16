# Дано множество A из N точек (N > 2), точки заданы своими координатами x, y. Найти наименьший периметр треугольника, вершины которого принадлежат различным точкам множества A, и сами эти точки (точки выводятся в том же порядке, в котором они перечислены при задании множества A).

import random
import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

n = int(input('Введите количество точек N (> 2): '))
points = [(random.randint(-10, 10), random.randint(-10, 10)) for _ in range(n)]

print('Множество точек A:')
for p in points:
    print(p, end=' ')
print()

min_perim = float('inf')
tri = None

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            perim = dist(x1, y1, x2, y2) + dist(x2, y2, x3, y3) + dist(x3, y3, x1, y1)
            if perim < min_perim:
                min_perim = perim
                tri = (points[i], points[j], points[k])

print('Наименьший периметр треугольника:', round(min_perim, 2))
print('Точки треугольника (в порядке ввода):', tri)
