print("Welcome to the Tip Calculator!!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
split = int(input("How many people to split the bill? "))
payment = (bill + (bill*(tip/100)))/split
print(f"Each person should pay: ${round(payment,2)}")