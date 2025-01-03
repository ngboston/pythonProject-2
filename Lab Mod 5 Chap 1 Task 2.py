#  Завдання 2
#  Напишіть програму для сортування списку цілих
# чисел методом вставок

unsorted = [9,8,7,6,5,4,3,3,2,1]
size_unsorted = len(unsorted)
print("\nUnsorted: ", end="")
for i in range(size_unsorted):
    print(unsorted[i], end=" ")
for i in range(1, size_unsorted):
    current_element = unsorted[i]
    j = i - 1
    while j >= 0 and unsorted[j] > current_element:
        unsorted[j+1], unsorted[j] = unsorted[j], unsorted[j+1]
        j -= 1
print("\nSorted: ", end="")
for i in range(size_unsorted):
    print(unsorted[i], end=" ")