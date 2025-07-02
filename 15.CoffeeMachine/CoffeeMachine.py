
coffee_menu = {
    "Espresso": {
        "milk": 0,       # ml
        "water": 30,     # ml
        "coffee": 7,     # g
        "sugar": 0,      # g
        "price": 2.50    # USD
    },
    "Latte": {
        "milk": 150,     # ml
        "water": 30,     # ml
        "coffee": 7,     # g
        "sugar": 5,      # g
        "price": 3.50    # USD
    },
    "Cappuccino": {
        "milk": 120,     # ml
        "water": 30,     # ml
        "coffee": 7,     # g
        "sugar": 3,      # g
        "price": 3.80    # USD
    },
    "Americano": {
        "milk": 0,       # ml
        "water": 120,    # ml
        "coffee": 7,     # g
        "sugar": 2,      # g
        "price": 2.80    # USD
    },
    "Mocha": {
        "milk": 100,     # ml
        "water": 30,     # ml
        "coffee": 7,     # g
        "sugar": 8,      # g
        "price": 4.00    # USD
    }
}
coffee_machine = {
    "Water":500,
    "Milk":500,
    "Coffee":80,
    "Sugar":20,
    "Money":50
}



start = "ON"
while start=="ON":
    coffee = input("What Would you like?(Espresso,Latte,Cappuccino,Americano,Mocha): ")
    if coffee == "report":
        print(f''' 
        Water = {coffee_machine["Water"]} ml
        Milk = {coffee_machine["Milk"]} ml
        Coffee = {coffee_machine["Coffee"]} g
        Sugar = {coffee_machine["Sugar"]} g
        Money = $ {coffee_machine["Money"]}   
        ''')
    else:
        penny = int(input("How much penny you are inserting? ")) #0.01
        nickel = int(input("How much nickel you are inserting? ")) #0.05
        dime = int(input("How much dime you are inserting? ")) #0.10
        half_dollar = int(input("How much half_dollar you are inserting? ")) #0.50

        total = penny*0.01 + nickel*0.05 + dime*0.10 + half_dollar*0.50
        total = round(total,1)
        if total<coffee_menu[coffee]["price"]:
            print("You do not have enough money. Money Refund")
        else:
            returning = total-coffee_menu[coffee]["price"]
            returning = round(returning,2)
            coffee_machine["Water"] -= coffee_menu[coffee]["water"]
            coffee_machine["Milk"] -= coffee_menu[coffee]["milk"]
            coffee_machine["Coffee"] -= coffee_menu[coffee]["coffee"]
            coffee_machine["Sugar"] -= coffee_menu[coffee]["sugar"]
            coffee_machine["Money"] += coffee_menu[coffee]["price"]
            print(f"${returning} is returned. Kindly collect it")
            print(f"Your {coffee} is ready. Enjoyyyy :)")
    start = input("Coffee Machine: ON or OFF: ")

