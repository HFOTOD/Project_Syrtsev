#Сумма квадратов от N до 2N
while True:
    try:
        N = int(input("Введите целое число N (> 0): "))
        if N <= 0:
            print("Ошибка: N должно быть положительным целым числом.")
            continue
        break
    except ValueError:
        print("Ошибка: введите корректное целое число.")

total_sum = 0
for i in range(N, 2 * N + 1):
    total_sum += i * i

print(f"Сумма квадратов от {N} до {2 * N}: {total_sum}")


#Банковский вклад с ежемесячным начислением процентов
while True:
    try:
        P = float(input("Введите процентную ставку P (0 < P < 25): "))
        if not (0 < P < 25):
            print("Ошибка: P должно быть числом в диапазоне от 0 до 25 (не включая границы).")
            continue
        break
    except ValueError:
        print("Ошибка: введите корректное число.")

initial_deposit = 1000.0
current_deposit = initial_deposit
months = 0

while current_deposit <= 1100.0:
    months += 1
    current_deposit += current_deposit * (P / 100.0)

K = months
S = current_deposit

print(f"Количество месяцев K: {K}")
print(f"Итоговый размер вклада S: {S:.2f} руб.")