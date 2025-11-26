#С начала суток прошло N секунд (N-целое). Найти количество полных минут, прошедших с начала последнего времени.
while True:
    try:
        N = input("Введи количество секунд с начала суток: ")
        N = int(N)
        break
    except ValueError:
        print("Ошибка: введите число")

seconds_in_current_hour = N % 3600
full_minutes = seconds_in_current_hour // 60
print("Полных минут с начала последнего часа: ", full_minutes)
