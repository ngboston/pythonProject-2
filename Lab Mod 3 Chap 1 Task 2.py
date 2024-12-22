#  Завдання 2
#  Користувач вводить з клавіатури рядок. Підрахуйте
# кількість літер та цифр у рядку. Виведіть обидві кількості
# на екран.

string = input("Введить строку: ")
letter = sum(i.isalpha() for i in string)
number = sum(i.isdigit()for i in string)
print(f"Кількість букв: " . format(letter))
print(f"Кількістьо цифр:" . format(number))
