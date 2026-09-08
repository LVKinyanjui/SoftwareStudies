from typing import Protocol, runtime_checkable

# Common Interface
@runtime_checkable
class Beverage(Protocol):
    def get_description(self):
        ...
    def cost(self):
        ...
@runtime_checkable
class CondimentDecorator(Protocol):
    def get_description(self):
        ...

# Beverages
class DarkRoast(Beverage):
    def __init__(self):
        self.description = "Dark Roast" # We cam eliminate the redundant instance attribute description
    def get_description(self):
        return self.description # and move that description string here
    def cost(self):
        return .99

class HouseBlend(Beverage):
    def __init__(self):
        self.description = "House Blend"
    def get_description(self):
        return self.description
    def cost(self):
        return .89

class Decaf(Beverage):
    def __init__(self):
        self.description = "dECAF"
    def get_description(self):
        return self.description
    def cost(self):
        return 1.05

class Espresso(Beverage):
    def __init__(self):
        self.description = "Espresso"
    def get_description(self):
        return self.description
    def cost(self):
        return 1.99
        
# Condiments
class Milk(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage


    def cost(self):
        return self.beverage.cost() + .10

    def get_description(self):
        return self.beverage.get_description() + ", Steamed Milk"

class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage


    def cost(self):
        return self.beverage.cost() + .20

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

class Soy(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage


    def cost(self):
        return self.beverage.cost() + .15

    def get_description(self):
        return self.beverage.get_description() + ", Soy"

class Whip(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage


    def cost(self):
        return self.beverage.cost() + .10

    def get_description(self):
        return self.beverage.get_description() + ", Whip"

if __name__ == "__main__": 
    serving = Milk(Soy(DarkRoast()))
    print(serving.get_description())
    print(serving.cost())
    # # Checking types
    # # Should both be True
    # print(isinstance(serving, Beverage))
    # print(isinstance(serving, CondimentDecorator))

