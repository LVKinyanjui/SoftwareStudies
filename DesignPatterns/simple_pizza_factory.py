from abc import ABC, abstractmethod
from enum import Enum


# Pizza product interface
class Pizza(ABC):
    def __init__(self, name: str):
        self.name = name

    def prepare(self):
        print(f"Preparing {self.name}")

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def __str__(self):
        return self.name


# Concrete product pizzas
class CheesePizza(Pizza):
    def __init__(self):
        super().__init__("Cheese Pizza")


class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__("Pepperoni Pizza")


class VeggiePizza(Pizza):
    def __init__(self):
        super().__init__("Veggie Pizza")


class ClamPizza(Pizza):
    def __init__(self):
        super().__init__("Clam Pizza")


# Pizza type enum for type safety
class PizzaType(Enum):
    CHESE = "cheese"
    PEPPERONI = "pepperoni"
    VEGGIE = "veggie"
    CLAM = "clam"


# SimplePizzaFactory - encapsulates object creation
class SimplePizzaFactory:
    def create_pizza(self, pizza_type: PizzaType) -> Pizza:
        if pizza_type == PizzaType.CHESE:
            return CheesePizza()
        elif pizza_type == PizzaType.PEPPERONI:
            return PepperoniPizza()
        elif pizza_type == PizzaType.VEGGIE:
            return VeggiePizza()
        elif pizza_type == PizzaType.CLAM:
            return ClamPizza()
        else:
            raise ValueError(f"Unknown pizza type: {pizza_type}")


# PizzaStore - uses factory to create pizzas
class PizzaStore:
    def __init__(self, factory: SimplePizzaFactory):
        self.factory = factory

    def order_pizza(self, pizza_type: PizzaType) -> Pizza:
        pizza = self.factory.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


# Client code
if __name__ == "__main__":
    factory = SimplePizzaFactory()
    store = PizzaStore(factory)

    print("--- Ordering a Cheese Pizza ---")
    pizza = store.order_pizza(PizzaType.CHESE)
    print(f"Got a: {pizza}\n")

    print("--- Ordering a Pepperoni Pizza ---")
    pizza = store.order_pizza(PizzaType.PEPPERONI)
    print(f"Got a: {pizza}\n")

    print("--- Ordering a Veggie Pizza ---")
    pizza = store.order_pizza(PizzaType.VEGGIE)
    print(f"Got a: {pizza}\n")

    print("--- Ordering a Clam Pizza ---")
    pizza = store.order_pizza(PizzaType.CLAM)
    print(f"Got a: {pizza}\n")
