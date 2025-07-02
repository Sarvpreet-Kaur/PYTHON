from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self,owner):
        self.owner = owner

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class FixedDeposit(Account):
    def __init__(self,owner,amount,term):
        super().__init__(owner)
        self.amount = amount
        self.term = term
    def deposit(self, amount):
        self.amount += amount
        print(f"Depositing {amount} in FD")

    def withdraw(self, amount):
        print("Cannot withdraw before maturity.")


p1 = FixedDeposit("Reet",30000,12)
p1.deposit(10000)
p1.withdraw(39)