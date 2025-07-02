from Item import Item

item1 = Item("MyItem",750)

# item1._name = "Other"
# print(item1._name)

#print(item1.readOnly)
# item1.readOnly = "BBB"

# item1.name = "other"
print(item1.name)

#To set a new value for only the read only attribute

item1.name = "Other"
print(item1.name)

#item1.__price = 900
print(item1)

print(item1.price)

item1.apply_increment(0.2)
print(item1.price)

item1.apply_discount()
print(item1.price)