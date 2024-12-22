class Human:
    def __init__(self, name="Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = [] # тільки об'єкти класу Human

    def add_passenger(self, *human):
        myset1 = set(human)
        for p in myset1:
            self.passengers.append(p)

    def print_pessagers_names(self):
        if self.passengers != []:
            print(f"Name of {self.brand} passngers: ")
            for p in self.passengers:
                print(p.name)
        else:
            print(f"No passengers in {self.brand}")


nick = Human("Nick")
kate = Human("Kate")

car = Auto("Mercedes")

car.add_passenger(nick)
car.add_passenger("")
car.add_passenger(kate)
car.print_pessagers_names()