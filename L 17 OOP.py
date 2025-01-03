class Dog:
    name = None
    age = None
    isHeppy = None

    def set_data(self, dog_name, age, isHeppy): # Перший метод
        self.name = dog_name
        self.age = age
        self.isHeppy = isHeppy

    def get_data(self):
        print(self.name, "age:", self.age, ".Happy: ", self.isHeppy)

dog1 = Dog()
dog1.set_data("Skubby", 3, True)
# dog1.name = "Skubby"
# dog1.age = 3
# dog1.isHeppy = True

dog2 = Dog()
dog2.set_data("Bob", 5, False)
# dog2.name = "Bob"
# dog1.age = 5
# dog1.isHeppy = False

# print(dog1.name)
# print(dog2.name)
dog1.get_data()
dog2.get_data()