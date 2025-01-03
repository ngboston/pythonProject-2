class Build:
    __year = None  # Інкапсуляція закриваємо поля
    __city = None

    def __init__(self, year, city):# Конструктор головного класу
        self.year = year
        self.city = city

    def get_info(self):
        print("Yeas: ", self.year, ".City: ", self.city, sep='')

class School(Build):# Спадковий клас 1
    __pupils = None
    
    def __init__(self, year, city, pupils=500):
        super(School, self).__init__(year, city) # super Звернення до головного класу
        self.pupils = pupils
        
    def get_info(self):# Поліморфизм
        super().get_info()
        print("Pupils:", self.pupils)
        
    
class House(Build):# Спадковий клас 2
    pass

class Shop(Build):# Спадковий клас 3
    pass

school = School(1990, "Seattle", 700) # Обєкти
school.get_info()
house = Build(2010, "New York")
house.get_info()
shop = Build(2000, "Miami")
shop.get_info()