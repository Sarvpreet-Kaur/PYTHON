class BankAccount:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.__balance = int(balance)

    def deposit(self,amount):
        if amount>0:
            self.__balance += amount
            print(f"{amount} deposited")
        else:
            print(f"Invalid amount: {amount}")

    def withdraw(self,amount):
        if 0<amount<self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print(f"Invalid amount")

    def get_balance(self):
        return self.__balance

class SavingAccount(BankAccount):
    def __init__(self,owner,balance = 0, interest_rate = 0.02):
        super().__init__(owner,balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance()*self.interest_rate
        self.deposit(interest)
        print(f"Interest applied: {interest}")


def create_new_account(name,balance):
    account = SavingAccount(name, balance)
    print("New account created")
    print_account_details(account)
    return account

def print_account_details(account):
    print("Account details: ")
    print(f"Owner: {account.owner}")
    print(f"Balance: {account.get_balance()}")


p2 = create_new_account("Reet",10000000)
p2.deposit(100000000)
p2.apply_interest()