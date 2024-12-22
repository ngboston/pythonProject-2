# Завдання 3
# Користувач вводить з клавіатури розмір сторони
# квадрата. Виведіть на екран незаповнений квадрат (відо
# бразяться лише межі квадрата). Розмір сторони дорівнює
# введеному розміру

side=int(input('Enter the size of the side of the square: '))
for i in range(side):
    if i == 0 or i == side - 1:
       print("*" * side)
    else:
       print("*" + " " * (side - 2) + "*")