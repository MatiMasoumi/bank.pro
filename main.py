from bank_account import BankAccount
from insufficient_funds_error import InsufficientFundsError

if __name__=='main':
    account1=BankAccount('ali',12345,5000)
    account2=BankAccount('sara',67890,2000)

    account1.despoint(1000)
    account1.check_balance()
    try:
        account1.withdraw(7000)
    except InsufficientFundsError as e:
        print(e)

    try:
        account1.transform_to(account2,2000)
    except InsufficientFundsError as e:
        print(e)

    account1.check_balance()
    account2.check_balance()