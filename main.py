# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи

"""
def create_task_manager():
    task_list = []

    def add_task(task):
        task_list.append(task)

    def get_tasks():
        return task_list.copy()

    return add_task, get_tasks

personal_tasks = create_task_manager()
work_tasks = create_task_manager()

add_personal_task, get_personal_tasks = personal_tasks
add_work_task, get_work_tasks = work_tasks

add_personal_task("Купити продукти")
add_personal_task("Прочитати книгу")

add_work_task("Підготувати звіт")
add_work_task("Написати лист клієнту")

print("Особисті завдання:", get_personal_tasks())
print("Робочі завдання:", get_work_tasks())
"""

# 2) протипізувати перше завдання

from typing import Callable

def create_task_manager() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
    task_list: list[str] = []

    def add_task(task: str) -> None:
        nonlocal task_list
        task_list.append(task)

    def get_tasks() -> list[str]:
        return task_list.copy()

    return add_task, get_tasks

personal_tasks = create_task_manager()
work_tasks = create_task_manager()

add_personal_task, get_personal_tasks = personal_tasks
add_work_task, get_work_tasks = work_tasks

add_personal_task("Купити продукти")
add_personal_task("Прочитати книгу")

add_work_task("Підготувати звіт")
add_work_task("Написати лист клієнту")

print("Особисті завдання:", get_personal_tasks())
print("Робочі завдання:", get_work_tasks())




# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

def expanded_form(number):
    number_str = str(number)
    num_length = len(number_str) - 1
    parts = []

    for index, digit in enumerate(number_str):
        if digit != '0':
            parts.append(digit + '0' * (num_length - index))

    return ' + '.join(parts) + f' = {number_str}'

print(expanded_form(3810))

# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# та буде виводити це значення після виконання функцій

def call_counter(func):
    call_count = 0  # Лічильник викликів для конкретної функції

    def wrapper(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        func(*args, **kwargs)
        print(f'Виклики {func.__name__}: {call_count}')

    return wrapper

@call_counter
def function_one():
    print('Виконується function_one')

@call_counter
def function_two():
    print('Виконується function_two')

function_one()
function_two()
function_one()
function_one()
function_two()
function_two()
function_one()
function_two()
function_one()
