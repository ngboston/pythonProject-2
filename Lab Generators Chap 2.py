#  Завдання 1.1
#  Створіть функцію, яка повертає всі непарні числа в діапазоні. Функція приймає початок і кінець діапазону
# як параметри. Використовуйте механізм генераторів усередині функції.

print("\n Task 1.1")

def findN(a,b):
    l = list(filter(lambda x: x%2==0, range(a,b)))
    return l
a=1
b=20
print(f"a={a}, b={b}: {findN(a,b)}")

#   Завдання 2.1
#  Створіть функцію, яка повертає всі значення зі списку, що не перебувають у діапазоні, зазначеному користувачем.
# Функція приймає список, початок і кінець діапазону як параметри. Використовуйте механізм генераторів усередині
# функції.

print("\n Task 2.1")

def findN(l,a,b):
    l0 = list(filter(lambda x: (x<=b and x>=a),l))
    return l0
l=[i for i in range(1,20)]
a=2
b=8
print(a,b,findN(l,a,b))

#   Завдання 3.1
# Для виконання цього завдання обов'язково використовуйте механізм функцій вищого порядку (higher order functions).
# Створіть функцію, що відображає лінію (горизонтальну або вертикальну) з використанням символу, зазначеного
# користувачем. Користувач визначає символ і яку лінію відображати.
# Сигнатура функції:
# def show_line(symbol, function_to_call)
# symbol — символ для відображення.
# function_to_call — функція для відтворення лінії(вертикальна лінія або горизонтальна лінія, на один тип лінії —
# одна функція).

print("\n Task 3.1")

def function_to_call(l,a):
    if a==True:
        return f"pair is{l%2 == 0}"
    else:
        return f" not pair is {l % 2 == 1}"
def check_value(v,f):
    a=int(input("Pair ? 1 or 0: "))
    return f(v,a)
v = 6
print(f"number: {v} {check_value(v,function_to_call)}")

#   Завдання 1.2
#  Створіть функцію, яка повертає всі прості числа в діапазоні. Функція приймає початок і кінець діапазону як
# параметри. Використовуйте механізм генераторів усередині функції.

print("\n Task 1.2")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def get_primes(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            yield num
if __name__ == "__main__":
    start = int(input("Введіть початок діапазону: "))
    end = int(input("Введіть кінець діапазону: "))
    primes = list(get_primes(start, end))
    print(f"Прості числа в діапазоні від {start} до {end}: {primes}")

#    Завдання 2.2
#  Створіть функцію, яка повертає всі числа Армстронга в діапазоні. Функція приймає початок і кінець діапазону
# як параметри. Використовуйте механізм генераторів усередині функції.
# Числа Армстронга (або самозакохані числа) — це натуральні числа, які дорівнюють сумі своїх цифр, піднесених
# до степеня, що дорівнює кількості цифр числа. Наприклад, число 153 є числом Армстронга, тому що
# 1^3 + 5^3 + 3^3 = 153.
# Ще приклад: число 370 — це число Армстронга, оскільки сума кубів його цифр дорівнює самому числу:
# 3^3 + 7^3 + 0^3 = 27 + 343 + 0 = 370

print("\n Task 2.2")

def is_armstrong(num):
    num_str = str(num)
    n = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit) ** n
        return sum == num

def armstrong_numbers_in_range(start, end):
    return (num for num in range(start, end+1) if is_armstrong(num))

start = 100
end = 1000
armstrong_nums = armstrong_numbers_in_range(start, end)

for num in armstrong_nums:
    print(num)


# Завдання 3.2
# Для виконання цього завдання обов'язково використовуйте механізм функцій вищого порядку (higher order functions).
# Створіть функцію, яка знаходить мінімум або максимум у списку. Користувач визначає на що перевіряти (мінімум або
# максимум).
# Сигнатура функції:
# def find_min_or_max(list_to_check, function_to_call)
# list_to_check — список для перевірки.
# function_to_call — функція перевірки (функція для перевірки на мінімум або функція для перевірки на максимум).

print("\n Task 3.2")

def find_min_or_max(list_to_check, function_to_call):
    return function_to_call(list_to_check)

def find_minimum(list):
    return min(list)

def find_maximum(list):
    return max(list)

my_list = [3, 5, 1, 8, 2, 9]
print(find_min_or_max(my_list, find_minimum))
print(find_min_or_max(my_list, find_maximum))