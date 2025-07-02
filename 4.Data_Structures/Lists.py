states = ["Delhi","UP","Punjab","Banglore"]
print(states[0])
print(states)
print(type(states))

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])

print(states[1:])
print(states[1:2])
print(states[-1:])
print(states[:-1])

#List methods
states.append("Kolkata")

states.insert(3,"Gujarat")
print(states)
#deletes from end
popp = states.pop()
print(states)
print(popp)

print(fruits.index("Peaches"))

print(states.sort())
print(states)

vegetables.reverse()
print(vegetables)

vegetables.clear()
print(vegetables)

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[1:])
print(numbers[2:5])
print(numbers[1:5:2])
print(numbers[::3])
print(numbers[::-1])

for index,num in enumerate(numbers):
    print(index,num)

#List Comprehension
#[expression for item in iterable]
sq = [x**2 for x in range(10)]
print(sq)

#[expression for item in iterable if condition]
sq = [x**2 for x in range(10) if x%2==0]
print(sq)

##Nested list comprehension
#[expression for item1 in iterable for item2 in iterable]

ls1 = [1,2,3]
ls2 = ['a','b']
lsFinal = [[i,j] for i in ls1 for j in ls2]
print(lsFinal)

ls3 = [1,2,3]
lsMul = [[i,j] for i in ls1 for j in ls3 if (i*j)%2==0]
print(lsMul)