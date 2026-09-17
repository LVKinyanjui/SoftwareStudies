from abc import ABC, abstractmethod

class Pizza(ABC):
    def __init__(self, name: str, dough: str, sauce: str):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings: list[str] = []

    def prepare(self):
        print(f"Preparing {self.name}")
        print(f"Tossing {self.dough}...")
        print(f"Adding {self.sauce}...")
        if self.toppings:
            print(f"Adding toppings: {', '.join(self.toppings)}")

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")


class NYStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__(
            name="NY Style Sauce and Cheese Pizza",
            dough="Thin Crust Dough",
            sauce="Marinara Sauce"
        )
        self.toppings.append("Grated Reggiano Cheese")


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__(
            name="Chicago Style Deep Dish Cheese Pizza",
            dough="Extra Thick Crust Dough",
            sauce="Plum Tomato Sauce"
        )
        self.toppings.append("Shredded Mozzarella Cheese")

    def cut(self):
        print("Cutting the pizza into square slices")


class PizzaStore(ABC):
    # Factory method
    def order_pizza(self, type: str) -> Pizza:
        pizza = self.create_pizza(type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def create_pizza(self, type: str) -> Pizza:
        """Factory Method to create pizza instances based on type"""
        pass


class NYPizzaStore(PizzaStore):
    def create_pizza(self, type: str) -> Pizza:
        if type == "cheese":
            return NYStyleCheesePizza()
        else:
            raise ValueError(f"Unknown pizza type: {type}")


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, type: str) -> Pizza:
        if type == "cheese":
            return ChicagoStyleCheesePizza()
        else:
            raise ValueError(f"Unknown pizza type: {type}")


if __name__ == "__main__":
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()

    print("--- Ethan ordered a NY Style Cheese Pizza ---")
    pizza = ny_store.order_pizza("cheese")
    print(f"Ethan got a {pizza.name}\n")

    print("--- Joel ordered a Chicago Style Cheese Pizza ---")
    pizza = chicago_store.order_pizza("cheese")
    print(f"Joel got a {pizza.name}\n")

