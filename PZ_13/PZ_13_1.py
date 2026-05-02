#В исходном текстовом файле(dates.txt) найти все даты в форматах ДД.ММ.ГГГГ и
#ДД/ММ/ГГГГ. Посчитать количество дат в каждом формате. Поместить в новый
#текстовый файл все даты февраля в формате ДД/ММ/ГГГГ.

import re

with open('dates.txt', 'r', encoding='utf-8') as file:
    text = file.read()

pattern_dot = re.compile(r"[0-3][0-9]\.[0-1][0-9]\.[1-2][0-9][0-9][0-9]")
pattern_slash = re.compile(r"[0-3][0-9]/[0-1][0-9]/[1-2][0-9][0-9][0-9]")

dates_dot = pattern_dot.findall(text)
dates_slash = pattern_slash.findall(text)

count_dot = len(dates_dot)
count_slash = len(dates_slash)

print("Количество дат с точками:", count_dot)
print("Количество дат со слешами:", count_slash)

february_slash = []

for date in dates_dot:
    if ".02." in date:
        new_date = date.replace('.', '/')
        february_slash.append(new_date)

for date in dates_slash:
    if "/02/" in date:
        february_slash.append(date)

with open('result.txt', 'w', encoding='utf-8') as file:
    for d in february_slash:
        file.write(d + '\n')


дипсик

import re

with open('dates.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Регулярные выражения для поиска дат
pattern_dot = re.compile(r"[0-3][0-9]\.[0-1][0-9]\.[1-2][0-9][0-9][0-9]")
pattern_slash = re.compile(r"[0-3][0-9]/[0-1][0-9]/[1-2][0-9][0-9][0-9]")

# Регулярное выражение для поиска февраля в любом формате
# \2 означает, что разделитель должен быть одинаковым (точка или слеш)
pattern_feb = re.compile(r"(\d{2})([./])02\2\d{4}")

dates_dot = pattern_dot.findall(text)
dates_slash = pattern_slash.findall(text)

count_dot = len(dates_dot)
count_slash = len(dates_slash)

print("Количество дат с точками:", count_dot)
print("Количество дат со слешами:", count_slash)

# Поиск всех дат февраля и преобразование их в формат со слешами
february_dates = re.findall(pattern_feb, text)
february_slash = [f"{day}/{month}/{year}" for day, sep, year in february_dates]

with open('result.txt', 'w', encoding='utf-8') as file:
    for d in february_slash:
        file.write(d + '\n')

print(f"Найдено дат февраля: {len(february_slash)}")


переработка чатагпт

import re

with open('dates.txt', 'r', encoding='utf-8') as file:
    text = file.read()

pattern_dot = re.compile(r"[0-3][0-9]\.[0-1][0-9]\.[1-2][0-9][0-9][0-9]")
pattern_slash = re.compile(r"[0-3][0-9]/[0-1][0-9]/[1-2][0-9][0-9][0-9]")

dates_dot = pattern_dot.findall(text)
dates_slash = pattern_slash.findall(text)

count_dot = len(dates_dot)
count_slash = len(dates_slash)

print("Количество дат с точками:", count_dot)
print("Количество дат со слешами:", count_slash)

february_slash = []

for date in dates_dot:
    if re.search(r"\.02\.", date):
        february_slash.append(date.replace('.', '/'))

for date in dates_slash:
    if re.search(r"/02/", date):
        february_slash.append(date)

with open('result.txt', 'w', encoding='utf-8') as file:
    for d in february_slash:
        file.write(d + '\n')
