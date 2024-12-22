#   Завдання 4
#  Користувач вводить з клавіатури числа. Програма має підраховувати суму введених чисел: максимум та мінімум. Коли
# користувач вводить число 7, програма припиняє свою роботу
# та виводить на екран напис «Good bye!».

min_value = None
max_value = None
Sum_value = 0
while True:
    value = int(input('Enter the number: '))
    if value == 7 :
        break
    Sum_value += value
    if min_value  is None  or value < min_value :
        min_value = value
    if max_value is None or value > max_value :
        max_value = value
print(' Good bye! ')
print('Amount : ' , Sum_value)
print(' Minimum value : ' , min_value)
print(' Maximum value : ' , max_value)





