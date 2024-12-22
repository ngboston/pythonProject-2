#    Завдання 1
#   Користувач вводить з клавіатури назву фрукта. Ви
# ведіть на екран кількість фруктів, що містяться в кортежі
# як елемент

print("\n Task 1")

fruits = ('apple', 'banana', 'orange', 'kiwi')
fruit = input("Enter a fruit name: ")
count = fruits.count(fruit)
print(f"There are {count} {fruit}s in the tuple.")

#   Завдання 2
#   Додайте до першого завдання підрахунок кількості,
# коли назва фрукта є частиною елемента. Наприклад,
# banana, apple, bananamango, mango, strawberry-banana.
# У приведеному прикладі banana попадається три рази

print("\n Task 2")

fruits = ('apple', 'banana', 'orange', 'kiwi')
fruit = input("Enter a fruit name: ")
count = 0
for f in fruits:
    if fruit in f:
        count += 1

print(f"There are {count} {fruit}s in the tuple.")

#    Завдання 3
#   Маємо кортеж з назвами автовиробників (назва ви
# робника може зустрічатися від 0 до N разів). Користувач
# вводить з клавіатури назву виробника та слово для заміни.
# Замініть в кортежі усі елементи з цією назвою на слово
# для заміни. Збіг за назвою має бути повним

print("\n Task 3")

cars = [('Toyota', 'Corolla'), ('Honda', 'Civic'), ('Ford', 'Mustang')]
brand = input("Enter a car brand to replace: ")
replace = input("Enter a replacement brand: ")
for i, car in enumerate(cars):
    if car[0] == brand:
        cars[i] = (replace, car[1])

print(cars)

#  Завдання 4
#  Маємо кортеж з цілими числами. Виведіть статистику
# за кількістю цифр в елементах кортежу. Наприклад:
#  Одна цифра — 3 елементи
#  Дві цифри — 4 елементи
#  Три цифри — 5 елементів

print("\n Task 4")

import random

def countL(n):
    l=[]
    for i in n:
        l.append(len(str(abs(i))))
    return l

def tupleN(n):
    l=countL(n)
    m=max(l)
    for i in range(1,m+1):
        print(f"{i} number is {l.count(i)} times")

t=tuple([random.randint(-1000, 1000) for _ in range(10)])
print(t)
tupleN(t)
