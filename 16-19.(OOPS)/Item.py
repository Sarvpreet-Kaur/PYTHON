import csv
class Item:
    #Class Attributes
    pay_rate = 0.8
    all = []

    def __init__(self,name:str , price:float, quantity=0):
        #Running validation to the received arguments
        assert price>=0, f"Price {price} can not be negative"
        assert quantity>=0, f"Quantity {quantity} can not be negative"

        #Assign to self objects - Instance Attribute
        # self._name = name
        self.__name = name
        self.__price = price
        self.quantity = quantity

        #Appending each object to the list to access all the instances of class easily
        Item.all.append(self)
    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        #On using Item.pay_rate it will always take the pay_rate variable from class level
        # no matter if we have changed the value in instance level
        ##To avoid this happening we use self.pay_rate so that if there is any changes applied
        #at instance level it will first refer to instance level and if not present then class level
        self.__price = self.__price * self.pay_rate


    def apply_increment(self,increment_value):
        self.__price = self.__price + self.__price*increment_value

    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        #return self.name
        #return self._name
        return self.__name
    #name is the function name
    @name.setter
    def name(self,value):
        if len(value)>10:
            raise Exception("The name is too long")
        else:
            self.__name = value
        #self.__name = value

    def calculate_total_price(self):
        return self.__price* self.quantity



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
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

    # @property
    # def readOnly(self):
    #     return "AAAAA"
    def __connect(self,server):
        pass
    def __body(self):
        return f"""
                Hello
                This is an email. """

    def __send(self):
        pass

    def send_email(self):
        self.__connect("")
        self.__body()
        self.__send()