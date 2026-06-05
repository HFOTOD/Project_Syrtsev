class Animal:
    """Класс Животное."""

    def __init__(self, species, age):
        self.species = species
        self.age = age

    def show_info(self):
        """Вывод информации о животном."""
        print(f"Вид: {self.species}")
        print(f"Возраст: {self.age}")


class Dog(Animal):
    """Класс Собака."""

    def __init__(self, species, age, breed):
        super().__init__(species, age)
        self.breed = breed

    def show_info(self):
        """Вывод информации о собаке."""
        super().show_info()
        print(f"Порода: {self.breed}")


class Cat(Animal):
    """Класс Кошка."""

    def __init__(self, species, age, breed):
        super().__init__(species, age)
        self.breed = breed

    def show_info(self):
        """Вывод информации о кошке."""
        super().show_info()
        print(f"Порода: {self.breed}")


animal = Animal("Животное", 3)
print("Информация о животном:")
animal.show_info()

print()

dog = Dog("Собака", 5, "Немецкая овчарка")
print("Информация о собаке:")
dog.show_info()

print()

cat = Cat("Кошка", 2, "Британская короткошерстная")
print("Информация о кошке:")
cat.show_info()
==================================

class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age


class Dog(Animal):
    def __init__(self, species, age, breed):
        self.species = species
        self.age = age
        self.breed = breed


class Cat(Animal):
    def __init__(self, species, age, breed):
        self.species = species
        self.age = age
        self.breed = breed


dog = Dog("Собака", 5, "Овчарка")
print("Вид:", dog.species)
print("Возраст:", dog.age)
print("Порода:", dog.breed)

print()

cat = Cat("Кошка", 2, "Британская")
print("Вид:", cat.species)
print("Возраст:", cat.age)
print("Порода:", cat.breed)
