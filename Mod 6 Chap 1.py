#   Завдання 1
#  Маємо три кортежі цілих чисел. Знайдіть елементи, які
# є у всіх кортежах.

print("\n Task 1")

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
tuple3 = (5, 6, 7, 8, 9)

common_elements = set(tuple1).intersection(set(tuple2), set(tuple3))
result_tuple = tuple(common_elements)

print("Common elements in tuples:", result_tuple)

#   Завдання 2
#  Маємо три кортежі цілих чисел. Знайдіть елементи, які
# унікальні для кожного списку.

print("\n Task 2")

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
tuple3 = (5, 6, 7, 8, 9)

unique_elements = set(tuple1) ^ set(tuple2) ^ set(tuple3)
result_tuple = tuple(unique_elements)

print("Unique elements in tuples:", result_tuple)

#   Завдання 3
#  Маємо три кортежі цілих чисел. Знайдіть елементи, які
# є в кожному з кортежів і знаходяться в кожному з них на тій
# самій позиції

print("\n Task 3")

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
tuple3 = (5, 6, 7, 8, 9)

result_tuple = ()

for i in range(min(len(tuple1), len(tuple2), len(tuple3))):
    if tuple1[i] == tuple2[i] == tuple3[i]:
        result_tuple += (tuple1[i],)

print("Elements that are in the same position in each tuple:", result_tuple)