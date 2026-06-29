#Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для инкремента и декремента значения.
#Создайте класс "Животное", который содержит информацию о виде и возрасте животного. 
#Создайте классы "Собака" и "Кошка", которые наследуются от класса "Животное" и содержат информацию о породе.

class Counter:
    """Класс 'Счетчик' с методами инкремента и декремента."""
    
    def __init__(self, start_value=0):
        self.value = start_value
        
    def increment(self):
        """Метод для инкремента (увеличения) значения."""
        self.value += 1
        
    def decrement(self):
        """Метод для декремента (уменьшения) значения."""
        self.value -= 1

my_counter = Counter(10)

my_counter.increment()
print("Значение после инкремента:", my_counter.value)

my_counter.decrement()
my_counter.decrement()
print("Значение после двух декрементов:", my_counter.value)

=================================================

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

print(f"Объект 1: Вид - {dog_instance.animal_type}, Возраст - {dog_instance.age}, Порода - {dog_instance.breed}")
print(f"Объект 2: Вид - {cat_instance.animal_type}, Возраст - {cat_instance.age}, Порода - {cat_instance.breed}")
