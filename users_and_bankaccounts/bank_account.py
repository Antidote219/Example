class BankAccount:
    def __init__(self,data):
        self.int_rate = data ["int_rate"]
        self.balance = data["balance"]
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdrawl(self,amount):
        self.balance -= amount