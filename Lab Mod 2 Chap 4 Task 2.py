# Завдання 2
# Користувач вводить з клавіатури ширину та висоту
#прямокутника. Виведіть на екран заповнений прямо
# кутник із зазначеною висотою та шириною. Наприклад,
# якщо користувач ввів висоту 3, а ширину 5, на екран буде
# виведено:
#  *****
#  *****
#  *****

height = int(input('Enter the height of the rectangle: '))
width = int(input('Enter the width of the rectangle: '))
for i in range(width):
     print('*' * height)