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






import sqlite3 as sq

# Данные для заполнения таблицы (список кортежей)
# Структура: (id, ФИО мастера, ФИО клиента, пол (1-муж, 2-жен), название стрижки, стоимость)
info_services = [
    (1, 'Смирнов А.В.', 'Иванов И.И.', 1, 'Бокс', 500),
    (2, 'Попова Е.А.', 'Сидорова В.В.', 2, 'Каре', 1500),
    (3, 'Смирнов А.В.', 'Петров П.П.', 1, 'Полубокс', 600),
    (4, 'Ильин И.И.', 'Алексеева А.А.', 2, 'Каскад', 1200)
]

# [span_2](start_span)Подключение к БД через менеджер контекста[span_2](end_span)
with sq.connect('barbershop.db') as con:
    cur = con.cursor()

    # Удаляем таблицу, если она уже существует (для чистоты эксперимента при перезапусках)
    cur.execute("DROP TABLE IF EXISTS services")

    # 1. [span_3](start_span)СОЗДАНИЕ ТАБЛИЦЫ[span_3](end_span)
    # [span_4](start_span)Используем AUTOINCREMENT для первичного ключа и DEFAULT для пола[span_4](end_span)
    cur.execute("""CREATE TABLE IF NOT EXISTS services (
        service_id INTEGER PRIMARY KEY AUTOINCREMENT,
        master_name TEXT NOT NULL,
        client_name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        haircut_name TEXT,
        price INTEGER
    )""")

    # 2. ЗАПОЛНЕНИЕ БД (INSERT)
    # [span_5](start_span)Используем executemany для массового добавления данных из списка[span_5](end_span)
    cur.executemany("INSERT INTO services VALUES (?, ?, ?, ?, ?, ?)", info_services)

    # 3. [span_6](start_span)ВЫБОРКА ДАННЫХ (SELECT)[span_6](end_span)
    print("--- Все стрижки дороже 550 рублей (сортировка по убыванию цены) ---")
    # [span_7](start_span)Используем WHERE для фильтрации и ORDER BY DESC для сортировки по убыванию[span_7](end_span)
    cur.execute("SELECT * FROM services WHERE price > 550 ORDER BY price DESC")
    
    # [span_8](start_span)Перебираем результат, используя Cursor в качестве итерируемого объекта[span_8](end_span)
    for result in cur:
        print(result)

    # 4. [span_9](start_span)ОБНОВЛЕНИЕ ДАННЫХ (UPDATE)[span_9](end_span)
    # Увеличим стоимость мужских стрижек (sex = 1) на 100 рублей
    cur.execute("UPDATE services SET price = price + 100 WHERE sex = 1")

    # 5. [span_10](start_span)[span_11](start_span)УДАЛЕНИЕ ДАННЫХ (DELETE)[span_10](end_span)[span_11](end_span)
    # Удалим запись с id = 4
    cur.execute("DELETE FROM services WHERE service_id = 4")

    # Итоговый вывод таблицы после всех изменений
    print("\n--- Итоговое состояние таблицы (после UPDATE и DELETE) ---")
    cur.execute("SELECT * FROM services")
    [span_12](start_span)final_result = cur.fetchall() # Получаем все записи в виде списка[span_12](end_span)
    for row in final_result:
        print(row)
