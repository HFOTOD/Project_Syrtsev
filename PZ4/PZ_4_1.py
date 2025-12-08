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
