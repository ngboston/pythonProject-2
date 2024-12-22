from random import randint


def bubble(array):
    iterations = len(array) - 1
    for i in range(iterations):
        for j in range(iterations-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


a = [randint(1, 99) for n in range(10)]
print(a)
bubble(a)
print(a)

from random import randint

N = 10
# Вариант заполнения списка с помощью спискового выражения:
a = [randint(1, 99) for n in range(N)]
print(a)

i = 0
while i < N-1:
    j = 0
    while j < N-1-i:
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
        j += 1
    i += 1

print(a)

from random import randint

N = 10  # количество элементов в списке
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)  # вывод исходного неотсортированного списка

# Сама сортировка методом "пузырька"
for i in range(N-1):
    for j in range(N-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)  # вывод отсортированного списка