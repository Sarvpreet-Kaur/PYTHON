from Phone import Phone
from Keyboard import Keyboard
item1 = Phone("AB",100,0)
item1.apply_discount()
print(item1.price)

item2 = Keyboard("AB",100,0)
item2.apply_discount()
print(item2.price)