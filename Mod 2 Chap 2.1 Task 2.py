# Завдання 2
# Користувач вводить з клавіатури довжину лінії та символ
# для заповнення лінії. Виведіть на екран вертикальну лінію із
# введеним символом зазначеної довжини.
# Наприклад, якщо було введено 5 та символ %, тоді виведення на екран буде таким:

#   %
#   %
#   %
#   %
#   %

line=int(input('Enter the line length: '))
symbol=str(input('Enter the character: '))
for i in range(line):
    print(symbol)