#Сгенерировать словарь вида {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216}, удалить из
#него первый и последний элементы. Отобразить исходный и получившийся словарь.
#Использовать for, range.

original_dict = {}
for i in range(7):
    original_dict[i] = i ** 3

print("Исходный словарь:", original_dict)
del original_dict[0]
del original_dict[6]

print("Словарь после удаления первого и последнего элементов:", original_dict)
