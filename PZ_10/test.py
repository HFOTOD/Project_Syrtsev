#Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной последовательности из целых положительных и отрицательных чисел. 
#Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов: Элементы первого и второго файлов: 
#Среднее арифметическое элементов первого и второго файлов: Количество нечетных элементов первого и второго файлов: 
#Элементы общие для двух файлов: Количество элементов, общих для двух файлов:

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
for i in range(len(a)):
    a[i] = int(a[i])
f1.close()

f2 = open('file2.txt')
b = f2.read().split()
for i in range(len(b)):
    b[i] = int(b[i])
f2.close()

all_numbers = a + b
avg = sum(all_numbers) / len(all_numbers)
odd_count = 0

for x in all_numbers:
    if x % 2 != 0:
        odd_count += 1

common = []
for x in a:
    if x in b and x not in common:
        common.append(x)

f3 = open('result1.txt', 'w')

f3.write('Элементы первого и второго файлов:\n')
f3.write(str(all_numbers) + '\n')
f3.write('Среднее арифметическое: ' + str(avg) + '\n')
f3.write('Количество нечетных элементов: ' + str(odd_count) + '\n')
f3.write('Общие элементы: ' + str(common) + '\n')
f3.write('Количество общих элементов: ' + str(len(common)) + '\n')

f3.close()

#Из предложенного текстового файла (text18-28.txt) вывести на экран его содержимое, количество символов в тексте. 
#Сформировать новый файл, в который поместить текст в стихотворной форме предварительно вставив после строки N (N – задается пользователем) произвольную фразу.
N = int(input('Введите номер строки N: '))

symbols = 0

for line in open('text18-28.txt', encoding='UTF-8'):
    print(line, end='')
    for ch in line:
        symbols += 1

print('\nКоличество символов:', symbols)

f1 = open('text18-28.txt', encoding='UTF-8')
lines = f1.readlines()
f1.close()

phrase = '*** ВСТАВЛЕННАЯ СТРОКА ***\n'

if N < len(lines):
    lines.insert(N, phrase)
else:
    lines.append(phrase)
  
f2 = open('result2.txt', 'w')
f2.writelines(lines)
f2.close()
