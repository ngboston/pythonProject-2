class Bank:
    def __init__(self, name, address, phone, website, swift_code, routing_number, account_types, interest_rates):
        self.name = name
        self.address = address
        self.phone = phone
        self.website = website
        self.swift_code = swift_code
        self.routing_number = routing_number
        self.account_types = account_types
        self.interest_rates = interest_rates

    def open_account(self, customer_name, account_type, initial_deposit):
        if account_type in self.account_types:
            interest_rate = self.interest_rates[account_type]
            account_number = self.generate_account_number()
            account = BankAccount(customer_name, account_type, account_number, initial_deposit, interest_rate)
            print(f"Congratulations, {customer_name}! Your {account_type} account has been opened with account number {account_number}.")
            return account
        else:
            print(f"Sorry, {account_type} is not a valid account type at this bank.")
            return None

    def generate_account_number(self):
        return "123456789"

class BankAccount:
    def __init__(self, customer_name, account_type, account_number, balance, interest_rate):
        self.customer_name = customer_name
        self.account_type = account_type
        self.account_number = account_number
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} to your {self.account_type} account. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from your {self.account_type} account. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Your {self.account_type} account balance is: {self.balance}")


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

account = bank.open_account("John Doe", "Checking", 1000)

account.deposit(500)
account.withdraw(200)
account.check_balance()