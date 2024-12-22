#    Завдання 2
#  Маємо список цілих, заповнений випадковими чис
# лами. Використовуючи дані цього масиву створіть список
# цілих, що містить лише:
#  ■ парні числа з першого списку;
#  ■ непарні числа з першого списку;
#  ■ від’ємні числа з першого списку;
#  ■ додатні числа з першого списку.

numbers = [-12, 55, -32, 10, -47, 93, -1, 60, -1, 33]
odd_list = [i for i in numbers if i%2]
even_list = [i for i in numbers if not i%2]
negative_list = [i for i in numbers if i < 0]
positive_list = [i for i in numbers if i >= 0]
print("Odd numbers:", odd_list)
print("Even numbers:",even_list)
print("Negative numbers:",negative_list)
print("Positive numbers:", positive_list)