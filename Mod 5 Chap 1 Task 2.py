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
            b = int(input(f'{i} оценка: '))
        except:
            b = 0
    score.append(b)

option = 0
while option == 0:
    print('\n1. Вывод списка оценок', '2. Пересдача экзамена', '3. Выходит ли стипендия',
          '4. Сортировка оченок по возрастанию', '5. Сортировка оченок по убыванию', '6. Выход', '\n', sep='\n')
    try:
        option = int(input())
        if option == 1:
            for i, val in enumerate(score):
                print(i + 1, ' - ', val)
        elif option == 2:
            try:
                index = int(input('Введите номер экзамена: '))
                val = int(input('Введите оценку: '))
                if val > 0 and val < 13:
                    score[index - 1] = val
                    print('Оценка изменена')
            except:
                print('Ошибка!')
                option = 0
        elif option == 3:
            if sum(score) / len(score) >= 10.7:
                print('Стипендия выходит :)')
            else:
                print('Стипендия не выходит :(')
        elif option == 4:
            print(sorted(score))
        elif option == 5:
            print(sorted(score, reverse=True))
        if option != 6:
            option = 0
    except:
        option = 0