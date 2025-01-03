class Dog:
    name = None
    age = None
    isHeppy = None

    def __init__(self, name = "Bob", age = 1, isHeppy = True):
        self.set_data(name, age, isHeppy)
        self.get_data()
        # print("Object is created")
        # self.name = name
        # self.age = age
        # self.isHeppy = isHeppy

    def set_data(self, dog_name, age = 1, isHeppy = True): # Перший метод
        self.name = dog_name
        self.age = age
        self.isHeppy = isHeppy

    def get_data(self):# Другий метод
        print(self.name, "age:", self.age, ".Happy: ", self.isHeppy)

dog1 = Dog("Alex")
dog3 = Dog(age=7)
# dog1 = Dog("Skubby", 3, True)
# dog1.set_data("Alex", 5)
# dog1.set_data("Skubby", 3, True)
# dog1.name = "Skubby"
# dog1.age = 3
# dog1.isHeppy = True

dog2 = Dog("Bob", 5, False)
# dog2.set_data("Bob", 5, False)
# dog2.name = "Bob"
# dog1.age = 5
# dog1.isHeppy = False

# print(dog1.name)
# print(dog2.name)
# dog1.get_data()
# dog2.get_data()