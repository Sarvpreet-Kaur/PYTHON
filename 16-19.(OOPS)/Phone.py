from Item import Item

class Phone(Item):
    def __init__(self,name:str , price:float, quantity=0,broken_phones = 0):
        #Call to super function to access attributes of parent class
        super().__init__(
            name,price,quantity
        )
        #Running validation to the received arguments
        assert broken_phones >= 0, f"Quantity {broken_phones} can not be negative"

        #Assign to self objects - Instance Attribute
        self.broken_phones = broken_phones

        #Appending each object to the list to access all the instances of class easily