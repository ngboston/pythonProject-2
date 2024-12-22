#   Завдання 1
#  Напишіть програму, яка запитує у користувача число і обчислює його факторіал. Обробіть виняток, що виникає при
# введенні від'ємного числа, і виведіть повідомлення про помилку.

print("\n Task 1")

def calculate_factorial():
    try:
        num = int(input("Введіть число: "))
        if num < 0:
            raise ValueError("Помилка: Число має бути відємним.")
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        print(f"Факторіал числа {num} дорівнює {factorial}")
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    calculate_factorial()

#     Завдання 2
#   Реалізуйте перше завдання через функцію. Функція повинна приймати число як параметр і повертати його факторіал.
# Перевірка коректності отриманих даних повинна бути всередині функції. Створіть дві версії реалізації функції:
#   Перша версія не обробляє виняток усередині функції. Уся обробка знаходиться зовні;
#   Друга версія обробляє виняток усередині функції.

print("\n Task 2.1")

def factorial(n):
    if n < 0:
        raise ValueError("Помилка: Число має бути відємним.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
if __name__ == "__main__":
    try:
        num = int(input("Введіть число: "))
        result = factorial(num)
        print(f" Факторіал числа {num} дорівнює {result}")
    except ValueError as e:
        print(e)

print("\n Task 2.3")

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Помилка: Число має бути не відємним цілим числом.")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
if __name__ == "__main__":
    try:
        num = int(input("Введіть число: "))
        result = factorial(num)
        print(f"Факторіал числа {num} дорівнює {result}")
    except ValueError as e:
        print(e)

# Завдання 3
# Напишіть програму, яка дає змогу користувачеві заповнити список із клавіатури числами. Після отримання даних
# відобразіть на екран меню, яке дозволяє виконати такі операції:
#
# Відображення списку;
# Отримання максимального значення у списку;
# Отримання мінімального значення у списку;
# Відображення значення елемента за індексом, введеним користувачем;
# Видалення елемента за індексом, введеним користувачем.
# Обробіть виняток, що виникає під час виходу за межі списку (користувач ввів неправильне значення для індексу елемента
# в списку), і виведіть повідомлення про помилку.

print("\n Task 3")

def fill_list():
    lst = []
    while True:
        try:
            num = int(input("Введіть число (або 'q' для завершення): "))
            if num == 'q':
                break
            lst.append(num)
        except ValueError:
            if num == 'q':
                break
            else:
                print("Помилка: не введено число.")
    return lst

def display_list(lst):
    print("Список чисел:", lst)

def get_max(lst):
    if not lst:
        print("Список поржній.")
    else:
        print("Максимальне значення:", max(lst))

def get_min(lst):
    if not lst:
        print("Список порожній.")
    else:
        print("Минимальне значення:", min(lst))

def get_element_by_index(lst):
    index = int(input("Введіть індекс елемента: "))
    try:
        print("Значення елемента:", lst[index])
    except IndexError:
        print("Помилка: індекс поза списком.")

def delete_element_by_index(lst):
    index = int(input("Введіть індекс елемента для видалення: "))
    try:
        del lst[index]
        print("Елемент видалено.")
    except IndexError:
        print("Помилка: індекс поза списком.")

def main():
    numbers_list = fill_list()
    while True:
        print("Меню:")
        print("1. Відобразити список")
        print("2. Отримати максимальне значення")
        print("3. Отримати мінімальне значення")
        print("4. Відобразити значення елемента за індексом")
        print("5. Видалити елемент за індексом")
        print("6. Вихід")

        choice = input("Виберіть дію (1-6): ")

        if choice == '1':
            display_list(numbers_list)
        elif choice == '2':
            get_max(numbers_list)
        elif choice == '3':
            get_min(numbers_list)
        elif choice == '4':
            get_element_by_index(numbers_list)
        elif choice == '5':
            delete_element_by_index(numbers_list)
        elif choice == '6':
            print("Вихід із програми.")
            break
        else:
            print("Помилка: неправильний вибір.")

if __name__ == "__main__":
    main()

# Завдання 4
# Реалізуйте третє завдання через функції. Створіть дві версії реалізації функцій:
#
# Перша версія не обробляє винятки всередині функцій. Уся обробка знаходиться зовні;
# Друга версія обробляє винятки всередині функцій.

print("\n Task 4.1")

def fill_list():
    lst = []
    while True:
        num = input("Введіть число (або 'q' для завершення): ")
        if num == 'q':
            break
        lst.append(int(num))
    return lst

def display_list(lst):
    print("Список чисел:", lst)

def get_max(lst):
    if not lst:
        print("Список порожній.")
    else:
        print("Максимальне значення:", max(lst))

def get_min(lst):
    if not lst:
        print("Список порожній.")
    else:
        print("Мінімальне значення:", min(lst))

def get_element_by_index(lst):
    index = int(input("Мінімальне значення: "))
    try:
        print("Значення елемента:", lst[index])
    except IndexError:
        print("Помилка: індекс поза списком.")

def delete_element_by_index(lst):
    index = int(input("Введіть індекс елемента для видалення: "))
    try:
        del lst[index]
        print("Елемент видалено.")
    except IndexError:
        print("Помилка: індекс поза списком.")

def main():
    numbers_list = fill_list()
    while True:
        print("Меню:")
        print("1. Відобразити список")
        print("2. Отримати максимальне значення")
        print("3. Отримати мінімальне значення")
        print("4. Відобразити значення елемента за індексом")
        print("5. Видалити елемент за індексом")
        print("6. Вихід")

        choice = input("Виберіть дію (1-6): ")

        if choice == '1':
            display_list(numbers_list)
        elif choice == '2':
            get_max(numbers_list)
        elif choice == '3':
            get_min(numbers_list)
        elif choice == '4':
            get_element_by_index(numbers_list)
        elif choice == '5':
            delete_element_by_index(numbers_list)
        elif choice == '6':
            print("Вихід із програми..")
            break
        else:
            print("Помилка: неправильний вибір.")

if __name__ == "__main__":
    main()

print("\n Task 4.2")

def fill_list():
    lst = []
    while True:
        try:
            num = input("Введіть число (або 'q' для завершення):  ")
            if num == 'q':
                break
            lst.append(int(num))
        except ValueError:
            print("Помилка: не введено число.")
    return lst

def display_list(lst):
    print("Список чисел:", lst)

def get_max(lst):
    if not lst:
        print("Список поржній.")
    else:
        print("Максимальне значення:", max(lst))

def get_min(lst):
    if not lst:
        print("Список порожній.")
    else:
        print("Мінімальне значення:", min(lst))

def get_element_by_index(lst):
    index = int(input("Введіть індекс елемента: "))
    try:
        print("Значення елемента:", lst[index])
    except IndexError:
        print("Помилка: індекс поза списком.")

def delete_element_by_index(lst):
    index = int(input("ведіть індекс елемента для видалення: "))
    try:
        del lst[index]
        print("Елемент видалено.")
    except IndexError:
        print("Помилка: індекс поза списком.")

def main():
    numbers_list = fill_list()
    while True:
        print("Меню:")
        print("1. Відобразити список")
        print("2. Отримати максимальне значення")
        print("3. Отримати мінімальне значення")
        print("4. Відобразити значення елемента за індексом")
        print("5. Видалити елемент за індексом")
        print("6. Вихід")

        choice = input("Виберіть дію (1-6): ")

        if choice == '1':
            display_list(numbers_list)
        elif choice == '2':
            get_max(numbers_list)
        elif choice == '3':
            get_min(numbers_list)
        elif choice == '4':
            get_element_by_index(numbers_list)
        elif choice == '5':
            delete_element_by_index(numbers_list)
        elif choice == '6':
            print("Вихід із програми.")
            break
        else:
            print("Помилка: неправильний вибір.")

if __name__ == "__main__":
    main()