#   Завдання 2
#  Користувач вводить з клавіатури два числа (початок та
# кінець діапазону). Проаналізуйте усі числа у цьому діапазоні.
# Виведіть на екран:
#   1. Усі числа діапазону.
#   2. Усі числа діапазону за спаданням.
#   3. Усі числа, кратні 7.
#   4. Кількість чисел, кратних 5.

x = int(input('Enter the start of the range : '))
y  = int(input('Enter the end of the range : '))
for i in range(x, y+1):
    print(i, end=' ')
print()
for i in range(y-1, x-1, -1):
    print(i, end=' ')
print()
for i in range(x, y):
    if i % 7 == 0:
        print(i, end=' ')
print()
for i in range(x, y):
     if i % 5 == 0:
        print(i, end=' ')
