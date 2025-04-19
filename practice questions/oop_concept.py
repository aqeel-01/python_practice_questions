


# program
'''
create a bankAccount class with methods for depositing and withdrawing funds
'''

class BankAccount:
    def __init__(self, balance= 0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited :{amount}. new balance: {self.balance}")
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds...")
        else:
            self.balance -= amount
            print(f"withdraw: {amount}. new balance is {self.balance}")


account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
account.withdraw(150)
        