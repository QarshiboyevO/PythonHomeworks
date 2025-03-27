from random import randint







class Account:
    def __init__(self,name,balance:float):

        self.name = name
        self.balance = balance

    def __str__(self):
        return f' name: {self.name} balance: {self.balance}'


class Bank:
    def __init__(self):
        self.accounts = {}

    def loaddata(self):
        try:
            with open("accounts.txt" ,'r') as accounts_file:
                for line in accounts_file:
                    account_number,name,balance=line.strip().split(':')
                    self.accounts[int(account_number)]=Account(name,balance)
        except FileNotFoundError:
            print("file not found")

    def savedata(self):

        with open("accounts.txt","w") as accounts_file:
            for account_number,account in self.accounts.items():
                accounts_file.write(f'{account_number}:{account.name}:{account.balance}\n')

    def openaccounts(self,name,initial_deposit):
        self.loaddata()
        account_number = int(randint(10000,99999))
        while account_number in self.accounts:
            account_number = int(randint(10000,99999))
        self.accounts[account_number]=Account(name,initial_deposit)
        self.savedata()
        print("Account opened \n account number:",account_number )
        return account_number

    def viewaccount(self,account_number):
        self.loaddata()
        if account_number not in self.accounts:
            raise Exception(f'account {account_number} not found')
        else:
            details=self.accounts.get(account_number)
            print(str(details))

    def deposit(self,amount:int ,account_number):
        self.loaddata()
        account=self.accounts.get(account_number)
        if account_number not in self.accounts:
            raise Exception(f'account {account_number} not found')
        else:
            if amount>0:
                account.balance=int(account.balance)+amount
            else:
                raise Exception(f'amount {amount} is negative')
        self.savedata()

    def withdraw(self,amount:int ,account_number):
        self.loaddata()
        account=self.accounts.get(account_number)
        if account_number not in self.accounts:
            raise Exception(f'account {account_number} not found')
        else:
            if int(account.balance)<amount:
                print("Insufficient balance")
            else:
                account.balance=int(account.balance)-amount
        self.savedata()



my_bank=Bank()
acc_num=my_bank.openaccounts('Orifjon',1000)
my_bank.viewaccount(acc_num)
my_bank.deposit(1000,acc_num)
my_bank.withdraw(500,acc_num)