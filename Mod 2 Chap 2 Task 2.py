# Завдання 2
# Користувач вводить з клавіатури номер місяця (1-12).
# Виведіть на екран назву місяця. Наприклад, якщо введено 1,
# то на екрані з’явиться напис «Січень», 2 — «Лютий» і т. д.

mounth = int(input('Введіть номер місяця від 1 до 12: '))
if mounth == 1:
    print('Січень')
elif mounth == 2:
    print('Лютий')
elif mounth == 3:
    print('Березень')
elif mounth == 4:
    print('Квітень')
elif mounth == 5:
    print('Травень')
elif mounth == 6:
    print('Червень')
elif mounth == 7:
    print('Липень')
elif mounth == 8:
    print('Серпень')
elif mounth == 9:
    print('Вересень')
elif mounth == 10:
    print('Жовтень')
elif mounth == 11:
    print('Листопад')
elif mounth == 12:
    print('Грудень')
else:
    print('В році тільки 12 місяців. Введить від 1 до 12.')


