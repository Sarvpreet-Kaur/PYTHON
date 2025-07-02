import csv

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

    @classmethod
    def instantiate_from_csv(cls):
        # with open('items.csv','r') as f:
        #     reader = csv.DictReader(f)
        #     items = list(reader)
        # for item in reader :
        #     print(item) this will give error reader is an iterator which does not store the dictionary
        #     and hence accessing it after the with block gives I/O error as the file is closed
        #     with is a context manager that opens and closes the file safely
        with open('items.csv','r')as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            #print(item)
            Item(
                name = item.get('name'),
                price= float(item.get('price')),
                quantity = int(item.get('quantity'))
            )
    @staticmethod
    def is_integer(num):
        #We will count out the floats that are point zero
        #For i.e. 5.0 or 10.0
        if isinstance(num,float):
            #Counts out the float with decimal 0
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False

    def __repr__(self):
        #Used to represent it in a friendly manner which is easy to understand
        return f"Item('{self.name}', {self.price}, {self.quantity})"


# Item.instantiate_from_csv()
# print(Item.all)
print(Item.is_integer(7.5))
print(Item.is_integer(7.0))

