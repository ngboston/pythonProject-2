#   Завдання 1:
# Створіть клас BankAccount з атрибутами account_number (номер рахунку) і balance (баланс рахунку), а також методами
# deposit, який додає певну суму до балансу, і withdraw, який знімає певну суму з балансу. Метод withdraw повинен
# перевіряти, чи є на рахунку достатньо коштів перед зняттям.

print("\n Task 1")

class BankAccount():
    def __init__(self):
        self.balance = 0

    def deposit(self, summa):
        self.balance += summa
        return self.balance

    def withdraw(self, summa):
        if self.balance < summa: raise
        self.balance -= summa
        return self.balance


my_bank_account = BankAccount()
print(my_bank_account.deposit(1000))
try:
    print(my_bank_account.withdraw(100))
except:
    print("Недостатньо коштів на рахунку")

print("\n Task 1.2")


class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

    def display(self):
        print("\n Net Available Balance=", self.balance)


s = Bank_Account()

s.deposit()
s.withdraw()
s.display()

# Завдання 2:
# Створіть клас Car з атрибутами make (марка автомобіля), model (модель автомобіля) і year (рік випуску автомобіля),
# а також методом get_info, який повертає рядок з інформацією про автомобіль у форматі "[рік] [марка] [модель]".

print("\n Task 2")

class Car:
    def __init__(self, year, mark, model):
        self.mark = mark
        self.model = model
        self.year = year


# Завдання 3:
# Створіть клас Employee з атрибутами name (ім'я працівника), position (посада працівника) і salary (заробітна плата
# працівника), а також методом get_salary_info, який повертає рядок з інформацією про заробітну плату у форматі
# "Заробітна плата [ім'я]: [заробітна плата]".

print("\n Task 2")
