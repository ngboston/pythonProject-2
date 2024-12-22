# Завдання 4
# Користувач вводить два числа. Визначте, чи рівні ці числа,
# якщо ні, виведіть іх на екран у порядку зростання.

number1 = int(input('Введить перше число: '))
number2 = int(input('Введить друге число: '))
if number1 < number2:
    print('Числа не рівні: ', number1, number2)
elif number1 > number2:
    print('Числа не рівні: ', number2, number1)
else:
    print('Числа рівні')

