class BankAccount:
    def __init__(self, account_no, holder_name, balance):
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = balance


class SavingsAccount(BankAccount):
    def __init__(self, account_no, holder_name, balance, interest_rate):
        super().__init__(account_no, holder_name, balance)
        self.interest_rate = interest_rate

    def display(self):
        interest = self.balance * self.interest_rate / 100

        print("Account No:", self.account_no)
        print("Holder Name:", self.holder_name)
        print("Balance:", self.balance)
        print("Interest Rate:", str(self.interest_rate) + "%")
        print("Interest:", interest)


account = SavingsAccount(1001, "Rahul", 50000, 5)
account.display()
