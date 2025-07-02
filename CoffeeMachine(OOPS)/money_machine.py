class Money_machine:
    COINS = {
        "half_dollar": 0.50,
        "dollar":1
    }
    def __init__(self):
        self.profit = 0
        self.money_in_machine = 200

    def report(self):
        print(f"Profit: {self.profit}")

    def cost_calculation(self):
        print("Insert amount: ")
        cost = 0
        for item in self.COINS:
            cost += int(input(f"How many {item}"))* self.COINS[item]
        return cost

    def money_calculation(self,amount):
        given = False
        money = self.cost_calculation()
        if money>= amount:
            self.money_in_machine -= (money-amount)
            self.profit += amount
            given = True
            print(f"Money refunded: {(money-amount)}. ENJOY! ")
        else:
            print("Not enough money to purchase the drink")
            given = False
        return given