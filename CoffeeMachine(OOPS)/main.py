from coffee_maker import Coffee_maker
from money_machine import Money_machine
from menu import Menu

coffee = Coffee_maker()
money = Money_machine()
menu = Menu()

working = True
while working:
    choice = input(f"{menu.get_items()} or 'off' to turn off the machine else check 'report':\n")
    if choice=="off":
        working = False
    elif choice == "report":
        coffee.report()
        money.report()
    else:
        drink = menu.find_item(choice)
        if coffee.resource_sufficient(drink):
            if money.money_calculation(drink.cost):
                coffee.make_coffee(drink)