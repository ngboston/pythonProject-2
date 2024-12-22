# Завдання 3
# Користувач вводить з клавіатури числа. Якщо число більше
# 0, виведіть напис «Number is positive», якщо менше 0 — «Number
# is negative», якщо дорівнює 0 — «Number is equal to zero». Коли
# користувач вводить число 7, програма припиняє свою роботу
# та виводить на екран напис «Good bye!».

while True:
     number = int(input('Enter the number: '))
     if number>0:
        print('«Numberis positive»')
     elif number<0:
        print('«Numberis negative»')
     elif number==0:
         print('«Number is equal to zero»')
     if number==7:
         break
