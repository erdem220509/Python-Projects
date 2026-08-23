import sys

class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        else:
            self.balance += amount
            print(f"Deposited succesfully! Your new balance is {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid input!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn successfully! Your new balance is {self.balance}")

    def display_info(self):
        print(f"Account {self.account_number}")
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, owner, account_number, interest_rate, balance=0):
        super().__init__(owner, account_number, balance)
        self.interest_rate = interest_rate  

    def apply_interest(self):
        change = self.balance * self.interest_rate
        self.balance += change
        print(f"Interest applied! New balance: ${self.balance:.2f}")

class CheckingAccount(BankAccount):
    def __init__(self, owner, account_number, overdraft_limit, balance = 0):
        super().__init__(owner, account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid input!")
        elif amount > self.overdraft_limit + self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn successfully! Your new balance is {self.balance}")

accounts = []


def create_account():

    while True:
        owner = input("Owner name: ")

        if len(owner.strip()) > 0:
            break
        else:
            print("Name can't be empty!")

    print("""Account type:
1. Savings
2. Checking""")

    while True:
        try:
            accounttype = int(input("Choose: "))

            if accounttype in (1, 2):
                break
            else:
                print("You can only enter 1 or 2!")

        except ValueError:
            print("You should enter a number!")

    while True:
        try:
            startingbalance = float(input("Starting balance: "))

            if startingbalance >= 0:
                break
            else:
                print("Starting balance cannot be negative!")

        except ValueError:
            print("Balance should be a number!")

    accountnumber = 1001 + len(accounts)

    if accounttype == 1:

        while True:
            try:
                interest_rate = float(input("Interest Rate: "))

                if interest_rate >= 0:
                    break
                else:
                    print("Interest rate cannot be negative!")

            except ValueError:
                print("Interest rate should be a number!")

        accounts.append(
            SavingsAccount(
                owner,
                accountnumber,
                interest_rate,
                startingbalance
            )
        )

    elif accounttype == 2:

        while True:
            try:
                overdraft_limit = float(input("Overdraft Limit: "))

                if overdraft_limit >= 0:
                    break
                else:
                    print("Overdraft limit cannot be negative!")

            except ValueError:
                print("Overdraft limit should be a number!")

        accounts.append(
            CheckingAccount(
                owner,
                accountnumber,
                overdraft_limit,
                startingbalance
            )
        )

    print("Account created successfully!")
    print(f"Account number is {accountnumber}")

def view_accounts():

    if len(accounts) == 0:
        print("There are no accounts!")
        return

    if len(accounts) == 1:
        print("=== ACCOUNT ===")
        accounts[0].display_info()

    print("=== ACCOUNTS ===")
    for element in accounts:
        element.display_info()

def find_account(account_number):
    for element in accounts:
        if element.account_number == account_number:
            return element
        else:
            print("Account not found!")
    return None

def deposit_to_account():
    while True:
        try:
            account_number = int(input("What is your account number: "))
            account = find_account(account_number)

            if account is None:
                print("There is no such account!")
                continue

            break

        except ValueError:
            print("Account number should be a number!")

    while True:
        try:
            amount = float(input("How much do you want to deposit: "))
            break

        except ValueError:
            print("Deposit amount should be a number!")

    account.deposit(amount)


def withdraw_from_account():
    while True:
        try:
            account_number = int(input("What is your account number: "))
            account = find_account(account_number)

            if account is None:
                print("There is no such account!")
                continue

            break

        except ValueError:
            print("Account number should be a number!")

    while True:
        try:
            amount = float(input("How much do you want to withdraw: "))
            break

        except ValueError:
            print("Withdrawal amount should be a number!")

    account.withdraw(amount)

def apply_interest_to_account():
    while True:
        try:
            account_number = int(input("What is your account number: "))
            account = find_account(account_number)

            if account is None:
                print("There is no such account!")
                continue

            break

        except ValueError:
            print("Account number should be a number!")

    if isinstance(account, SavingsAccount):
        account.apply_interest()
    else:
        print("Interest can only be applied to savings accounts!")

def interface():
    print("""
=== BANKING SYSTEM ===

1. Create Account
2. View Accounts
3. Deposit
4. Withdraw
5. Apply Interest
6. Exit
""")

    while True:
        try:
            user_answer = int(input("Choose: "))

            if 1 <= user_answer <= 6:
                break

            print("Enter a number between 1 and 6!")

        except ValueError:
            print("You should enter a number!")

    if user_answer == 1:
        create_account()

    elif user_answer == 2:
        view_accounts()

    elif user_answer == 3:
        deposit_to_account()

    elif user_answer == 4:
        withdraw_from_account()

    elif user_answer == 5:
        apply_interest_to_account()

    elif user_answer == 6:
        print("Exiting banking system...")
        sys.exit()


while True:
    interface()

        