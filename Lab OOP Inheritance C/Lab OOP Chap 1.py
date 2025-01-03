# Завдання 1
# Створіть клас Device, який містить інформацію про пристрій.
# За допомогою механізму успадкування реалізуйте клас CoffeeMachine (містить інформацію про кавомашину), клас Blender
# (містить інформацію про блендер), клас MeatGrinder (містить інформацію про м'ясорубку).
# Кожен із класів має містити необхідні для роботи методи.

print("\n Task 1")

class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power

    def turn_on(self):
        print(f"{self.brand} {self.model} is turned on.")

    def turn_off(self):
        print(f"{self.brand} {self.model} is turned off.")

class CoffeeMachine(Device):
    def __init__(self, brand, model, power, water_capacity):
        super().__init__(brand, model, power)
        self.water_capacity = water_capacity

    def make_coffee(self):
        print(f"{self.brand} {self.model} is making coffee.")

class Blender(Device):
    def __init__(self, brand, model, power, speed_levels):
        super().__init__(brand, model, power)
        self.speed_levels = speed_levels

    def blend(self):
        print(f"{self.brand} {self.model} is blending.")

class MeatGrinder(Device):
    def __init__(self, brand, model, power, capacity):
        super().__init__(brand, model, power)
        self.capacity = capacity

    def grind_meat(self):
        print(f"{self.brand} {self.model} is grinding meat.")


coffee_machine = CoffeeMachine("Breville", "Barista Express", 1500, 2)
blender = Blender("Vitamix", "Professional Series 750", 1200, 10)
meat_grinder = MeatGrinder("KitchenAid", "Stand Mixer Attachment", 500, 2)

coffee_machine.turn_on()
coffee_machine.make_coffee()
coffee_machine.turn_off()

blender.turn_on()
blender.blend()
blender.turn_off()

meat_grinder.turn_on()
meat_grinder.grind_meat()
meat_grinder.turn_off()

# Завдання 2
# Створіть клас Ship, який містить інформацію про кораблі. За допомогою механізму успадкування реалізуйте клас Frigate
# (містить інформацію про фрегат), клас Destroyer (містить інформацію про есмінця), клас Cruiser (містить інформацію
# про крейсер).
# Кожен із класів має містити необхідні для роботи методи.

print("\n Task 2")

class Ship:
    def __init__(self, name, displacement, crew_size):
        self.name = name
        self.displacement = displacement
        self.crew_size = crew_size

    def print_info(self):
        print(f"Ship Name: {self.name}")
        print(f"Displacement: {self.displacement} tons")
        print(f"Crew Size: {self.crew_size}")

    def increase_crew(self, additional_crew):
        self.crew_size += additional_crew
        print(f"Crew size increased to {self.crew_size}")

    def decrease_crew(self, reduced_crew):
        self.crew_size -= reduced_crew
        print(f"Crew size decreased to {self.crew_size}")

class Frigate(Ship):
    def __init__(self, name, displacement, crew_size, num_guns, speed):
        super().__init__(name, displacement, crew_size)
        self.num_guns = num_guns
        self.speed = speed

    def print_info(self):
        super().print_info()
        print(f"Number of Guns: {self.num_guns}")
        print(f"Speed: {self.speed} knots")

    def increase_speed(self, additional_speed):
        self.speed += additional_speed
        print(f"Speed increased to {self.speed} knots")

    def decrease_speed(self, reduced_speed):
        self.speed -= reduced_speed
        print(f"Speed decreased to {self.speed} knots")

class Destroyer(Ship):
    def __init__(self, name, displacement, crew_size, num_torpedoes, range):
        super().__init__(name, displacement, crew_size)
        self.num_torpedoes = num_torpedoes
        self.range = range

    def print_info(self):
        super().print_info()
        print(f"Number of Torpedoes: {self.num_torpedoes}")
        print(f"Range: {self.range} nautical miles")

    def increase_torpedoes(self, additional_torpedoes):
        self.num_torpedoes += additional_torpedoes
        print(f"Number of Torpedoes increased to {self.num_torpedoes}")

    def decrease_torpedoes(self, reduced_torpedoes):
        self.num_torpedoes -= reduced_torpedoes
        print(f"Number of Torpedoes decreased to {self.num_torpedoes}")

class Cruiser(Ship):
    def __init__(self, name, displacement, crew_size, num_missiles, armor_thickness):
        super().__init__(name, displacement, crew_size)
        self.num_missiles = num_missiles
        self.armor_thickness = armor_thickness

    def print_info(self):
        super().print_info()
        print(f"Number of Missiles: {self.num_missiles}")
        print(f"Armor Thickness: {self.armor_thickness} mm")

    def increase_missiles(self, additional_missiles):
        self.num_missiles += additional_missiles
        print(f"Number of Missiles increased to {self.num_missiles}")

    def decrease_missiles(self, reduced_missiles):
        self.num_missiles -= reduced_missiles
        print(f"Number of Missiles decreased to {self.num_missiles}")

    def increase_armor(self, additional_armor):
        self.armor_thickness += additional_armor
        print(f"Armor Thickness increased to {self.armor_thickness} mm")

    def decrease_armor(self, reduced_armor):
        self.armor_thickness -= reduced_armor
        print(f"Armor Thickness decreased to {self.armor_thickness} mm")


ship1 = Ship("USS Enterprise", 100000, 5000)
frigate1 = Frigate("HMS Dauntless", 5000, 300, 20, 30)
destroyer1 = Destroyer("USS Arleigh Burke", 9000, 380, 12, 4000)
cruiser1 = Cruiser("USS Ticonderoga", 15000, 500, 80, 200)


ship1.print_info()
print()
frigate1.print_info()
print()
destroyer1.print_info()
print()
cruiser1.print_info()


ship1.increase_crew(100)
frigate1.increase_speed(5)
destroyer1.increase_torpedoes(4)
cruiser1.increase_missiles(10)
cruiser1.increase_armor(50)


# Завдання 3
# Запрограмуйте клас Money (об'єкт класу оперує однією валютою) для роботи з грошима.
# У класі мають бути передбачені: поле для зберігання цілої частини грошей (долари, євро, гривні тощо) і поле для
# зберігання копійок (центи, євроценти, копійки тощо).
# Реалізуйте методи виведення суми на екран, задання значень частин.
# Створіть клас Product для роботи з продуктом або товаром беручи за основу клас Money. Реалізуйте метод для зменшення
# ціни на задане число.
# Для кожного з класів реалізуйте необхідні методи та поля.

print("\n Task 3")

class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def __str__(self):
        return f"{self.dollars}.{self.cents:02d}"

    def set_dollars(self, dollars):
        self.dollars = dollars

    def set_cents(self, cents):
        self.cents = cents

    def add(self, other):
        total_cents = self.cents + other.cents
        total_dollars = self.dollars + other.dollars
        if total_cents >= 100:
            total_dollars += 1
            total_cents -= 100
        return Money(total_dollars, total_cents)

    def subtract(self, other):
        total_cents = self.cents - other.cents
        total_dollars = self.dollars - other.dollars
        if total_cents < 0:
            total_dollars -= 1
            total_cents += 100
        return Money(total_dollars, total_cents)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}"

    def decrease_price(self, amount):
        self.price = self.price.subtract(amount)

money1 = Money(10, 50)
money2 = Money(5, 75)


print(money1)
print(money2)


total = money1.add(money2)
print(total)

difference = money1.subtract(money2)
print(difference)


product = Product("Apple", Money(2, 99))
print(product)


product.decrease_price(Money(0, 50))
print(product)