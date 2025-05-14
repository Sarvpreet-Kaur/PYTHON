import copy

empty = {} # or using => empty = dict()
print(type(empty))

student = {"name":"Reet","age":19,"gpa":9.0}
print(student)

#Accessing elements
print(student['gpa'])

print(student.get('address'))
print(student.get('address',0))

#Modifying
student['age'] = 20
student['address'] = 'India'

print(student)

del student['age'] #deletes key-value pair
print(student)

##DICTIONARY METHODS
key = student.keys()
value = student.values()
item = student.items()

print(key)
print(value)
print(item)

#shallow copy

student_copy = student #points to same object just created two references for that object

student["name"] = "Reet2"
print(student)
print(student_copy)

student_copy = student.copy()
student["name"] = "Reet3"
print(student)
print(student_copy)

student_copy= copy.deepcopy(student)
student['age'] = 22
print(student)
print(student_copy)


#Difference between shallow and deep copy
# import copy

# Original student dictionary with a nested list
student = {
    "name": "Reet",
    "age": 20,
    "grades": [85, 90, 95]   # <-- Nested list
}

# Shallow copy
student_copy = student.copy()

# Modify the nested list in the original
student["grades"][0] = 100

print("After modifying student['grades'][0] = 100")
print("student:", student)
print("student_copy (shallow):", student_copy)

# Deep copy
student_copy_deep = copy.deepcopy(student)

# Modify the nested list again
student["grades"][1] = 99

print("\nAfter modifying student['grades'][1] = 99")
print("student:", student)
print("student_copy_deep:", student_copy_deep)


##ITERAYING
#over keys
for key in student.keys():
    print(key)
#over values
for val in student.values():
    print(val)
#over key-value pair
for key,val in student.items():
    print(f"{key}: {val}")

#NESTED DICTIONARIES
student = {
    "student1": {"name":"Ree","age":19},
    "student2": {"name":"Reee","age":119}
}
print(student)

#Accessing
print(student["student2"]["age"])

#Iterating
for stId, stInfo in student.items():
    print(f"{stId} : {stInfo}")
    for key,val in stInfo.items():
        print(f"{key} : {val}")


#Dictionary Comprehension
sq = {x:x**2 for x in range(10)}
print(sq)

sq = {x:x**2 for x in range(10) if x%2==0}
print(sq)
sq = {x: {y** 2: y ** 3 for y in range(10)} for x in range (10) if x%2==0}
print(sq)

##Practical Examples
#1. Use a dictionary to count frequency of numbers
numbers = [1,2,3,2,1,1,2,3,4,2,1,5,2,3,4,4,2,1,2,2,3,4]
freq = dict()
for n in numbers:
    if n in freq.keys():
        freq[n] = freq[n]+1
    else:
        freq[n] = 1
print(freq)

#2. Merging 2 dictionaries
dict1 = {'a':1,'b':2}
dict2 = {'c':3,'d':4}
merged = {**dict1, **dict2} #Using keyword arguments
print(merged)