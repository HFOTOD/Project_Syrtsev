# Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из результата вновь вычли сумму его цифр и т. д. Через сколько таких действий получится нуль?

def count_steps_to_zero(n):
    steps = 0
    while n > 0:
        digit_sum = sum(int(digit) for digit in str(n))
        n -= digit_sum
        steps += 1
    return steps

number = input("Введите целое положительное число: ")
while True:
    try:
        number = int(number)
        if number <= 0:
            print("Число должно быть положительным!")
            number = input("Введите целое положительное число: ")
        else:
            break
    except ValueError:
        print("Неверный ввод! Введите целое число.")
        number = input("Введите целое положительное число: ")

result = count_steps_to_zero(number)
print(f"Количество шагов до нуля: {result}")
