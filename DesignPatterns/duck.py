# In python a protocol is an informal interface
# that defines a set of methods that a class must implement. 
# It allows for duck typing, where an object can be used as long as it has the required methods, 
# regardless of its actual type

from typing import Protocol

class FlyBehavior(Protocol):
    def fly(self) -> None:
        ...

class QuackBehavior(Protocol):
    def quack(self) -> None:
        ...

class FlyWithWings:
    def fly(self) -> None:
        print("I'm flying with wings!")

class FlyNoWay:
    def fly(self) -> None:
        print("I can't fly.")

class Quack:
    def quack(self) -> None:
        print("Quack!")

class Duck:
    # Delegation of behaviors to strategy objects
    # add two instance variables 
    # that are declared as the interface type
    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior) -> None:
        #Instance Variables hold a reference to a specific behaviour at runtime
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def perform_quack(self) -> None:
        self.quack_behavior.quack()

    def perform_fly(self) -> None:
        self.fly_behavior.fly()

    def set_fly_behavior(self, fly_behavior: FlyBehavior) -> None:
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior: QuackBehavior) -> None:
        self.quack_behavior = quack_behavior

class ModelDuck(Duck):
    def __init__(self) -> None:
        super().__init__(FlyWithWings(), Quack())

if __name__ == "__main__":
    model_duck = ModelDuck()
    model_duck.perform_fly()
    # Change the fly behavior at runtime
    model_duck.set_fly_behavior(FlyNoWay())
    model_duck.perform_fly()
