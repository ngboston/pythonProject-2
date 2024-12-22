 #   Завдання 1
#  У списку цілих, заповненому випадковими числами,
# розрахуйте:

#  ■ Суму від’ємних чисел.
#  ■ Суму парних чисел.
#  ■ Суму непарних чисел.
#  ■ Добуток елементів з індексами, кратними 3.
#  ■ Добуток елементів між мінімальним та максимальним
#  елементом.
#  ■ Суму елементів, що знаходяться між першим та ос
#  таннім додатним елементом


import random
numbers = [random.randint(-100, 100) for _ in range(25)]
print(numbers)
# Task 1
sum_neg = 0
for number in numbers:
    if number < 0:
        sum_neg += number
print('sum_neg =', sum_neg)
# Task 2
sum_even = 0
for num in numbers:
    if num % 2 == 0:
        sum_even += number
print('sum_even =', sum_even)
# Task 3
sum_odd = 0
for number in numbers:
    if number % 2 != 0:
        sum_odd += number
print('sum_odd =', sum_odd)
# Task 4
prod_3 = 1
for i, number in enumerate(numbers):
    if i % 3 == 0:
        prod_3 *= number
print('prod_3 =', prod_3)
# Task 5
prod_min_max = 1
min_number = min(numbers)
max_number = max(numbers)
for number in numbers:
    if number > min_number and number < max_number:
        prod_min_max *= number
print('prod_min_max =', prod_min_max)
# Task 6
sum_pos = 0
first_found = False
last_found = False
for number in numbers:
    if number > 0 and first_found == False:
        first_found = True
    elif first_found == True and number > 0:
        sum_pos += number
    elif first_found == True and number < 0:
        last_found = True
    if last_found == True and number > 0:
        break
print('sum_pos =', sum_pos)

