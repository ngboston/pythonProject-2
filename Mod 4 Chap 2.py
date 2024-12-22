#   Завдання 1
#  Напишіть функцію для підрахунку добутку елементів
# списку цілих. Список передається як параметр. Отриманий
# результат повертається із функції.

print("\n Task 1")

def multiplication_elements(list_of_integers):
    m = 1
    for element in list_of_integers:
        m = m * element
    return m


a = multiplication_elements([1, 2, 3, 4])
print(a)

#   Завдання 2
#  Напишіть функцію для знаходження мінімуму в списку
# цілих. Список передається як параметр. Отриманий результат
# повертається із функції.

print("\n Task 2")

def smallest_element(list_of_integers):
    s = list_of_integers[0]
    for element in list_of_integers:
        if s > element:
            s = element
    return s

a = smallest_element([-6, 5, 4, 3, -2, 1, 0, 2])
print(a)

#   Завдання 3
# Напишіть функцію, яка визначає кількість простих чисел
# у списку цілих. Список передається як параметр. Отриманий
# результат повертається із функції.

print("\n Task 3")

def is_prime(integer):
    if 1 < integer:
        for i in range(2, integer):
            if integer % i == 0:
                return False
        return True


def number_of_primes(list_of_integers):
    number_of_prim = 0
    for element in list_of_integers:
        if is_prime(element) == True:
            number_of_prim = number_of_prim + 1
    return number_of_prim


a = number_of_primes([-6, 5, 4, 3, -2, 1, 0, 2])
print(a)

#   Завдання 4
#  Напишіть функцію, яка видаляє зі списку цілих певне
# задане число. З функції потрібно повернути кількість віддалених елементів.

print("\n Task 4")

def remove_integer_from_list(integer, list):
    c = list.count(integer)
    for i in range(c):
        list.remove(integer)
    return c


a_list = [-6, 5, 4, 3, -2, 1, 0, 2]
a_integer = 2
c = remove_integer_from_list(a_integer, a_list)

print(c)
print(a_list)


#   Завдання 5
#  Напишіть функцію, яка отримує два списки як параметр
# і повертає список з елементами обох списків.

print("\n Task 5")

def concatenate_two_lists(list1, list2):
    return list1 + list2

a_list = [2, 3, 4, 5]
b_list = [12, 13, 14, 15]
c = concatenate_two_lists(a_list, b_list)
print(c)

#   Завдання 6
#  Напишіть функцію, яка підраховує степінь кожного елемента
# списку цілих. Значення для степеня, як і список, передається
# як параметр. Функція повертає новий список з отриманими
# результатами.повертає список з елементами обох списків.

print("\n Task 6")

def power_of_elements_list(power, list_of_integers):
    for i in range(len(list_of_integers)):
        list_of_integers[i] = list_of_integers[i]**power
    return list_of_integers


a_power = 4
a_list = [-6, 5, 4, 3, -2, 1, 0, 2]
p = power_of_elements_list(a_power, a_list)

print(p)
