# Завдання 1
# Користувач вводить з клавіатури ціле шестизначне
# число. Напишіть програму, яка визначає, чи є введене
# число — щасливим (щасливим вважається шестизначне
# число, в якому сума перших трьох цифр дорівнює сумі
# других трьох цифр).
# Наприклад, 123321 — щасливе число, оскільки 1+2+3 =
# 3+2+1.
# З іншого боку, 378423 нещасливе число, оскільки
# 3+7+8 != 4+2+3.
#  Якщо користувач ввів не шестизначне число, виведіть
# повідомлення про помилку

num = int(input('Enter a six digit number: '))
part_1 = num//1000
a=part_1//100
b=(part_1//10)%10
c=part_1%10
part_2 = num%1000
d=part_2//100
e=(part_2//10)%10
f=part_2%10
if (a+b+c)==(d+e+f):
    print('Lucky number')
elif num<10000:
    print('The number you entered is not a six-digit number. Please try again.')
elif num>999999:
    print('The number you entered is not a six-digit number. Please try again.')
else:
    print('Unlucky number')