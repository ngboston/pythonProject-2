#   Завдання 1
#  Напишіть програму, яка запитує у користувача ім'я та вік. Після отримання даних програма повинна виводити
# привітання у форматі: "Привіт, {ім'я}! Твій вік — {вік}". Обробіть виняток, що виникає при введенні некоректного
# віку (вік < 0 або вік > 130), і виведіть повідомлення про помилку.

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    if age < 0 or age > 130:
        raise ValueError("Incorrect age")
    print(f"Hello, {name}! Your age — {age}")
except ValueError as e:
    print(f"Error: {e}")

# Завдання 2
# Реалізуйте перше завдання через функцію. Функція повинна приймати ім'я і вік як параметри і повертати
# відформатований рядок. Перевірка коректності отриманих даних повинна бути всередині функції. Створіть дві версії
# реалізації функції:
# Перша версія не обробляє виняток всередині функції. Уся обробка знаходиться зовні;
# Друга версія обробляє виняток усередині функції.

print("\n Task 2.1")

def greet(name, age):
    if age < 0 or age > 130:
        raise ValueError("Incorrect age")
    return f"Hello, {name}! Your age — {age}"

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    greeting = greet(name, age)
    print(greeting)
except ValueError as e:
    print(f"Error: {e}")

print("\n Task 2.1")

def greet(name, age):
    try:
        if age < 0 or age > 130:
            raise ValueError("Incorrect age")
        return f"Hello, {name}!Your age — {age}"
    except ValueError as e:
        return f"Error: {e}"

name = input("Enter your name: ")
age = int(input("Enter your age: "))
greeting = greet(name, age)
print(greeting)


# Завдання 3
# Напишіть програму, яка дозволяє користувачеві ввести з клавіатури набір додатних (число більше нуля) чисел.
# Числа необхідно накопичувати у списку. Після отримання всіх значень програма повинна проаналізувати дані. У разі
# виявлення від'ємного значення програма має згенерувати виняток. Якщо всі значення у списку позитивні, програма має
# повернути на екран суму всіх чисел списку.
# Згенерований виняток має бути оброблений кодом програми.

print("\n Task 3")

def get_positive_numbers():
    numbers = []
    while True:
        try:
            num = float(input("Enter a positive number (or 'q' to quit): "))
            if num <= 0:
                raise ValueError("Negative number detected!")
            numbers.append(num)
        except ValueError as e:
            print(e)
            break
    return numbers

try:
    numbers = get_positive_numbers()
    print(f"The sum of the numbers is: {sum(numbers)}")
except ValueError as e:
    print(e)

# Завдання 4
# Реалізуйте третє завдання через функцію. Функція повинна приймати список як аргумент і повертати суму елементів
# списку. Перевірка коректності отриманих даних повинна бути всередині функції. Створіть дві версії реалізації функції:
# Перша версія не обробляє виняток всередині функції. Уся обробка знаходиться зовні;
# Друга версія обробкабробляє виняток усередині функції.

print("\n Task 4.1")

def get_sum_of_numbers(numbers):
    for num in numbers:
        if num <= 0:
            raise ValueError("Negative number detected!")
    return sum(numbers)

try:
    numbers = [1, 2, 3, 4, 5]
    result = get_sum_of_numbers(numbers)
    print(f"The sum of the numbers is: {result}")

    numbers = [1, 2, 3, 4, -5]
    result = get_sum_of_numbers(numbers)
    print(f"The sum of the numbers is: {result}")
except ValueError as e:
    print(e)

print("\n Task 4.2")

def get_sum_of_numbers(numbers):
    try:
        for num in numbers:
            if num <= 0:
                raise ValueError("Negative number detected!")
        return sum(numbers)
    except ValueError as e:
        raise e

try:
    numbers = [1, 2, 3, 4, 5]
    result = get_sum_of_numbers(numbers)
    print(f"The sum of the numbers is: {result}")

    numbers = [1, 2, 3, 4, -5]
    result = get_sum_of_numbers(numbers)
    print(f"The sum of the numbers is: {result}")
except ValueError as e:
    print(e)