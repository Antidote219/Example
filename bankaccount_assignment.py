class User:
    bank_name = "Dojo Credit Union"
    all_users = []
    def __init__(self, data):
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.int_rate = 0.02
        self.account_balance = data["account_balance"]
        User.all_users.append(self)
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"My name is {self.first_name} and my Account Balance is {self.account_balance}")
        return self
        
    def yield_interest(self):
        self.account_balance = self.account_balance + (self.account_balance * self.int_rate)
        return self
    
    # @classmethod
    # def bank_info(cls):
    #     for user in cls.all_users:
    #         return (cls.all_users)
        


jack_data = {
    "first_name" : "Jack",
    "last_name" : "Briscoe",
    "account_balance" : 0,
}
jack = User(jack_data)
bobby_data = {
    "first_name" : "Bobby",
    "last_name" : "Smith",
    "account_balance" : 0,
}
bobby = User(bobby_data)

jim_data = {
    "first_name" : "Jim",
    "last_name" : "Jones",
    "account_balance" : 0,
}
jim = User(jim_data)


# print(User.all_users)
jack.make_deposit(100).make_deposit(50).make_deposit(50).make_withdrawl(50).yield_interest().display_user_balance()
bobby.make_deposit(1000).make_deposit(375).make_withdrawl(225).make_withdrawl(50).make_withdrawl(25).make_withdrawl(50).yield_interest().display_user_balance()
# print(User.bank_info())

# print(jack.account_balance)
# jack.display_user_balance()
# jim.make_deposit(3000).make_withdrawl(500).make_withdrawl(250).make_withdrawl(1000)
# jack.yield_interest()
# jack.display_user_balance()
# bobby.yield_interest()
# bobby.display_user_balance()
# jim.yield_interest()
# jim.display_user_balance()
# # jim.transfer_money(100)