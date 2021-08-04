class Debt:
    def __init__(self, initial_balance, initial_interest_rate):
        self.balance = initial_balance
        self.interest_rate = initial_interest_rate

    def print_balance(self):
        print(self.balance)

    def wait_one_year(self):
        self.balance = self.balance * self.interest_rate