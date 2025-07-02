class MenuItem:
    ''' Properties that each menu item will have'''
    def __init__(self,name,cost,water,coffee,milk):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water" : water,
            "coffee": coffee,
            "milk":milk
        }

class Menu:
    '''Initiating menu with all the menu items'''
    def __init__(self):
        self.menu = [
            MenuItem("Latte",10,200,24,150),
            MenuItem("Espresso",20,50,18,0),
            MenuItem("Cappuccino",15,250,24,50)
        ]
    '''To get all the items'''
    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options
    '''Whether that particular drink exist or not'''
    def find_item(self,drink):
        for item in self.menu:
            if drink == item.name:
                return item
            return None
        return None