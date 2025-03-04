# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return self.area + other.area
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            return self.area - other.area
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area == other.area
        return NotImplemented

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area > other.area
        return NotImplemented

    def __len__(self):
        return self.perimeter

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"




# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cinderella(Human):
    __count = 0

    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cinderella.__count += 1

    @classmethod
    def get_count(cls):
        print(cls.__count)

    def __str__(self):
        return str(self.__dict__)

class Prince(Human):
    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size

    def find_cinderella(self, cinderella_list: list[Cinderella]):
        for cinderella in cinderella_list:
            if cinderella.foot_size == self.shoe_size:
                print(cinderella)
                return cinderella

cinderella_list:list[Cinderella] = [
    Cinderella('Olha', 25, 32),
    Cinderella('Kira', 18, 36),
    Cinderella('Albina', 30, 38),
    Cinderella('Maria', 25, 39),
]

prince = Prince('Max', 15, 36)

prince.find_cinderella(cinderella_list)

Cinderella.get_count()



# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f'This book is {self.name}')

class Magazine(Printable):
    def __init__(self, name):
        self.name = name
    def print(self):
        print(f'This magazine is {self.name}')

# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
#
# Приклад:
#
# Main.add(Magazine('Magazine1'))
#     Main.add(Book('Book1'))
#     Main.add(Magazine('Magazine3'))
#     Main.add(Magazine('Magazine2'))
#     Main.add(Book('Book2'))
#
#     Main.show_all_magazines()
#     print('-' * 40)
#     Main.show_all_books()
# для перевірки ксассів використовуємо метод isinstance, приклад:
#
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False


class Main:
    __printable_list:list[Printable] = []

    @classmethod
    def add(cls, item:Book|Magazine):
        if isinstance(item, (Book, Magazine)):
            cls.__printable_list.append(item)

    @classmethod
    def show_all_magazines(cls):
        for item in cls.__printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        for item in cls.__printable_list:
            if isinstance(item, Book):
                item.print()

Main.add(Magazine('Magazine1'))
Main.add(Magazine('Magazine2'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine4'))
Main.add(Book('Book1'))
Main.add(Book('Book2'))
Main.add(Book('Book3'))
Main.add(Book('Book4'))
Main.add('fasdfdsafs')

Main.show_all_magazines()
print('*******************************')
Main.show_all_books()





