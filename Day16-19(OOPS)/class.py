
#to declare a class
class Item:
    #Class Attributes
    pay_rate = 0.8
    all = []

    def __init__(self,name:str , price:float, quantity=0):
        #Running validation to the received arguments
        assert price>=0, f"Price {price} can not be negative"
        assert quantity>=0, f"Quantity {quantity} can not be negative"

        #Assign to self objects - Instance Attribute
        self.name = name
        self.price = price
        self.quantity = quantity

        #Appending each object to the list to access all the instances of class easily
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price* self.quantity

    def apply_discount(self):
        #On using Item.pay_rate it will always take the pay_rate variable from class level
        # no matter if we have changed the value in instance level
        ##To avoid this happening we use self.pay_rate so that if there is any changes applied
        #at instance level it will first refer to instance level and if not present then class level
        self.price = self.price*self.pay_rate

    def __repr__(self):
        #Used to represent it in a friendly manner which is easy to understand
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone",1000,1)
item2 = Item("Laptop",10000,1)

print(Item.pay_rate)
print(item1.pay_rate) #Since there is no pay_rate variable at instance level so it takes from class level

item1.apply_discount()
print(item1.price)

item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)

print(f"Item - {Item.__dict__}")
print(f"Item1 - {item1.__dict__}")
print(f"Item2 - {item2.__dict__}")

item3 = Item("Cable",10,5)
item4 = Item("Mouse",10,10)
item5 = Item("Keyboard",20,20)
print(Item.all)
for instance in Item.all:
    print(instance.name)


