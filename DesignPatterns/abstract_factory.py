from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass
from typing import List


# =============================================================================
# INGREDIENT DATA CLASSES
# =============================================================================

@dataclass
class Dough:
    name: str


@dataclass
class Sauce:
    name: str


@dataclass
class Cheese:
    name: str


@dataclass
class Veggies:
    items: List[str]

    def __str__(self):
        return ", ".join(self.items)


@dataclass
class Pepperoni:
    name: str


@dataclass
class Clam:
    name: str


# =============================================================================
# CONCRETE INGREDIENTS - NY STYLE
# =============================================================================

class ThinCrustDough(Dough):
    def __init__(self):
        super().__init__("Thin Crust Dough")


class MarinaraSauce(Sauce):
    def __init__(self):
        super().__init__("Marinara Sauce")


class ReggianoCheese(Cheese):
    def __init__(self):
        super().__init__("Reggiano Cheese")


class NYVeggies(Veggies):
    def __init__(self):
        super().__init__(["Garlic", "Onion", "Mushroom", "Red Pepper"])


class SlicedPepperoni(Pepperoni):
    def __init__(self):
        super().__init__("Sliced Pepperoni")


class FreshClams(Clam):
    def __init__(self):
        super().__init__("Fresh Clams")


# =============================================================================
# CONCRETE INGREDIENTS - CHICAGO STYLE
# =============================================================================

class ThickCrustDough(Dough):
    def __init__(self):
        super().__init__("Thick Crust Dough")


class PlumTomatoSauce(Sauce):
    def __init__(self):
        super().__init__("Plum Tomato Sauce")


class MozzarellaCheese(Cheese):
    def __init__(self):
        super().__init__("Shredded Mozzarella Cheese")


class ChicagoVeggies(Veggies):
    def __init__(self):
        super().__init__(["Black Olives", "Spinach", "Eggplant"])


class SlicedPepperoniChicago(Pepperoni):
    def __init__(self):
        super().__init__("Sliced Pepperoni")


class FrozenClams(Clam):
    def __init__(self):
        super().__init__("Frozen Clams")


# =============================================================================
# ABSTRACT INGREDIENT FACTORY
# =============================================================================

class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self) -> Dough:
        pass

    @abstractmethod
    def create_sauce(self) -> Sauce:
        pass

    @abstractmethod
    def create_cheese(self) -> Cheese:
        pass

    @abstractmethod
    def create_veggies(self) -> Veggies:
        pass

    @abstractmethod
    def create_pepperoni(self) -> Pepperoni:
        pass

    @abstractmethod
    def create_clam(self) -> Clam:
        pass


# =============================================================================
# CONCRETE INGREDIENT FACTORIES
# =============================================================================

class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:
        return ThinCrustDough()

    def create_sauce(self) -> Sauce:
        return MarinaraSauce()

    def create_cheese(self) -> Cheese:
        return ReggianoCheese()

    def create_veggies(self) -> Veggies:
        return NYVeggies()

    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def create_clam(self) -> Clam:
        return FreshClams()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:
        return ThickCrustDough()

    def create_sauce(self) -> Sauce:
        return PlumTomatoSauce()

    def create_cheese(self) -> Cheese:
        return MozzarellaCheese()

    def create_veggies(self) -> Veggies:
        return ChicagoVeggies()

    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoniChicago()

    def create_clam(self) -> Clam:
        return FrozenClams()


# =============================================================================
# PIZZA TYPE ENUM
# =============================================================================

class PizzaType(Enum):
    CHEESE = "cheese"
    PEPPERONI = "pepperoni"
    VEGGIE = "veggie"
    CLAM = "clam"


# =============================================================================
# PIZZA BASE CLASS
# =============================================================================

class Pizza(ABC):
    def __init__(self, name: str):
        self.name = name
        self.dough: Dough = None
        self.sauce: Sauce = None
        self.cheese: Cheese = None
        self.veggies: Veggies = None
        self.pepperoni: Pepperoni = None
        self.clam: Clam = None

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def __str__(self):
        return self.name


# =============================================================================
# CONCRETE PIZZA CLASSES - NY STYLE
# =============================================================================

class NYStyleCheesePizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        super().__init__("NY Style Cheese Pizza")
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        print(f"Tossing {self.dough.name}...")
        print(f"Adding {self.sauce.name}...")
        print(f"Adding {self.cheese.name}...")


class NYStylePepperoniPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        super().__init__("NY Style Pepperoni Pizza")
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.pepperoni = self.ingredient_factory.create_pepperoni()
        print(f"Tossing {self.dough.name}...")
        print(f"Adding {self.sauce.name}...")
        print(f"Adding {self.cheese.name}...")
        print(f"Adding {self.pepperoni.name}...")


class NYStyleVeggiePizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        super().__init__("NY Style Veggie Pizza")
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()
        print(f"Tossing {self.dough.name}...")
        print(f"Adding {self.sauce.name}...")
        print(f"Adding {self.cheese.name}...")
        print(f"Adding veggies: {self.veggies}")


class NYStyleClamPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        super().__init__("NY Style Clam Pizza")
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_clam()
        print(f"Tossing {self.dough.name}...")
        print(f"Adding {self.sauce.name}...")
        print(f"Adding {self.cheese.name}...")
        print(f"Adding {self.clam.name}...")


# =============================================================================
# CONCRETE PIZZA CLASSES - CHICAGO STYLE
# =============================================================================

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        super().__init__("Chicago Style Cheese Pizza")
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        print(f"Tossing {self.dough.name}...")
        print(f"Adding {self.sauce.name}...")
        print(f"Adding {self.cheese.name}...")

    def cut(self):
        print("Cutting the pizza into square slices")


class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        super().__init__("Chicago Style Pepperoni Pizza")
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.pepperoni = self.ingredient_factory.create_pepperoni()
        print(f"Tossing {self.dough.name}...")
        print(f"Adding {self.sauce.name}...")
        print(f"Adding {self.cheese.name}...")
        print(f"Adding {self.pepperoni.name}...")

    def cut(self):
        print("Cutting the pizza into square slices")


class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        super().__init__("Chicago Style Veggie Pizza")
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()
        print(f"Tossing {self.dough.name}...")
        print(f"Adding {self.sauce.name}...")
        print(f"Adding {self.cheese.name}...")
        print(f"Adding veggies: {self.veggies}")

    def cut(self):
        print("Cutting the pizza into square slices")


class ChicagoStyleClamPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        super().__init__("Chicago Style Clam Pizza")
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_clam()
        print(f"Tossing {self.dough.name}...")
        print(f"Adding {self.sauce.name}...")
        print(f"Adding {self.cheese.name}...")
        print(f"Adding {self.clam.name}...")

    def cut(self):
        print("Cutting the pizza into square slices")


# =============================================================================
# ABSTRACT PIZZA STORE
# =============================================================================

class PizzaStore(ABC):
    def order_pizza(self, pizza_type: PizzaType) -> Pizza:
        pizza = self.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type: PizzaType) -> Pizza:
        """Factory Method to create pizza instances based on type"""
        pass


# =============================================================================
# CONCRETE PIZZA STORES
# =============================================================================

class NYPizzaStore(PizzaStore):
    def __init__(self):
        self.ingredient_factory = NYPizzaIngredientFactory()

    def create_pizza(self, pizza_type: PizzaType) -> Pizza:
        if pizza_type == PizzaType.CHEESE:
            return NYStyleCheesePizza(self.ingredient_factory)
        elif pizza_type == PizzaType.PEPPERONI:
            return NYStylePepperoniPizza(self.ingredient_factory)
        elif pizza_type == PizzaType.VEGGIE:
            return NYStyleVeggiePizza(self.ingredient_factory)
        elif pizza_type == PizzaType.CLAM:
            return NYStyleClamPizza(self.ingredient_factory)
        else:
            raise ValueError(f"Unknown pizza type: {pizza_type}")


class ChicagoPizzaStore(PizzaStore):
    def __init__(self):
        self.ingredient_factory = ChicagoPizzaIngredientFactory()

    def create_pizza(self, pizza_type: PizzaType) -> Pizza:
        if pizza_type == PizzaType.CHEESE:
            return ChicagoStyleCheesePizza(self.ingredient_factory)
        elif pizza_type == PizzaType.PEPPERONI:
            return ChicagoStylePepperoniPizza(self.ingredient_factory)
        elif pizza_type == PizzaType.VEGGIE:
            return ChicagoStyleVeggiePizza(self.ingredient_factory)
        elif pizza_type == PizzaType.CLAM:
            return ChicagoStyleClamPizza(self.ingredient_factory)
        else:
            raise ValueError(f"Unknown pizza type: {pizza_type}")


# =============================================================================
# CLIENT CODE
# =============================================================================

if __name__ == "__main__":
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()

    print("--- Ethan ordered a NY Style Cheese Pizza ---")
    pizza = ny_store.order_pizza(PizzaType.CHEESE)
    print(f"Ethan got a {pizza.name}\n")

    print("--- Joel ordered a Chicago Style Cheese Pizza ---")
    pizza = chicago_store.order_pizza(PizzaType.CHEESE)
    print(f"Joel got a {pizza.name}\n")

    print("--- Ethan ordered a NY Style Pepperoni Pizza ---")
    pizza = ny_store.order_pizza(PizzaType.PEPPERONI)
    print(f"Ethan got a {pizza.name}\n")

    print("--- Joel ordered a Chicago Style Veggie Pizza ---")
    pizza = chicago_store.order_pizza(PizzaType.VEGGIE)
    print(f"Joel got a {pizza.name}\n")

    print("--- Ethan ordered a NY Style Clam Pizza ---")
    pizza = ny_store.order_pizza(PizzaType.CLAM)
    print(f"Ethan got a {pizza.name}\n")