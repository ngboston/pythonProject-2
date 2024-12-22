#    Завдання 1
#  Напишіть функцію, яка виводить на екран формато
# ваний текст, наведений нижче:
# “Don’t let the noise of others’ opinions
# drown out your own inner voice.”
#  Steve Jobs


print("\nTask 1")

def show_text():
    print(" Don’t let the noise of others’ opinions")
    print("drown out your own inner voice.")
    print(" "*29,"Steve Jobs")
show_text()

#   Завдання 2
#  Напишіть функцію, яка приймає два числа як пара
# метр і відображає усі непарні числа між ними

print("\nTask 2")

def display_odd(number1, number2):

 start = min(number1, number2)
 finish = max(number1, number2)

 for number in range(start + 1, finish):
    if number % 2 == 0:
        print(number)
number1 = 5
number2 = 15
display_odd(number1, number2)

#  Завдання 3
#  Напишіть функцію, яка відображає горизонтальну або
# вертикальну лінію з певного символу. Функція приймає
# як параметр: довжину лінії, напрям та символ.

print("\nTask 3")

def printLine(l=12,n=True,s="$"):
    if n:
        print(s*l)
    else:
        print(F"{s}\n"*l)
printLine(12, False,"$")

#   Завдання 4
#  Напишіть функцію, яка повертає максимальне число
# із чотирьох. Числа передаються як параметри.

print("\nTask 4")

def max_of_four(a, b, c, d):
    return max(a, b, c, d)
print(max_of_four(1, 2, 3, 4))
print(max_of_four(-5, -4, -3, -2))

#   Завдання 5
#  Напишіть функцію, яка повертає суму чисел у вказаному діапазоні. Межі діапазону передаються як параметри.

print("\nTask 5")

def sum_numbers_from_range(start, finish):
    i = start
    sum = 0
    while i <= finish:
        sum = sum + i
        i = i + 1
    return sum
print(sum_numbers_from_range(10, 20))

#   Завдання 6
#  Напишіть функцію, яка перевіряє чи є число простим.
#  Число передається як параметр. Якщо число просте, поверніть з методу true, якщо ні — false.

print("\nTask 6")

def check_num(n):
    for i in range(2, n//2):
        if n%i==0:
            print(f"Number{n}/{i}")
            return False
    print(f"{n} is prime number")
    return True
n=34
print(check_num(n))

#   Завдання 7
#  Напишіть функцію, яка перевіряє чи є шестизначне
# число «щасливим». Число передається як параметр. Якщо
# число щасливе, поверніть з функції true, якщо ні — false.
#  «Щасливе шестизначне число» — це число, в якому
# сума перших трьох цифр дорівнює сумі других трьох
# цифр. Наприклад, 123420 — щасливе 1+2+3 = 4+2+0, а
# 723422 — нещасливе 7+2+3 != 4+2+2.

print("\nTask 7")


def lucky_num(number):
    if len(str(number)) != 6:
        print(f" Number does not have 6 digits")
        return False
        digits = [int(digit) for digit in str(number)]
        sum1 = digits[0] + digits[1] + digits[2]
        sum2 = digits[4] + digits[5] + digits[6]
        if sum1 == sum2:
            print(f"Number{number}is lucky")
            return True
    else:
        print(f"Number{number} is unlucky")
        return False
number=111112

print(lucky_num(number))






