import random

higherLower = '''
            __  ___       __             
           / / / (_)___ _/ /_  ___  _____
          / /_/ / / __ '/ __ \/ _ \/ ___/
         / __  / / /_/ / / / /  __/ /    
        /_/ ///_/\__, /_/ /_/\___/_/     
           / /  /____/_      _____  _____
          / /   / __ \ | /| / / _ \/ ___/
         / /___/ /_/ / |/ |/ /  __/ /    
        /_____/\____/|__/|__/\___/_/
'''
vs = '''
                         _    __    
                        | |  / /____
                        | | / / ___/
                        | |/ (__  ) 
                        |___/____(_)
'''
famous_people = [
    {"rank": 1, "name": "Taylor Swift", "profession": "Musician", "country": "USA"},
    {"rank": 2, "name": "Cristiano Ronaldo", "profession": "Footballer", "country": "Portugal"},
    {"rank": 3, "name": "Lionel Messi", "profession": "Footballer", "country": "Argentina"},
    {"rank": 4, "name": "BTS", "profession": "Music Group", "country": "South Korea"},
    {"rank": 5, "name": "Elon Musk", "profession": "Entrepreneur", "country": "USA"},
    {"rank": 6, "name": "Beyoncé", "profession": "Musician", "country": "USA"},
    {"rank": 7, "name": "The Rock", "profession": "Actor / Wrestler", "country": "USA"},
    {"rank": 8, "name": "Ariana Grande", "profession": "Musician", "country": "USA"},
    {"rank": 9, "name": "Rihanna", "profession": "Musician / Entrepreneur", "country": "Barbados"},
    {"rank": 10, "name": "Selena Gomez", "profession": "Musician / Actress", "country": "USA"},
    {"rank": 11, "name": "Justin Bieber", "profession": "Musician", "country": "Canada"},
    {"rank": 12, "name": "Emma Watson", "profession": "Actress", "country": "UK"},
    {"rank": 13, "name": "Robert Downey Jr.", "profession": "Actor", "country": "USA"},
    {"rank": 14, "name": "Zendaya", "profession": "Actress", "country": "USA"},
    {"rank": 15, "name": "Shah Rukh Khan", "profession": "Actor", "country": "India"},
    {"rank": 16, "name": "Barack Obama", "profession": "Politician", "country": "USA"},
    {"rank": 17, "name": "Ed Sheeran", "profession": "Musician", "country": "UK"},
    {"rank": 18, "name": "Drake", "profession": "Musician", "country": "Canada"},
    {"rank": 19, "name": "Kylie Jenner", "profession": "Influencer / Entrepreneur", "country": "USA"},
    {"rank": 20, "name": "Leonardo DiCaprio", "profession": "Actor", "country": "USA"},
    {"rank": 21, "name": "Angelina Jolie", "profession": "Actress / Humanitarian", "country": "USA"},
    {"rank": 22, "name": "Billie Eilish", "profession": "Musician", "country": "USA"},
    {"rank": 23, "name": "Tom Holland", "profession": "Actor", "country": "UK"},
    {"rank": 24, "name": "Adele", "profession": "Musician", "country": "UK"},
    {"rank": 25, "name": "Emma Stone", "profession": "Actress", "country": "USA"},
    {"rank": 26, "name": "Shakira", "profession": "Musician", "country": "Colombia"},
    {"rank": 27, "name": "Millie Bobby Brown", "profession": "Actress", "country": "UK"},
    {"rank": 28, "name": "Timothée Chalamet", "profession": "Actor", "country": "USA"},
    {"rank": 29, "name": "BLACKPINK", "profession": "Music Group", "country": "South Korea"},
    {"rank": 30, "name": "Virat Kohli", "profession": "Cricketer", "country": "India"},
    {"rank": 31, "name": "LeBron James", "profession": "Basketball Player", "country": "USA"},
    {"rank": 32, "name": "Will Smith", "profession": "Actor / Rapper", "country": "USA"},
    {"rank": 33, "name": "Nicki Minaj", "profession": "Musician", "country": "USA"},
    {"rank": 34, "name": "Tom Hanks", "profession": "Actor", "country": "USA"},
    {"rank": 35, "name": "Dua Lipa", "profession": "Musician", "country": "UK"},
    {"rank": 36, "name": "Gordon Ramsay", "profession": "Chef / TV Host", "country": "UK"},
    {"rank": 37, "name": "Pedro Pascal", "profession": "Actor", "country": "Chile"},
    {"rank": 38, "name": "Jason Momoa", "profession": "Actor", "country": "USA"},
    {"rank": 39, "name": "Miley Cyrus", "profession": "Musician / Actress", "country": "USA"},
    {"rank": 40, "name": "Chris Hemsworth", "profession": "Actor", "country": "Australia"},
    {"rank": 41, "name": "Chris Evans", "profession": "Actor", "country": "USA"},
    {"rank": 42, "name": "Henry Cavill", "profession": "Actor", "country": "UK"},
    {"rank": 43, "name": "Jungkook", "profession": "Singer (BTS)", "country": "South Korea"},
    {"rank": 44, "name": "Neymar Jr.", "profession": "Footballer", "country": "Brazil"},
    {"rank": 45, "name": "Doja Cat", "profession": "Musician", "country": "USA"},
    {"rank": 46, "name": "Bill Gates", "profession": "Entrepreneur / Philanthropist", "country": "USA"},
    {"rank": 47, "name": "Simone Biles", "profession": "Gymnast", "country": "USA"},
    {"rank": 48, "name": "Gigi Hadid", "profession": "Model", "country": "USA"},
    {"rank": 49, "name": "Malala Yousafzai", "profession": "Activist", "country": "Pakistan"},
    {"rank": 50, "name": "Phoebe Bridgers", "profession": "Musician", "country": "USA"}
]

print(higherLower)
A = random.choice(famous_people)
B = random.choice(famous_people)
score = 0
print(f"Your score is {score}")
print("Compare A:"+ A["name"]+ ", "+ A["profession"] +", from " + A["country"])
print(vs)
print("Against B:"+ B["name"]+ ", "+ B["profession"] +", from " + B["country"])
choice = input("Who is more popular? Choose 'A' or 'B': ")
if A["rank"]>B["rank"]:
    ans = "A"
else:
    ans = "B"


while ans == choice:
    print("\n"*20)
    print(higherLower)
    score += 1
    B = random.choice(famous_people)
    while A["rank"] == B["rank"]:
        B = random.choice(famous_people)
    print(f"Your score is {score}")
    print("Compare A:" + A["name"] + ", " + A["profession"] + ", from " + A["country"])
    print(vs)
    print("Against B:" + B["name"] + ", " + B["profession"] + ", from " + B["country"])
    choice = input("Who is more popular? Choose 'A' or 'B': ")
    if B["rank"] > A["rank"]:
        ans = "A"
    else:
        ans = "B"
        A = B

print(f"Sorry you got that wrong. Final Score is {score}")
