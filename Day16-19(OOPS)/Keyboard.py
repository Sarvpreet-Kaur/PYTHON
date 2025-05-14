from Item import Item

class Keyboard(Item):
    pay_rate = 0.7
    def __init__(self,name:str , price:float, quantity=0):
        #Call to super function to access attributes of parent class
        super().__init__(
            name,price,quantity
        )
        #Appending each object to the list to access all the instances of class easily