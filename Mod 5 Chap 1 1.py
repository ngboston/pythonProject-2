#   Завдання 1

#  Відсортуйте перші дві третини списку в порядку зростання, якщо середнє арифметичне всіх елементів більше за нуль;
# якщо ні — тільки першу третину. Решту списку не сортуйте,
# а розташуйте у зворотному порядку

from random import randint


def fun(lst, n):
    return sorted(lst[:n]) + lst[n:][::-1]


a = [randint(-10, 11) for _ in range(11)]
m = len(a)
k = m // 3 + (m == 0)
print(a)
res = fun(a, (1 + (sum(a) / k > 0)) * k)
print(res)

#   Завдання 2

#  Написати програму «Успішність». Користувач вводить
# 10 оцінок студента. Оцінки від 1 до 12. Реалізуйте меню для
# користувача:
#   ■ виведення оцінок (виведення вмісту списку);
#   ■ перескладання іспиту (користувач вводить номер елемента
#   списку та нову оцінку);
#   ■ отримання стипендії (стипендію отримують, якщо середній бал не нижче 10.7);
#   ■ виведення відсортованого списку оцінок: за зростанням
#   або спаданням.

score = []
for i in range(1, 11):
    b = 0
    while b < 1 or b > 12:
        try:
            b = int(input(f'{i} Оцінка: '))
        except:
            b = 0
    score.append(b)

option = 0
while option == 0:
    print('\n1. Виведення вмісту списку', '2. Перездача іспиту', '3. Чи отримується стипендія ',
          '4. Сортування списку по зростанню', '5. Сортуванню оцінок по спаданню', '6. Вихід', '\n', sep='\n')
    try:
        option = int(input())
        if option == 1:
            for i, val in enumerate(score):
                print(i + 1, ' - ', val)
        elif option == 2:
            try:
                index = int(input('ВВедіть номер екзамену: '))
                val = int(input('Введите оценку: '))
                if val > 0 and val < 13:
                    score[index - 1] = val
                    print('Оцінка змінена')
            except:
                print('Помилка!')
                option = 0
        elif option == 3:
            if sum(score) / len(score) >= 10.7:
                print('Стипендію отримують.')
            else:
                print('Стипендію не отримують.')
        elif option == 4:
            print(sorted(score))
        elif option == 5:
            print(sorted(score, reverse=True))
        if option != 6:
            option = 0
    except:
        option = 0

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
