import random

egyptian_banks = [ "National Bank of Egypt","Banque Misr","Banque du Caire","Commercial International Bank (CIB)",
                   "Arab African International Bank (AAIB)","QNB Alahli","AlexBank","Abu Dhabi Islamic Bank Egypt (ADIB)",
                    "Faisal Islamic Bank of Egypt","Al Baraka Bank Egypt","Mashreq Bank Egypt"]

def welcome_message():
    bank_name = random.choice(egyptian_banks)
    print("Welcome to", bank_name)
    return bank_name

def personal_info():
    name = input("What is your name? ")

    while True:
            balance = float(input("Enter your current balance? "))
            if balance < 0:
                print("Balance cannot be negative. Try again.")
                continue
            break

    return {"name": name, "balance": balance}

def main_menu(user_account, bank):
    choice = int(input(f"Welcome {user_account['name']}. Choose the number of the operation you would like to do: "
                       "\n1. Check Balance "
                       "\n2. Deposit "
                       "\n3. Withdraw "
                       "\n4. Exit\n"))

    while True:
        if choice == 1:
            check_balance(user_account)
        elif choice == 2:
            deposit(user_account)
        elif choice == 3:
            withdraw(user_account)
        elif choice == 4:
            exit_program(bank)
            break
        else:
            print("Invalid choice. Try again.")

        want_to_continue = input("Do you make to do another operation? (Yes/No)")
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

    return

def check_balance(user):
    print(user["name"],", Your current balance is", user["balance"])
    return

def deposit(user):

    while True:
        amount = float(input("Enter your deposit amount? "))
        if amount < 0:
            print("Unsuccessful operation. Amount cannot be negative.")
            continue
        else:
            user["balance"] += amount
            print("Successful Operation.",user["name"],", Your new balance is", user["balance"])
            break
    return

def withdraw(user):
    while True:
        amount = float(input("Enter your withdraw amount? "))
        if amount < 0:
            print("Unsuccessful operation. Amount cannot be negative.")
            continue
        elif user["balance"] < amount:
            print("Sorry, not enough money!")
            continue
        else:
            user["balance"] -= amount
            print("Successful Operation.",user["name"],"Your new balance is", user["balance"])
            break
    return

def exit_program(bank):
    return print(f"Thank you for using {bank}!")




def main():
    bank_name = welcome_message()
    user_account = personal_info()
    #print("     *** Name:", user_account["name"], "  Balance:", user_account["balance"], "***")
    main_menu(user_account, bank_name)


if __name__ == "__main__":
    main()

