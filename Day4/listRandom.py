import random
friends = ["a","b","c","d",
           "e","f","g","h",
           "i","j","k","l",
           "m","n","o","p","q","r","s","t",
           "u","v","w","x","y","z"]

print(random.choice(friends))

print(friends[random.randint(0,len(friends)-1)])