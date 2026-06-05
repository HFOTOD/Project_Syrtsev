#Приложение ПАРИКМАХЕРСКАЯ для некоторой организации. 
#БД должна содержать таблицу Услуги со следующей структурой записи: 
#ФИО мастера, ФИО клиента, пол, название стрижки, стоимость.

import sqlite3 as sq

info_services = [
    (1, 'Иванов А.А.', 'Петров В.В.', 2, 'Полубокс', 500),
    (2, 'Смирнова О.И.', 'Сидорова К.К.', 1, 'Каре', 1200),
    (3, 'Иванов А.А.', 'Макаров Е.П.', 2, 'Цезарь', 700),
    (4, 'Кузнецов С.П.', 'Павлова М.А.', 1, 'Каскад', 1500)
]

with sq.connect('barbershop.db') as con:
    cur = con.cursor() 

    cur.execute("DROP TABLE IF EXISTS services")

    cur.execute("""CREATE TABLE IF NOT EXISTS services (
        service_id INTEGER PRIMARY KEY AUTOINCREMENT,
        master_name TEXT NOT NULL,
        client_name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        haircut_name TEXT,
        price INTEGER
    )""") 

    cur.executemany("INSERT INTO services VALUES (?, ?, ?, ?, ?, ?)", info_services)

    print("--- Выборка услуг (price > 600) с сортировкой по убыванию стоимости ---")
    cur.execute("SELECT * FROM services WHERE price > 600 ORDER BY price DESC")
    
    for result in cur:
        print(result)


    cur.execute("UPDATE services SET price = 600 WHERE haircut_name LIKE 'Полубокс'")

    cur.execute("DELETE FROM services WHERE service_id = 4")

    print("\n--- Итоговое состояние таблицы после UPDATE и DELETE ---")
    cur.execute("SELECT * FROM services")
    final_result = cur.fetchall() 
    for row in final_result:
        print(row)
