def get_key_by_value(d, target_value):
    for key, value in d.items():
        if value == target_value:
            return key
    return None  # or raise KeyError if you want strict behavior

image = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\|
                         `'-------'`
                       .-------------.
                      /_______________\|
'''

print(image)
print("WELCOME TO SECRET AUCTION BIDDING GAME: ")

play = input("Do you want to play this game? ").lower()
bidders = dict()
while play == 'yes':
    name = input("What is your name? ")
    bid = int(input("How much you want to bid? $"))
    bidders[name] = bid

    play = input("Are there any else bidders? ")

    print("\n"*20)
maximumB = 0

for key,value in bidders.items():
    if maximumB<value:
        maximumB = value

name = get_key_by_value(bidders,maximumB)

print(f"The winner is {name} with a bid of {maximumB} ")