# Завдання 1
# Створіть програму, що містить інформацію про відомих
# баскетболістів. Збережіть ПІБ та зріст кожного баскетболіста. Реалізуйте можливість додавати, видаляти, знаходити та
# змінювати дані. Використовуйте словник для збереження
# інформації.

print("\n Task 1")

basketball_players = {}

def add_player():
    name = input("Enter the basketball player's full name: ")
    height = float(input("Enter the basketball player's height (in meters): "))
    basketball_players[name] = height

def find_player():
    name = input("Enter the basketball player's full name for search: ")

    if name in basketball_players:
        print(f"{name}: {basketball_players[name]} м")
    else:
        print("Basketball player not found.")

def remove_player():
    name = input("Enter the basketball player's full name for removal: ")

    if name in basketball_players:
        del basketball_players[name]
        print(f"{name} removed.")
    else:
        print("Basketball player not found.")

while True:
    print("nMenu:")
    print("1. Add information about a basketball player")
    print("2. Find information about a basketball player")
    print("3. Delete basketball player information")
    print("4. Exit")

    choice = input("Select an action: ")

    if choice == '1':
        add_player()
    elif choice == '2':
        find_player()
    elif choice == '3':
        remove_player()
    elif choice == '4':
        break
    else:
        print("Incorrect selection. Try again.")

# Завдання 2
# Створіть програму «Англо-французький словник». Збережіть слово англійською та його переклад на французьку.
# Реалізуйте можливість додавати, видаляти, знаходити та
# змінювати дані. Використовуйте словник для збереження
# інформації.

print("\n Task 2")

dictionary = {}

def add_translation():
    english_word = input("Введите слово на английском: ")
    french_translation = input("Введите перевод на французский: ")
    dictionary[english_word] = french_translation

def find_translation():
    english_word = input("Enter a word in English to find a translation: ")

    if english_word in dictionary:
        print(f"{english_word}: {dictionary[english_word]}")
    else:
        print("Translation not found.")

def remove_translation():
    english_word = input("Enter a word in English to remove translation: ")
    if english_word in dictionary:
        del dictionary[english_word]
        print(f"Translation for {english_word} removed.")
    else:
        print("Translation not found.")


while True:
    print("nMenu:")
    print("1. Add translation")
    print("2. Find translation")
    print("3. Delete translation")
    print("4. Exit")


    choice = input("Select an action: ")


    if choice == '1':
        add_translation()
    elif choice == '2':
        find_translation()
    elif choice == '3':
        remove_translation()
    elif choice == '4':
        break
    else:
        print("Incorrect selection. Try again.")



# Завдання 3
# Створіть програму «Фірма», яка зберігає інформацію про
# працівників: ПІБ, телефон, корпоративний email, назва посади,
# номер кабінету, Skype. Реалізуйте можливість додавати, видаляти, знаходити та змінювати дані. Використовуйте словник
# для збереження інформації.

print("\n Task 3")

def get_name():
    return input("ВВедіть ПІБ: ")


def find_name(firm_data):
    name = get_name()
    if name in firm_data:
        return name
    print("Працівника не знайдено.")


def get_data():
    phone = input("Введіть номер телефона: ")
    email = input("Введіть email: ")
    position = input("Введить посаду: ")
    room = input("Введіть номер кабінету: ")
    skype = input("ВВедить skype: ")
    return {
        "Телефон": phone,
        "Email": email,
        "Посада": position,
        "Кабінет": room,
        "Skype": skype
    }


def add_inform(firm_data):
    name = get_name()
    data = get_data()
    firm_data[name] = data


def del_inform(firm_data):
    name = find_name(firm_data)
    if name:
        del firm_data[name]


def find_inform(firm_data):
    name = find_name(firm_data)
    if name:
        return firm_data[name]


def replace_inform(firm_data):
    name = find_name(firm_data)
    if name:
        firm_data[name] = get_data()


def choosing_an_action():
    d = {
        1: ("Додати інформацію про працівника", add_inform),
        2: ("Видалити інформацію про працівника", del_inform),
        3: ("Знайти інформацію про працівника", find_inform),
        4: ("Знайти інформацію про працівника", replace_inform),
        5: ("Вийти з програми", exit)
    }
    for k, v in d.items():
        print(f'{k}. {v[0]}')

    k = int(input("Виберіть дію"))
    print(f"Вибрана дія {d[k][0].upper()}")
    return d[k][1]


firm_data = {}
while True:
    print()
    action = choosing_an_action()
    if action == exit:
        exit(0)
    res = action(firm_data)
    print()
    if res:
        print(res)
    else:
        print(firm_data)
    print()



# Завдання 4
# Створіть програму «Книжкова колекція», яка зберігає
# інформацію про книги: автор, назва книги, жанр, рік випуску,
# кількість сторінок, видавництво. Реалізуйте можливість додавати, видаляти, знаходити та змінювати дані. Використовуйте
# словник для збереження інформації.

print("\n Task 4")

def get_name_book():
    return input("Введіть назву книги: ")


def find_name(library_data):
    title = get_name_book()
    if  title in library_data:
        return title
    print("Книгу не знайдено.")


def get_data():
    autor = input("Введіть автора: ")
    title = input("Введить назву: ")
    genre = input("Введить жанр: ")
    year = input("ВВедіть рік видання: ")
    number = input("Введіть кількість сорінок: ")
    publisher = input("Введіть видання: ")
    return {
        "Автор": autor,
        "Назва": title,
        "Жанр": genre,
        "Рік": year ,
        "Сторінки": number,
        "Видання": publisher
    }


def add_inform(library_data):
    title = get_name()
    data = get_data()
    library_data[title] = data


def del_inform(library_data):
    title = find_name(library_data)
    if title:
        del library_data[title]


def find_inform(library_data):
    title = find_name(library_data)
    if title:
        return library_data[title]


def replace_inform(library_data):
    title = find_name(library_data)
    if title:
        library_data[title] = get_data()


def choosing_an_action():
    d = {
        1: ("Добавити інформацію про книгу", add_inform),
        2: ("Видалити інформацію про книгу", del_inform),
        3: ("Знайти інформацію про книгу", find_inform),
        4: ("Замінити інформацію про книгу", replace_inform),
        5: ("Вийти з программи", exit)
    }
    for k, v in d.items():
        print(f'{k}. {v[0]}')

    k = int(input("Виберіть дію"))
    print(f"Вибрана дія {d[k][0].upper()}")
    return d[k][1]


library_data = {}
while True:
    print()
    action = choosing_an_action()
    if action == exit:
        exit(0)
    res = action(library_data)
    print()
    if res:
        print(res)
    else:
        print(librery_data)
    print()
