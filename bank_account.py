from insufficient_funds_error import InsufficientFundsError

class BankAccount:
    def __init__(self,account_holder,account_number,balance=0):
        self.account_holder=account_holder
        self.account_number=account_number
        self.balance=balance

    def despoint(self,amount):
        if amount>0:
            self.balance += amount
            print(f"{amount} despointed,current balance:{self.balance}")
        else:
            print("despoint amount must be greater than zero")
    
    def withdraw(self,amount):
        if amount > self.balance:
            raise InsufficientFundsError()
        elif amount <= 0:
            print("withdraw amount must be greater than zero.")
        else:
            self.balance -= amount
            print(f"{amount} withdraw current balance:{self.balance}")
    def check_balance(self):
        print(f'current balance:{self.balance}')


    def transform_to(self,another_account,amount):
        if amount > self.balance:
            raise InsufficientFundsError()
        elif amount <= 0:
            print("withdraw amount must be greater than zero.")
        else:
            self.balance -= amount
            another_account += amount
            print(f"{amount}transferred to {another_account.account_holder} account")
            print(f'your current balance:{self.balance}')
            print(f"{another_account.account_holder},s current balance:{another_account.balance}")