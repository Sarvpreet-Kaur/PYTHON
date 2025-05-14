from os import remove

sets = {1,2,3,4,5}
print(sets)
print(type(sets))

empty = set()

##Set operations
#Adding
sets.add(6)
print(sets)

#Remove
sets.remove(3)
print(sets)

#discard - does not raise the exception like remove() does
sets.discard(100)
print(sets)

#pops the first element and returns it
rem = sets.pop()
print(sets,rem)

#clears all values
sets.clear()
print(sets)

##Membership Tests
sets = {1,2,4,6,8,9,10}
print(3 in sets)
print(10 in sets)

##SET OPERATIONS - MATHEMATICAL
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

#1. Union
uni = set1.union(set2)
print(uni)

#2. Intersection
inter = set1.intersection(set2)
print(inter)

#3. Intersection update - update the set1 with the result of intersection
set1.intersection_update(set2)
print(set1)

#4. Difference
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
diff = set1.difference(set2)
print(diff)

#5. Difference_update
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
set1.difference_update(set2)
print(set1)

#6 Symmetric difference
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
diff = set1.symmetric_difference(set2)
print(diff)

##SET METHODS
#1. issubset
set1 = {1,2,3,4,5,6,7}
set2 = {3,4,5,6,7}
print(set1.issubset(set2))

#2. issuperset
print(set1.issuperset(set2))

##Counting unique words in a text
text = "We are studying sets. Sets are used for membership tests"
words = text.split()
print(words)

unique = set(words)
print(unique)
print(len(unique))