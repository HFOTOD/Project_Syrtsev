N = int(input("Введите количество секунд с начала суток: "))
seconds_in_current_hour = N % 3600
full_minutes = seconds_in_current_hour // 60
print(f"Количество полных минут с начала последнего часа: {full_minutes}")