class Coffee_maker:
    def __init__(self):
        self.resources = {
            "water" : 500,
            "milk" : 250,
            "coffee": 100
        }

    def report(self):
        for item in self.resources:
            print(f" {item}: {self.resources[item]}")

    def resource_sufficient(self,drink):
        for ingredient in drink.ingredients:
            if drink.ingredients[ingredient]>self.resources[ingredient]:
                return False
        return True

    def make_coffee(self,drink):
        for ingredient in drink.ingredients:
            self.resources[ingredient]-=drink.ingredients[ingredient]