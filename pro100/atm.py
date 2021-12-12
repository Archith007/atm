class bank():
    def __init__(self,balance):
        self.balance = balance

    def cash_withdrawal(self,balance):
        cash = int(input("How Much Cash Do You Want To Withdraw"))
        self.balance = self.balance - cash
        print("You have $",self.balance)


Archith = bank(50000)

Archith.cash_withdrawal(50000)


