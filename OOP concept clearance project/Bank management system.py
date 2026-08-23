from abc import ABC, abstractmethod
from datetime import datetime

class Person:

    def __init__(self, uname, age, address):
        self.name = uname
        self.age = age
        self.address = address

    def display(self):
        print("{0}\n{1}\n{2}".format(
            self.name,
            self.age,
            self.address
        ))


class Customer(Person):

    def __init__(self, uname, age, address, customer_id):
        super().__init__(uname, age, address)
        self.customer_id = customer_id


class Account(ABC):

    __total_accounts = 0

    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance
        self.transiction = []

        Account.__total_accounts += 1

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        self.__balance = amount

    def deposit(self, amount):

        if amount <= 0:
            print("\nInvalid amount.")
            return

        self.balance += amount

        self.transiction.append(
            "{0} | Deposit | Rs. {1}".format(
                datetime.now().strftime("%d-%m-%Y %I:%M %p"),
                amount
            )
        )

        print("\nAmount deposited successfully.")
        print("Current Balance : Rs.", self.balance)

    @abstractmethod
    def withdraw(self, amount):
        pass

    @classmethod
    def get_total_accounts(cls):
        return cls.__total_accounts

    @staticmethod
    def validate_account_number(account_number):

        return (
            len(str(account_number)) == 10
            and str(account_number).isdigit()
        )


class SavingsAccount(Account):

    def __init__(
        self,
        account_number,
        account_holder,
        balance,
        interest_rate
    ):
        super().__init__(
            account_number,
            account_holder,
            balance
        )

        self.interest_rate = interest_rate

    def withdraw(self, amount):

        if amount <= 0:
            print("\nInvalid amount.")

        elif self.balance < amount:
            print("\nInsufficient balance.")

        else:
            self.balance -= amount

            self.transiction.append(
                "{0} | Withdraw | Rs. {1}".format(
                    datetime.now().strftime(
                        "%d-%m-%Y %I:%M %p"
                    ),
                    amount
                )
            )

            print("\nAmount withdrawn successfully.")
            print("Current Balance : Rs.", self.balance)

    def add_interest(self):

        interestamount = (
            self.balance * self.interest_rate / 100
        )

        self.balance += interestamount

        self.transiction.append(
            "{0} | Interest | Rs. {1}".format(
                datetime.now().strftime(
                    "%d-%m-%Y %I:%M %p"
                ),
                interestamount
            )
        )

    def account_type(self):
        return "Savings Account"


class CurrentAccount(Account):

    def __init__(
        self,
        account_number,
        account_holder,
        balance,
        overdraft_limit
    ):
        super().__init__(
            account_number,
            account_holder,
            balance
        )

        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):

        if amount <= 0:
            print("\nInvalid amount.")

        elif amount <= self.balance:

            self.balance -= amount

            self.transiction.append(
                "{0} | Withdraw | Rs. {1}".format(
                    datetime.now().strftime(
                        "%d-%m-%Y %I:%M %p"
                    ),
                    amount
                )
            )

            print("\nAmount withdrawn successfully.")
            print("Current Balance : Rs.", self.balance)

        elif amount <= (
            self.balance + self.overdraft_limit
        ):

            extra_amount = amount - self.balance
            self.balance -= amount
            self.overdraft_limit -= extra_amount

            self.transiction.append(
                "{0} | Withdraw | Rs. {1}".format(
                    datetime.now().strftime(
                        "%d-%m-%Y %I:%M %p"
                    ),
                    amount
                )
            )

            print("\nAmount withdrawn successfully.")
            print("Current Balance : Rs.", self.balance)
            print(
                "Remaining Overdraft Limit : Rs.",
                self.overdraft_limit
            )

        else:
            print("\nAmount exceeds overdraft limit.")

    def account_type(self):
        return "Current Account"


class PremiumSavingsAccount(SavingsAccount):

    def __init__(
        self,
        account_number,
        account_holder,
        balance,
        interest_rate
    ):
        super().__init__(
            account_number,
            account_holder,
            balance,
            interest_rate
        )

    def withdraw(self, amount):

        if amount <= 0:
            print("\nInvalid amount.")

        elif self.balance < amount:
            print("\nInsufficient balance.")

        else:
            self.balance -= amount

            self.transiction.append(
                "{0} | Premium Withdraw | Rs. {1}".format(
                    datetime.now().strftime(
                        "%d-%m-%Y %I:%M %p"
                    ),
                    amount
                )
            )

            print("\nAmount withdrawn successfully.")
            print("Current Balance : Rs.", self.balance)

   


