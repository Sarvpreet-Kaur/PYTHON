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

def create_new_account(name,balance):
    account = BankAccount(name, balance)
    print("New account created")
    print_account_details(account)
    return account

def print_account_details(account):
    print("Account details: ")
    print(f"Owner: {account.owner}")
    print(f"Balance: {account.get_balance()}")

#
# p1 = BankAccount("Reet",1000000)
#
# p1.deposit(3000000)
# print(f"Current balance: {p1.get_balance()}")
#
# p1.withdraw(100000)
# print(f"Current balance: {p1.get_balance()}")
#
# p1.deposit(-3000000)
# print(f"Current balance: {p1.get_balance()}")
#
# p1.withdraw(00000)
# print(f"Current balance: {p1.get_balance()}")

name = input("Enter account holder's name: ")
initial_balance= int(input("Enter initial balance: "))
new = create_new_account(name,initial_balance)
new.deposit(500)
print(print_account_details(new))