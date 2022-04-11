from bank_account import BankAccount


class User:
    def __init__(self,data):
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.account = BankAccount({"int_rate" : 0.02, "balance" : 0})
        
        
    def make_deposit(self, amount):
        # self.account_balance += amount
        self.account.deposit(amount)
        return self
        
    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        
        other_user.account.deposit(amount)
        
        print(f"{self.first_name} transferred {amount} to {other_user.first_name} ")
        print(f"{self.first_name} new balance = {self.account.balance}")
        print(f"{other_user.first_name} new blance = {other_user.account.balance}" )
        return self
        
    def make_withdrawl(self,amount):
        self.account.withdrawl(amount)
        return self
jack_data = {
    "first_name" : "Jack",
    "last_name" : "Briscoe",
}
jack = User(jack_data)

bobby_data = {
    "first_name" : "Bobby",
    "last_name" : "Smith",
}
bobby = User(bobby_data)

jack.make_deposit(500)

bobby.make_deposit(200).make_withdrawl(20)

jack.transfer_money(bobby, 300)