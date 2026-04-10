#Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной последовательности из целых положительных и отрицательных чисел. 
#Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов: 
#Элементы первого и второго файлов: 
#Среднее арифметическое элементов первого и второго файлов: 
#Количество нечетных элементов первого и второго файлов: Элементы общие для двух файлов: Количество элементов, общих для двух файлов:

l1 = ['-5 10 3 -8 7 2']
l2 = ['4 -8 7 15 -5 20']

f1 = open('file1.txt', 'w')
f1.writelines(l1)
f1.close()

f2 = open('file2.txt', 'w')
f2.writelines(l2)
f2.close()

f1 = open('file1.txt')
a = f1.read().split()
f1.close()

f2 = open('file2.txt')
b = f2.read().split()
f2.close()

for i in range(len(a)):
    a[i] = int(a[i])

for i in range(len(b)):
    b[i] = int(b[i])

avg1 = sum(a) / len(a)
avg2 = sum(b) / len(b)

odd1 = 0
for x in a:
    if x % 2 != 0:
        odd1 += 1

odd2 = 0
for x in b:
    if x % 2 != 0:
        odd2 += 1

common = []
for x in a:
    if x in b and x not in common:
        common.append(x)

f3 = open('result1.txt', 'w')

f3.write('Элементы первого файла: ' + str(a) + '\n')
f3.write('Элементы второго файла: ' + str(b) + '\n')

f3.write('Среднее арифметическое:\n')
f3.write('Первый файл: ' + str(avg1) + '\n')
f3.write('Второй файл: ' + str(avg2) + '\n')

f3.write('Количество нечетных:\n')
f3.write('Первый файл: ' + str(odd1) + '\n')
f3.write('Второй файл: ' + str(odd2) + '\n')

f3.write('Общие элементы: ' + str(common) + '\n')
f3.write('Количество общих элементов: ' + str(len(common)) + '\n')

f3.close()
