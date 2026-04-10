#Из предложенного текстового файла (text18-28.txt) вывести на экран его содержимое, количество символов в тексте. 
#Сформировать новый файл, в который поместить текст в стихотворной форме предварительно вставив после строки N (N- задается пользователем) произвольную фразу.

N = int(input('Введите номер строки N: '))

symbols = 0

for line in open('text18-28.txt', encoding='UTF-8'):
    print(line, end='')
    symbols += len(line)

print('\nКоличество символов:', symbols)

f1 = open('text18-28.txt', encoding='UTF-8')
lines = f1.readlines()
f1.close()

phrase = '*** Заменил ***\n'

if N < len(lines):
    lines.insert(N + 1, phrase)
else:
    lines.append(phrase)

f2 = open('result2.txt', 'w', encoding='UTF-8')
f2.writelines(lines)
f2.close()
