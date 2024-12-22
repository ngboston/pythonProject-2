#   Завдання 4
# Створіть функцію, що повертає список з усіма парними числами, від 0
# до 100000.
# Використовуючи механізм декораторів, порахуйте скільки секунд знадобилося для обчислення всіх
# чисел.Відобразіть на екран кількість секунд і всі парні числа від 0 до 100000.

# Завдання 5
# Додайте до четвертого завдання можливість передавати межі діапазону для пошуку всіх парних чисел.

print("\n Task 4/5")

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")
        return result
    return wrapper

@timer
def find_even_numbers(start=0, end=100000):
    even_numbers = [num for num in range(start, end+1) if num % 2 == 0]
    return even_numbers

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

even_numbers = find_even_numbers(start_range, end_range)
print(even_numbers)