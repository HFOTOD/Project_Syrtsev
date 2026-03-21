import random

numbers = [random.randint(0, 10) for _ in range(20)]
print("Исходная последовательность:", numbers)

unique_numbers = list(set(numbers))
print("Неповторяющиеся элементы:", unique_numbers)

print("Количество уникальных элементов:", len(unique_numbers))

modified_numbers = [x * 2 if x > 5 else x for x in numbers]
print("Изменённая последовательность:", modified_numbers)


def lower_generator(text):
    for char in text:
        yield char.lower()

s = "HeLLo WoRLD"
result = ''.join(lower_generator(s))

print("Исходная строка:", s)
print("После генератора:", result)
