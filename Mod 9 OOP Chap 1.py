#    Завдання 1
#   Реалізуйте клас «Автомобіль». Збережіть у класі: назву
# моделі, рік випуску, виробника, об’єм двигуна, колір машини,
# ціну. Реалізуйте методи класу для введення-виведення даних
# та інших операцій.

print("\n Task 1")

class Car:
    def __init__(self, model, year, manufacturer, engine_volume, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def display_info(self):
        print(f"Модель: {self.model}")
        print(f"Рік випуску: {self.year}")
        print(f"Виробник: {self.manufacturer}")
        print(f"Об'єм двигуна: {self.engine_volume} л")
        print(f"Колір: {self.color}")
        print(f"Ціна: {self.price} грн")

    def update_price(self, new_price):
        self.price = new_price

car = Car("Toyota Camry", 2020, "Toyota", 2.5, "Білий", 500000)
car.display_info()
car.update_price(550000)
car.display_info()

#    Завдання 2
#  Реалізуйте клас «Книга». Збережіть у класі: назву книги,
# рік видання, видавця, жанр, автора, ціну. Реалізуйте методи
# класу для введення-виведення даних та інших операцій.

print("\n Task 2")

class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Назва: {self.title}")
        print(f"Рік видання: {self.year}")
        print(f"Видавець: {self.publisher}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        print(f"Ціна: {self.price} грн")

    def update_price(self, new_price):
        self.price = new_price

book = Book("Кобзар", 1840, "Видавництво Л. Тризна", "Поезія", "Тарас Шевченко ", 3000)
book.display_info()
book.update_price(3500)
book.display_info()

#    Завдання 3
#  Реалізуйте клас «Стадіон». Збережіть у класі: назву стадіону, дату відкриття, країну, місто, місткість. Реалізуйте методи
# класу для введення-виведення даних та інших операцій.

print("\n Task 3")

class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def display_info(self):
        print(f"Назва стадіону: {self.name}")
        print(f"Дата відкриття: {self.opening_date}")
        print(f"Країна: {self.country}")
        print(f"Місто: {self.city}")
        print(f"Місткість: {self.capacity}")

    def update_capacity(self, new_capacity):
        self.capacity = new_capacity

stadium = Stadium("Олімпійський", "10.10.1924", "Україна", "Київ", 70050)
stadium.display_info()
stadium.update_capacity(71000)
stadium.display_info()




