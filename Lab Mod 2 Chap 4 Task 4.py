#  Завдання 4
#  Користувач вводить з клавіатури довжину та ширину
# прямокутника. Виведіть на екран незаповнений прямо
# кутник (відобразяться лише межі прямокутника). Розмір
# довжини та ширини дорівнює введеним даним

height = int(input('Enter the height of the rectangle: '))
width = int(input('Enter the width of the rectangle: '))
for i in range(1, height + 1):
    if i == 1 or i == height:
        print('*' * width)
    else:
        print('*' + ' ' * (width - 2) + '*')