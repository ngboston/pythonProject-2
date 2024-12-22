#  Завдання 1
#  Маємо множину з назвами країн. Надайте користу
# вачеві можливість:
#  ■ додавати країни;
#  ■ видаляти країни;
#  ■ пошуку країн за введеними символами;
#  ■ перевіряти, чи міститься країна в множині.

print("\n Task 1")


def country_F():
    country = {"usa", "canada", "mexico"}
    while True:
        print(country)
        n = int(input("1- Add country,\n2- Remove counry, \n3- Find symbol country,\n4- Find country, \n5- Exit: "))

        if n == 1:
            country.add(input("Add country: "))
        elif n == 2:
            country.remove(input("Remove country: "))
        elif n == 3:
            f = input("enter symbol to find: ")
            for i in country:
                if f in i:
                    print(f"{f} is {i}")

        elif n == 4:
            f = input("Enter country to find: ")
            for i in country:
                if f == i:
                    print(f"Country {i} found")
        else:
            print("Task done")
            break
country_F()

#  Завдання 2
#  Маємо дві множини з назвами міст. Створіть третю
# множину з тими назвами, які є в обох множинах.

print("\n Task 2")

set1 = {'New York', 'Los Angeles', 'Chicago', 'Houston'}
set2 = {'San Francisco', 'Los Angeles', 'Seattle', 'Houston'}
intersection = set1.intersection(set2)
print(intersection)

#  Завдання 3
#  Маємо дві множини з назвами міст. Створіть третю
# множину з тими назвами, які містяться в першій множині,
# але відсутні у другій.

print("\n Task 3")

set1 = {'New York', 'Los Angeles', 'Chicago', 'Houston'}
set2 = {'San Francisco', 'Los Angeles', 'Seattle', 'Houston'}
difference = set1.difference(set2)
print(difference)

#  Завдання 4
#  Маємо дві множини з назвами міст. Створіть третю
# множину з тими назвами, які містяться в другій множині,
# але відсутні в першій.

print("\n Task 4")

set1 = {'New York', 'Los Angeles', 'Chicago', 'Houston'}
set2 = {'San Francisco', 'Los Angeles', 'Seattle', 'Houston'}
difference = set2.difference(set1)
print(difference)

#  Завдання 5
#  Маємо дві множини з назвами міст. Створіть третю
# множину з унікальними назвами для кожної множини.

print("\n Task 5")

set1 = {'New York', 'Los Angeles', 'Chicago', 'Houston'}
set2 = {'San Francisco', 'Los Angeles', 'Seattle', 'Houston'}
symmetric_difference = set1.symmetric_difference(set2)
print(symmetric_difference)

#  Завдання 6
#  У словнику зберігається набір пар: Назва країни ->
# Столиця. Реалізуйте функціональність за додаванням,
# видаленням, пошуком, заміною

print("\n Task 6")

dct = {"USA": "Washington", "Canada": "Ottawa"}
print(dct, "- existing dictionary")


def getDict():
    r = {}
    while True:
        print("Enter country: ")
        k = input()
        if k == '':
            break
        print("Enter the country's capital: ")
        v = input()
        r[k] = v
    return r


d = getDict()
print(dct)


def search():
    a = int(input("search capital by country - 1, search country by capital - 2 >>: "))
    if a == 1:
        name = input("Enter country: ").title()
        if name in dct:
            print(f"country - {name}, capital - {dct[name]}")
        else:
            print("There is no data in the database")
    elif a == 2:
        name = input("Enter capital: ").title()
        if name in dct.values():
            for key, val in dct.items():
                if val == name:
                    print(f"capital - {val}, country  - {key}")
        else:
            print("There is no data in the database")
    else:
        print("enter the correct number")


def getDict():
    while True:
        k = input("Enter country: ")
        if k == '':
            break
        v = input("Enter capital: ")
        dct[k.title()] = v.title()


dct = {"USA": "Washington", "Canada": "Ottawa"}
print(dct, "- existing dictionary")
while True:
    print("add - 1, search - 2")
    num = int(input("your choice>>: "))
    if num == 1:
        getDict()
        print(dct)
    elif num == 2:
        search()
    else:
        print('bye!')
        break
