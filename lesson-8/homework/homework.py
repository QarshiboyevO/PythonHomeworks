from random import randint

accounts = {}
class Account:
    def __init__(self,account_number,name,balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'account number: {self.account_number} name: {self.name} balance: {self.balance}'



class Bank(Account):
    def __init__(self):
        super().__init__(self)

    def openaccounts(self,name,initial_deposit):
        account_number = int(randint(1,100000))
        account=Account(account_number,name,initial_deposit)
        accounts[account_number]=account
        print("Account opened \n account number:",account_number )
        return account

    def viewaccount(self,account_number):
        details=accounts.get(account_number)
        print(details)

    def deposit(self,amount,account_number):
        account=accounts[account_number]
        account.balance=account.balance+amount
        accounts.update({account_number:account})



    def withdraw(self,amount,account_number):
        account=accounts[account_number]
        account.balance=account.balance-amount
        accounts.update({account_number:account})



my_bank=Bank()
my_bank.openaccounts('Orifjon',1000)

print(accounts)


