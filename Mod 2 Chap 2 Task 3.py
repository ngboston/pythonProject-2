# Завдання 3
# Користувач вводить з клавіатури число. Якщо число більше
# 0, виведіть напис «Number is positive», якщо менше 0 — «Number
# is negative», якщо дорівнює 0 — «Number is equal to zero».

number = int(input('ВВедіть число: '))
if number > 0:
    print('«Numberis positive»')
elif number < 0:
    print('«Number is negative»')
else:
    print('«Number is equal to zero»')

