#Определить в каких магазинах
#можно приобрести книги Пушкина и Тютчева

magistr = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
dom_knigi = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
bukmarket = {'Пушкин', 'Достоевский', 'Маяковский'}
galereya = {'Чехов', 'Тютчев', 'Пушкин'}

required = {'Пушкин', 'Тютчев'}
result = set()

if required & magistr == required:
    result.add('Магистр')

if required & dom_knigi == required:
    result.add('ДомКниги')

if required & bukmarket == required:
    result.add('БукМаркет')

if required & galereya == required:
    result.add('Галерея')

print('Магазины, в которых можно приобрести книги Пушкина и Тютчева:', result)



bookstores = {
    "Магистр": {"Лермонтов", "Достоевский", "Пушкин", "Тютчев"},
    "ДомКниги": {"Толстой", "Грибоедов", "Чехов", "Пушкин"},
    "БукМаркет": {"Пушкин", "Достоевский", "Маяковский"},
    "Галерея": {"Чехов", "Тютчев", "Пушкин"}
}

result = []
for store, authors in bookstores.items():
    if "Пушкин" in authors and "Тютчев" in authors:
        result.append(store)
        
        print("Магазины в которых можно приобрести книги Пушкина и Тютчев:", result)

