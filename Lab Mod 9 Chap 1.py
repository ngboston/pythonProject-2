#   Завдання 1
#  Реалізуйте клас «Людина». Збережіть у класі: ПІБ,
# дату народження, контактний телефон, місто, країну,
# домашню адресу. Реалізуйте методи класу для введен
# ня-виведення даних та інших операцій

print("\n Task 1")

class Person:
    def __init__(self, name, birth_date, phone, city, country, address):
        self.name = name
        self.birth_date = birth_date
        self.phone = phone
        self.city = city
        self.country = country
        self.address = address
    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Birth date: {self.birth_date}")
        print(f"Phone: {self.phone}")
        print(f"City: {self.city}")
        print(f"Country: {self.country}")
        print(f"Address: {self.address}")
    def update_phone(self, new_phone):
        self.phone = new_phone
        print(f"Phone number updated to: {self.phone}")
    def update_address(self, new_address):
        self.address = new_address
        print(f"Address updated to: {self.address}")

person = Person("John Doe", "1985-05-15", "555-1234", "New York", "USA", "123 Main St")
person.get_info()
person.update_phone("555-5678")
person.update_address("456 Park Ave")
person.get_info()

#    Завдання 2
#  Створіть клас «Місто». Збережіть у класі: назву міста,
# назву регіону, назву країни, кількість жителів у місті,
# поштовий індекс міста, телефонний код міста. Реалізуйте
# методи класу для введення-виведення даних та інших
# операцій.

print("\n Task 2")