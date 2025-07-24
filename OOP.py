import random

egyptian_banks = [
    "National Bank of Egypt", "Banque Misr", "Banque du Caire",
    "Commercial International Bank (CIB)", "Arab African International Bank (AAIB)",
    "QNB Alahli", "AlexBank", "Abu Dhabi Islamic Bank Egypt (ADIB)",
    "Faisal Islamic Bank of Egypt", "Al Baraka Bank Egypt", "Mashreq Bank Egypt"
]

class Bank:
    def __init__(self):
        self.name = random.choice(egyptian_banks)

    def welcome_message(self):
        print("Welcome to", self.name)
        return self.name

class Customer:
    def __init__(self):
        self.name = input("What is your name? ")
        self.balance = self.get_initial_balance()

    def get_initial_balance(self):
        while True:
            balance = float(input("Enter your current balance? "))
            if balance < 0:
                print("Balance cannot be negative. Try again.")
                continue
            return balance

class SystemOperation:
    def __init__(self, customer, bank):
        self.customer = customer
        self.bank = bank

    def check_balance(self):
        print(self.customer.name, ", Your current balance is", self.customer.balance)

    def deposit(self):
        while True:
            amount = float(input("Enter your deposit amount? "))
            if amount < 0:
                print("Unsuccessful operation. Amount cannot be negative.")
                continue
            else:
                self.customer.balance += amount
                print("Successful Operation.", self.customer.name, ", Your new balance is", self.customer.balance)
                break

    def withdraw(self):
        while True:
            amount = float(input("Enter your withdraw amount? "))
            if amount < 0:
                print("Unsuccessful operation. Amount cannot be negative.")
                continue
            elif self.customer.balance < amount:
                print("Sorry, not enough money!")
                continue
            else:
                self.customer.balance -= amount
                print("Successful Operation.", self.customer.name, "Your new balance is", self.customer.balance)
                break

    def exit_program(self):
        print(f"Thank you for using {self.bank.name}!")



def main():

    def main_menu():
        choice = int(input(f"Welcome {customer.name}. Choose the number of the operation you would like to do: "
                           "\n1. Check Balance "
                           "\n2. Deposit "
                           "\n3. Withdraw "
                           "\n4. Exit\n"))

        while True:
            if choice == 1:
                ops.check_balance()
            elif choice == 2:
                ops.deposit()
            elif choice == 3:
                ops.withdraw()
            elif choice == 4:
                ops.exit_program()
                break
            else:
                print("Invalid choice. Try again.")

            want_to_continue = input("Do you make to do another operation? (Yes/No) ")
            if want_to_continue.lower() == "yes":
                choice = int(input("Choose the number of the operation you would like to do: "
                                   "\n1. Check Balance "
                                   "\n2. Deposit "
                                   "\n3. Withdraw "
                                   "\n4. Exit\n"))
            elif want_to_continue.lower() == "no":
                choice = 4
            else:
                print("Invalid choice. Try again.")
                break



    bank = Bank()
    bank.welcome_message()
    customer = Customer()
    ops = SystemOperation(customer,bank)
    main_menu()



