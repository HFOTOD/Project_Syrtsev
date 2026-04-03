def lower_generator(text):
    for char in text:
        yield char.lower()

s = "HeLLo WoRLD"
result = ''.join(lower_generator(s))

print("Исходная строка:", s)
print("После генератора:", result)