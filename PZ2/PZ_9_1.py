#Книжные магазины предлагают следующие коллекции книг.
#Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
#ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
#БукМаркет – Пушкин, Достоевский, Маяковский.
#Галерея – Чехов, Тютчев, Пушкин.
#Определить в каких магазинах
#можно приобрести книги Пушкина и Тютчева

magistr = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
dom_knigi = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
bukmarket = {'Пушкин', 'Достоевский', 'Маяковский'}
galereya = {'Чехов', 'Тютчев', 'Пушкин'}

all_stores = {
    'магистр': magistr,
    'домкниги': dom_knigi,
    'букмаркет': bukmarket,
    'галерея': galereya
}

def find_stores_with_books(all_stores, books):
    available_stores = []
    for store, collection in all_stores.items():
        if books.issubset(collection):
            available_stores.append(store)
    return available_stores

books_to_find = {'Пушкин', 'Тютчев'}
stores_with_books = find_stores_with_books(all_stores, books_to_find)

print('Магазины в которых модно купить Пушкина и Тютчева:', stores_with_books)