class Bank:

    def __init__(self):
        self.customers = []
        self.accounts = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, account_number):

        for account in self.accounts:

            if str(account.account_number) == str(account_number):
                return account

        return None

    def transfer(self, accountself, account_num, amount):

        sender = self.find_account(accountself)
        receiver = self.find_account(account_num)

        if sender is None:
            print("\nSender account not found.")
            return

        if receiver is None:
            print("\nReceiver account not found.")
            return

        if sender == receiver:
            print("\nBoth accounts cannot be the same.")
            return

        if amount <= 0:
            print("\nInvalid amount.")
            return

        if sender.balance < amount:
            print("\nInsufficient balance.")
            return

        sender.balance -= amount
        receiver.balance += amount

        sender.transiction.append(
            "{0} | Transfer to {1} | Rs. {2}".format(
                datetime.now().strftime(
                    "%d-%m-%Y %I:%M %p"
                ),
                receiver.account_number,
                amount
            )
        )

        receiver.transiction.append(
            "{0} | Transfer from {1} | Rs. {2}".format(
                datetime.now().strftime(
                    "%d-%m-%Y %I:%M %p"
                ),
                sender.account_number,
                amount
            )
        )

        print("\nMoney transferred successfully.")
        print("Sender Balance   : Rs.", sender.balance)
        print("Receiver Balance : Rs.", receiver.balance)

    def __len__(self):
        return len(self.customers)

    def count_no_accounts(self):
        print(
            "\nTotal Accounts :",
            Account.get_total_accounts()
        )

    def create_account(self):

        print("\n" + "=" * 55)
        print("                 CREATE NEW ACCOUNT")
        print("=" * 55)

        name = input("Enter customer name    : ")
        age = int(input("Enter customer age     : "))
        address = input("Enter customer address : ")

        customer_id = "CUST" + str(
            len(self.customers) + 1
        )

        customer = Customer(
            name,
            age,
            address,
            customer_id
        )

        account_number = input(
            "Enter 10 digit account number : "
        )

        while True:

            if not Account.validate_account_number(
                account_number
            ):
                print(
                    "Invalid account number. "
                    "Enter exactly 10 digits."
                )

                account_number = input(
                    "Enter account number : "
                )

            elif self.find_account(
                account_number
            ) is not None:

                print("Account number already exists.")

                account_number = input(
                    "Enter another account number : "
                )

            else:
                break

        print("\n1. Savings Account")
        print("2. Current Account")
        print("3. Premium Savings Account")

        choice = input(
            "\nEnter account type : "
        )

        balance = float(
            input("Enter initial balance : Rs. ")
        )

        if balance < 0:
            print("\nBalance cannot be negative.")
            return

        if choice == "1":

            account = SavingsAccount(
                account_number,
                customer,
                balance,
                4
            )

        elif choice == "2":

            account = CurrentAccount(
                account_number,
                customer,
                balance,
                10000
            )

        elif choice == "3":

            account = PremiumSavingsAccount(
                account_number,
                customer,
                balance,
                6
            )

        else:

            print("\nInvalid account type.")
            return

        self.add_customer(customer)
        self.add_account(account)

        print("\n" + "=" * 55)
        print("             ACCOUNT CREATED SUCCESSFULLY")
        print("=" * 55)

        print("Customer ID    :", customer.customer_id)
        print("Customer Name  :", customer.name)
        print("Account Number :", account.account_number)
        print("Account Type   :", account.account_type())
        print("Balance        : Rs.", account.balance)

        print("=" * 55)

    def deposit_money(self):

        print("\n" + "=" * 55)
        print("                    DEPOSIT MONEY")
        print("=" * 55)

        account_number = input(
            "Enter account number : "
        )

        account = self.find_account(account_number)

        if account is None:
            print("\nAccount not found.")
            return

        amount = float(
            input("Enter amount to deposit : Rs. ")
        )

        account.deposit(amount)

    def withdraw_money(self):

        print("\n" + "=" * 55)
        print("                   WITHDRAW MONEY")
        print("=" * 55)

        account_number = input(
            "Enter account number : "
        )

        account = self.find_account(account_number)

        if account is None:
            print("\nAccount not found.")
            return

        amount = float(
            input("Enter amount to withdraw : Rs. ")
        )

        account.withdraw(amount)

    def check_balance(self):

        print("\n" + "=" * 55)
        print("                    CHECK BALANCE")
        print("=" * 55)

        account_number = input(
            "Enter account number : "
        )

        account = self.find_account(account_number)

        if account is None:
            print("\nAccount not found.")
            return

        print("\nCustomer ID    :", account.account_holder.customer_id)
        print("Customer Name  :", account.account_holder.name)
        print("Account Number :", account.account_number)
        print("Account Type   :", account.account_type())
        print("Balance        : Rs.", account.balance)

    def print_statement(self):

        print("\n" + "=" * 65)
        print("                     ACCOUNT STATEMENT")
        print("=" * 65)

        account_number = input(
            "Enter account number : "
        )

        account = self.find_account(account_number)

        if account is None:
            print("\nAccount not found.")
            return

        print("\nCustomer ID    :", account.account_holder.customer_id)
        print("Customer Name  :", account.account_holder.name)
        print("Account Number :", account.account_number)
        print("Account Type   :", account.account_type())

        print("\n" + "-" * 65)
        print("TRANSACTIONS")
        print("-" * 65)

        if len(account.transiction) == 0:

            print("No transactions available.")

        else:

            for transaction in account.transiction:
                print(transaction)

        print("-" * 65)
        print("Current Balance : Rs.", account.balance)
        print("=" * 65)


bank1 = Bank()


while True:

    print("\n" + "=" * 55)
    print("             BANK MANAGEMENT SYSTEM")
    print("=" * 55)

    print("1. Create New Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Check Balance")
    print("6. Print Statement")
    print("7. View Total Accounts (classmethod)")
    print("8. Exit")

    print("=" * 55)

    choice = input("Enter your choice : ")

    if choice == "1":

        bank1.create_account()

    elif choice == "2":

        bank1.deposit_money()

    elif choice == "3":

        bank1.withdraw_money()

    elif choice == "4":

        accountself = input(
            "Enter sender account number   : "
        )

        account_num = input(
            "Enter receiver account number : "
        )

        amount = float(
            input("Enter amount to transfer     : Rs. ")
        )

        bank1.transfer(
            accountself,
            account_num,
            amount
        )

    elif choice == "5":

        bank1.check_balance()

    elif choice == "6":

        bank1.print_statement()

    elif choice == "7":

        bank1.count_no_accounts()

    elif choice == "8":

        print("\nThank you for using Bank Management System.")
        break

    else:

        print("\nInvalid choice. Please try again.")