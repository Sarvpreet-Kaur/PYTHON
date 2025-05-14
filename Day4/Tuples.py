#Creating tuple - immutable but similar to list

tup = ()
print(type(tup))

tup = tuple()
print(type(tup))

numbers = tuple([1,2,3,4,5,6])
print(numbers)
print(type(numbers))

#Accessing tuple elements - using indexes

#Operations on tuples
tuple1 = (1,2,3,4)
tuple2 = ('a','b')
concatenation = tuple1 + tuple2
print(concatenation)

print(concatenation*3)

numbers = (1,1,2,6,7,8,2,10)

#Methods on tuples
print(numbers.count(1))
print(numbers.index(2))

#Packing and unpacking of Tuple
packed = 1,"hii",3.14
print(packed)

a,b,c = packed
print(a)
print(b)
print(c)

#Unpacking using *
numbers = (1,2,3,4,5,6)
first,*middle,last = numbers
print(first,middle,last)
print(type(middle))