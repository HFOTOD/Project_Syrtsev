# Дан символ C и строки S, S0. Перед каждым вхождением символа C в строку S вставить строку S0.

try:
    C = input('Введите символ C: ')
    S = input('Введите строку S: ')
    S0 = input('Введите строку S0: ')
except ValueError:
    print('Обнаружена ошибка ввода.')
    exit()

result = ""
for char in S:
    if char == C:
        result += S0 + char
    else:
        result += char

print('Результат:', result)
