import random

class Student:
    def __init__(self, name,money=0, is_studying=True):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.money = money
        self.is_studying = is_studying

    def to_study(self):
        print("I'm study")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("I'm sllep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.progress -= 0.1
        self.gladness += 5

    def is_alive(self):
        if self.progress < -0.5:
            print("Відрахували")
            self.alive = False
        elif self.gladness <= 0:
            print("Йому потрібний друг")
            self.alive = False
        elif self.progress > 5:
            print("Закінчив курс екстерном")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.progress, 2)}")

    def live(self, day):
        print(f"Day {day} of {self.name}")

        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()

        self.end_of_day()
        self.is_alive()

# bohdan = Student("Bohdan")
# for day in range(355):
#     if bohdan.alive == False:
#         break
#     bohdan.live(day)

# """РОзширте клас студента, додавши йому арибуи гроші, реалізуйте можливість заробітку,
#     під час відпочинку гроші витрачаються.
#    Глибще продумайте поведінку студента, наприклад, якщо пракує коштів, він має піти на роботу, якщо проблеми з навчанням то вчиться"""


    def earn_money(self, amount):
        self.money += amount
        print(f"{self.name} earned {amount} money. Total money: {self.money}")


    def spend_money(self, amount):
        if self.money >= amount:
            self.money -= amount
            print(f"{self.name} spent {amount} money. Total money: {self.money}")
        else:
            print(f"{self.name} does not have enough money to spend {amount}.")


    def study(self):
        if not self.is_studying:
            print(f"{self.name} is now studying.")
            self.is_studying = True
        else:
            print(f"{self.name} is already studying.")


    def relax(self):
        if self.money >= 10:
            self.spend_money(10)
            print(f"{self.name} is relaxing.")
        else:
            print(f"{self.name} needs to earn more money to relax.")


    def work(self):
        if not self.is_studying:
            print(f"{self.name} is now working.")
            self.earn_money(50)
        else:
            print(f"{self.name} cannot work while studying.")


student1 = Student("Bohdan", 30)
student1.study()
student1.relax()
student1.earn_money(300)
student1.relax()
student1.work()
student1.study()
student1.work()

bohdan = Student("Bohdan")
for day in range(355):
   if bohdan.alive == False:
       break
   bohdan.live(day)