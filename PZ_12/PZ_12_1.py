#В матрице элементы последней строки заменить на 0.
#В матрице элементы столбца N (N задать с клавиатуры) увеличить в дв

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Исходная матрица:")
print(*matrix, sep="\n")

N = int(input("Введите номер столбца N (с 0): "))

matrix = [
    ([0 for _ in row] if i == len(matrix) - 1 else row)
    for i, row in enumerate(matrix)
]

matrix = list(map(
    lambda row: [
        (x * 2 if j == N else x)
        for j, x in enumerate(row)
    ],
    matrix
))

print("\nРезультирующая матрица:")
print(*matrix, sep="\n")






import sqlite3 as sq  # Раздаточный материал №6

# Подготовим демонстрационные данные для вставки (список кортежей)
# Порядок полей: id, ФИО мастера, ФИО клиента, пол (1-муж, 2-жен), стрижка, стоимость
info_services = [
    (1, 'Иванов А.А.', 'Петров В.В.', 2, 'Полубокс', 500),
    (2, 'Смирнова О.И.', 'Сидорова К.К.', 1, 'Каре', 1200),
    (3, 'Иванов А.А.', 'Макаров Е.П.', 2, 'Цезарь', 700),
    (4, 'Кузнецов С.П.', 'Павлова М.А.', 1, 'Каскад', 1500)
]

# Подключение к БД через менеджер контекста (автоматически делает commit и close)
with sq.connect('barbershop.db') as con:  # Раздаточный материал №6, №7
    cur = con.cursor()  # Раздаточный материал №6

    # Удаляем таблицу, если она осталась от прошлых запусков скрипта
    cur.execute("DROP TABLE IF EXISTS services")  # Раздаточный материал №8

    # 1. СОЗДАНИЕ ТАБЛИЦЫ "Услуги" (services)
    # Поля строго по варианту: ФИО мастера, ФИО клиента, пол, название стрижки, стоимость.
    # Дополнительно добавлен первичный ключ (PRIMARY KEY AUTOINCREMENT) по аналогии с лекцией.
    cur.execute("""CREATE TABLE IF NOT EXISTS services (
        service_id INTEGER PRIMARY KEY AUTOINCREMENT,
        master_name TEXT NOT NULL,
        client_name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        haircut_name TEXT,
        price INTEGER
    )""")  # Раздаточный материал №6, №8

    # 2. ЗАПОЛНЕНИЕ БД (INSERT)
    # Используем метод executemany и подстановку знаков '?'
    cur.executemany("INSERT INTO services VALUES (?, ?, ?, ?, ?, ?)", info_services)  # Раздаточный материал №12

    # 3. ВЫБОРКА ДАННЫХ (SELECT) С ФИЛЬТРАЦИЕЙ И СОРТИРОВКОЙ
    # Выберем услуги дороже 600 рублей и отсортируем по убыванию стоимости (DESC)
    print("--- Выборка услуг (price > 600) с сортировкой по убыванию стоимости ---")
    cur.execute("SELECT * FROM services WHERE price > 600 ORDER BY price DESC")  # Раздаточный материал №14, №18
    
    # Перебор результатов, используя Cursor в качестве итерируемого объекта (экономит память)
    for result in cur:  # Раздаточный материал №20
        print(result)

    # 4. ОБНОВЛЕНИЕ ДАННЫХ (UPDATE)
    # Изменим стоимость стрижки с названием 'Полубокс' (установим 600 рублей)
    cur.execute("UPDATE services SET price = 600 WHERE haircut_name LIKE 'Полубокс'")  # Раздаточный материал №22, №24

    # 5. УДАЛЕНИЕ ДАННЫХ (DELETE)
    # Удалим запись, где service_id равен 4
    cur.execute("DELETE FROM services WHERE service_id = 4")  # Раздаточный материал №25, №26

    # Проверим итоговое состояние базы через метод fetchall()
    print("\n--- Итоговое состояние таблицы после UPDATE и DELETE ---")
    cur.execute("SELECT * FROM services")
    final_result = cur.fetchall()  # Раздаточный материал №19
    for row in final_result:
        print(row)
