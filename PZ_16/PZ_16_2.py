class Animal:
    """Базовый класс 'Животное'."""
    
    def __init__(self, animal_type, age):
        self.animal_type = animal_type
        self.age = age


class Dog(Animal):
    """Подкласс 'Собака', наследуемый от 'Животное'."""
    
    def __init__(self, animal_type, age, breed):
        super().__init__(animal_type, age)
        self.breed = breed


class Cat(Animal):
    """Подкласс 'Кошка', наследуемый от 'Животное'."""
    
    def __init__(self, animal_type, age, breed):
        super().__init__(animal_type, age)
        self.breed = breed

dog_instance = Dog("Собака", 3, "Лабрадор")
cat_instance = Cat("Кошка", 2, "Сиамская")

# Обращение к атрибутам базового класса и подклассов
print(f"Объект 1: Вид - {dog_instance.animal_type}, Возраст - {dog_instance.age}, Порода - {dog_instance.breed}")
print(f"Объект 2: Вид - {cat_instance.animal_type}, Возраст - {cat_instance.age}, Порода - {cat_instance.breed}")
