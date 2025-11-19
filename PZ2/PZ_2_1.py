while True:
    N = input("Введи количество секунд с начала суток (только цифры): ")
    N = int(N)
    seconds_in_current_hour = N % 3600
    full_minutes = seconds_in_current_hour // 60
    print(f"Полных минут с начала последнего часа: {full_minutes}")
    break
