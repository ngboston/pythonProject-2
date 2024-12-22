#   Завдання 1
# Напишіть функцію, яка виводить на екран форматований
# текст, наведений нижче:
# “Don’t compare yourself with anyone in this world…
#  if you do so, you are insulting yourself.”
#                                         Bill Gates
print("\nTask 1")

def show_text():
    print(" Don’t compare yourself with anyone in this world…")
    print("if you do so, you are insulting yourself.")
    print(" "*39,"Bill Gates")
show_text()
#   Завдання 2
#  Напишіть функцію, яка приймає два числа як параметр
# і відображає усі парні числа між ними

def display_odd(number1, number2):

 start = min(number1, number2)
 finish = max(number1, number2)

 for number in range(start + 1, finish):
    if number % 2 == 0:
        print(number)
number1 = 5
number2 = 15
display_odd(number1, number2)

#   Завдання 3
#  Напишіть функцію, яка відображає порожній або заповнений квадрат із певним символом. Функція приймає в якості параметрів довжину сторони квадрата, символ та змінну
# логічного типу:
#   ■ якщо вона дорівнює True, квадрат заповнений;
#   ■ якщо False, квадрат порожній.

def square(sym, n, fill=True):
    line = n * sym
    if fill:
        for _ in range(n):
            print(line)
    else:
        print(line)
        for _ in range(n - 2):
            print(sym + " " * (n - 2) + sym)
        print(line)


square("*", 5, False)

#   Завдання 4
#  Напишіть функцію, яка повертає мінімальне з п’яти чисел.
# Числа передаються як параметри.

def min_mum(a,b,c,d,e):
    q=min(a,b,c,d,e)
    return q
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=int(input("d="))
e=int(input("e="))
print(min_mum(a,b,c,d,e))


#   Завдання 5
#  Напишіть функцію, яка повертає добуток чисел у зазначеному діапазоні. Межі діапазону передаються як параметри.
# Якщо межі діапазону переплутані (наприклад, 5 — верхня
# межа, 25 — нижня межа), їх треба поміняти місцями.

def multiplication(A, B):
    if A == B:
        return "Діапазон введено не вірно."
    if A > B:
        A, B = B, A
    res = 1
    for i in range(A, B + 1):
        res *= i
    return res
print(multiplication(int(input("Введіть A: ")), int(input(" Введіть B: "))))

#   Завдання 6
#  Напишіть функцію, яка підраховує кількість цифр у числі.
# Число передається як параметр. Поверніть з функції отриману
# кількість цифр. Наприклад, якщо передали 3456, кількість
# цифр буде 4

def digit_number(x):
    res = 0
    for i in range(len(str(x))):
        res += 1
    return res


print('кількисть цифр в числі 123456 = ', digit_number(123456))

#   Завдання 7
#  Напишіть функцію, яка перевіряє число на паліндром.
# Число передається як параметр. Якщо число є паліндромом,
# поверніть з функції true, якщо ні — false.
# «Паліндром» — це число, в якому перша частина цифр
# дорівнює другій перевернутій частини цифр. Наприклад,
# 123321 — паліндром (перша частина 123, друга 321, яка після
# перевороту стає 123), 546645 — паліндром, а 421987 — не
# паліндром.

def polindrom(x):
    comp = ''.join(reversed(str(x)))
    return str(x) == str(comp)


num = 1221
if polindrom(num):
    print('Число ', num, '- паліндром.')
else:
    print('Число ', num, '- не паліндром .')