#   Завдання 3
#  Напишіть програму для сортування списку методом
# удосконаленого бульбашкового сортування. Удосконалення
# полягає в тому, щоб аналізувати кількість перестановок на
# кожному кроці. Якщо ця кількість дорівнює нулю, то продовжувати сортування немає сенсу — список відсортовано.

def count_of_swaps_in_bubble_sort(a):
    n = len(a)
    unordered = True
    count_of_swaps = 0
    while unordered:
        unordered = False
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                count_of_swaps += 1
        unordered = True
        n -= 1
    return count_of_swaps



