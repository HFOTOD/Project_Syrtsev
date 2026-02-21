sample = {'a': 100, 'b':200, 'c':300}
for i, key in sample.items():
    if key == 200:
        print('norm')

original_dict = {}
for i in range(7):
    original_dict[i] = i ** 3

print("Исходный словарь:", original_dict)
del original_dict[0]
del original_dict[6]

print("Словарь после удаления первого и последнего элементов:", original_dict)
