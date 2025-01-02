class Bank:
    def __init__(self, name, address, phone, website, swift_code, routing_number, account_types, interest_rates):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__website = website
        self.__swift_code = swift_code
        self.__routing_number = routing_number
        self.__account_types = account_types
        self.__interest_rates = interest_rates

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def get_website(self):
        return self.__website

    def get_swift_code(self):
        return self.__swift_code

    def get_routing_number(self):
        return self.__routing_number

    def get_account_types(self):
        return self.__account_types

    def get_interest_rates(self):
        return self.__interest_rates

    def open_account(self, customer_name, account_type, initial_deposit):
        if account_type in self.__account_types:
            interest_rate = self.__interest_rates[account_type]
            account_number = self.__generate_account_number()
            account = BankAccount(customer_name, account_type, account_number, initial_deposit, interest_rate)
            print(f"Congratulations, {customer_name}! Your {account_type} account has been opened with account number {account_number}.")
            return account
        else:
            print(f"Sorry, {account_type} is not a valid account type at this bank.")
            return None

    def __generate_account_number(self):
        return "123456789"

class BankAccount:
    def __init__(self, customer_name, account_type, account_number, balance, interest_rate):
        self.__customer_name = customer_name
        self.__account_type = account_type
        self.__account_number = account_number
        self.__balance = balance
        self.__interest_rate = interest_rate

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount} to your {self.__account_type} account. New balance: {self.__balance}")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Withdrew {amount} from your {self.__account_type} account. New balance: {self.__balance}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Your {self.__account_type} account balance is: {self.__balance}")

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, account_number, balance, interest_rate):
        super().__init__(customer_name, "Savings", account_number, balance, interest_rate)

    def apply_interest(self):
        interest_earned = self._BankAccount__balance * self._BankAccount__interest_rate
        self._BankAccount__balance += interest_earned
        print(f"Interest of {interest_earned} has been applied to your Savings account. New balance: {self._BankAccount__balance}")

# Создание экземпляра банка
bank = Bank(
    "ABC Bank",
    "123 Main St, Anytown USA",
    "555-1234",
    "www.abcbank.com",
    "ABCBUSXX",
    "123456789",
    ["Checking", "Savings", "CD"],
    {"Checking": 0.01, "Savings": 0.02, "CD": 0.03}
)

account = bank.open_account("John Doe", "Savings", 1000)

account.deposit(500)
account.withdraw(200)
account.check_balance()

if isinstance(account, SavingsAccount):
    account.apply_interest()