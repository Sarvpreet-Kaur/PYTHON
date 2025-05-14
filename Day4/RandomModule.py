import random
import myModule
from Day4.myModule import favNum

#inclusive
random_integer = random.randint(1,100)
print(random_integer)

#from myModule
print(myModule.favNum)

#for floating point
randomNum0to1 = random.random()
print(randomNum0to1)

randomNum0to1 = random.random()*10
print(randomNum0to1)

randomFloat = random.uniform(1,10)
print(randomFloat)