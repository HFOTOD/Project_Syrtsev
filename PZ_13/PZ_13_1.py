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