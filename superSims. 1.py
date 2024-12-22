import random

brands_of_car = {
    "BMW" : {"fuuel":100, "strength":100, "consumption":6},
    "Volvo" : {"fuuel":75, "strength":69, "consumption":8},
    "Zaz" : {"fuuel":45, "strength":30, "consumption":15},
    "Ford" : {"fuuel":80, "strength":130, "consumption":4},
}

job_list = {
    "Java dev" : {"salary":50, "gladness_less":10},
    "Python dev" : {"salary":50, "gladness_less":10},
    "Assambler dev" : {"salary":50, "gladness_less":10},
    "Swift dev" : {"salary":50, "gladness_less":10},
}

class Human:
     def __init__(self, name="Human", home=None,  job=None, car=None):
         self.name = name
         self.mony = 100
         self.gladness = 10
         self.home = home
         self.job = job
         self.car = car

     def get_home(self):
         self.h

     def get_car(self):
         pass

     def get_job(self):
         pass

     def eat(self):
         pass

     def worck(self):
         pass

     def shopping(self, manage):
         pass

     def chil(self):
         pass

     def to_repair(self):
         pass

     def is_alive(self):
         pass

     def live(self, day):
         pass

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brands_of_car[self.brand]["fuel"]
        self.strength = brands_of_car[self.brand]["stregth"]
        self.consumption = brands_of_car[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("Car cant move")
            return False

class Nouse:
    def __init__(self):
        self.mess = 0
        self.food = 0

class job:
    def __init__(self, job_list):












