#   Завдання
#  Два списки цілих заповнюються випадковими числами.
# Сформуйте третій список, який містить:
#   ■ елементи обох списків;
#   ■ елементи обох списків без повторень;
#   ■ елементи, спільні для двох списків;
#   ■ тільки унікальні елементи кожного зі списків;
#   ■ тільки мінімальне та максимальне значення кожного зі
#    списків.

import random
length = int(input("Enter the number of items in the lists: "))
choice = int(input(" 1) Elements of both lists \n 2) Elements of both lists without repetitions \n 3) Elements common to two lists \n 4) Only unique elements of each of the lists \n 5) All above \n Enter your choice: "))
list1 = []
list2 = []
if length > 0:
    for i in range(length):
        list1.append(random.randint(0, 50))
        list2.append(random.randint(0, 50))
    print("List 1: ", list1)
    print("List 2: ", list2)
    if choice == 1 or choice == 5:
        list3 = list1 + list2
        print("Elements of both lists: ", list3)
    if choice == 2 or choice == 5:
        list3 = list(set(list1 + list2))
        print("Elements of both lists without repetitions: ", list3)
    if choice == 3 or choice == 5:
        list3 = list(set(list1) & set(list2))
        print("Elements common to two lists: ", list3)
    if choice == 4 or choice == 5:
        list3 = list(set(list1) ^ set(list2))
        print("Only unique elements of each of the lists: ", list3)
else:
    print("Items in lists must be positive:")

