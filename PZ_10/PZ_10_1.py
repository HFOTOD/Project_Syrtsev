d = 0
t = 0

for i in open('text18-1.txt', encoding='UTF-8'):
    print(i, end='')
    t += 1
    for j in i:
        if j == 'ж':
            d += 1

print(end='\n')
print('Количество строк:', t)
print('Количество букв "ж":', d)