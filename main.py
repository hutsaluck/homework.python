# #ДЗ core1
#
# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

st = 'as 23 fdfdg544'
digits = [char for char in st if char.isnumeric()]
print(', '.join(digits))

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

st = 'as 23 fdfdg544 34'
numbers = [''.join(char if char.isnumeric() else ' ' for char in st).split()]
print(', '.join(numbers[0]))

# #################################################################################
#
# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

greeting = 'Hello, world'
result = list(map(lambda char: char.upper(), greeting))
print(result)

# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

print([num**2 for num in range(1, 50, 2)])


# function
#
# - створити функцію яка виводить ліст
def display_items(items):
    for item in items:
        print(item)

display_items((1,2,3,4,5,6,7,8,9,10))

# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def find_maximum(num1, num2, num3):
    maximum = max(num1, num2, num3)
    print(maximum)
    return maximum

find_maximum(1, 2, 3)

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def find_max_and_min(*args):
    print(max(args))
    return min(args)

min_value = find_max_and_min(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(min_value)

# - створити функцію яка повертає найбільше число з ліста
def find_max_in_list(list):
    return max(list)

list_max = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
max_in_list = find_max_in_list(list_max)
print(max_in_list)

# - створити функцію яка повертає найменьше число з ліста
def find_min_in_list(list):
    return min(list)

list_min = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
min_in_list = find_min_in_list(list_min)
print(min_in_list)

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def sum_in_list(list):
    return sum(list)

list_sum = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sum_list = sum_in_list(list_sum)
print(sum_list)

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
def avg_in_list(list):
    return sum(list) / len(list)

list_avg = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
avg_list = avg_in_list(list_avg)
print(avg_list)

#
#
#
#
# ################################################################################################
# 1)Дан list:
list_num = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
print(min(list_num))

#   - видалити усі дублікати
def remove_duplicate_list():
    list_unique = list_num.copy()
    print(list(set(list_unique)))

remove_duplicate_list()

#   - замінити кожне 4-те значення на 'X'
def change_four_value_to_x():
    list_unique = list_num.copy()
    print(['X' if not (index + 1) % 4 else num for index, num in enumerate(list_unique)])
change_four_value_to_x()

# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як аргумент функції
def create_square(side):
    for i in range(side):
        if i == 0 or i == side - 1:
            print('*' * side)
        else:
            print('*' + ' ' * (side - 2) + '*')

create_square(8)

# 3) вывести табличку множення за допомогою цикла while
def show_multiplication_table():
    size = 9
    j = 1

    while j <= size:
        i = 1
        while i <= size:
            print(f'{i} x {j} = {(i * j):2}', end='   ')
            i += 1
        print()
        j += 1

show_multiplication_table()

# 4) переробити це завдання під меню

while True:
    print('1) знайти мінімальне число')
    print('2) видалити усі дублікати')
    print('3) замінити кожне 4-те значення на \'X\'')
    print('4) вивести на екран пустий квадрат з "*" сторона якого вказана як аргумент функції')
    print('5) вивести табличку множення за допомогою цикла while')
    print('6) Вихід')

    choice = input('Зробіть свій вибір: ')
    if choice == '1':
        print(find_min_in_list(list_num))
    elif choice == '2':
        remove_duplicate_list()
    elif choice == '3':
        change_four_value_to_x()
    elif choice == '4':
        create_square(6)
    elif choice == '5':
        show_multiplication_table()
    elif choice == '6':
        break

