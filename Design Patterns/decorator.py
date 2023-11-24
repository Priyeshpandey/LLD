# Functional approach
# def cheese_topping(func):
#     def wrapper():
#         cost = func()
#         return cost + 10
#     return wrapper

# def mushroom_topping(func):
#     def wrapper():
#         cost = func()
#         return cost + 20
#     return wrapper


# def margherita_cost():
#     return 200

# def vegdelight_cost():
#     return 250

# @mushroom_topping
# @cheese_topping
# def farmhouse_cost():
#     return 300


# def get_pizza_cost(pizza_cost):
#     return pizza_cost()


# if __name__=="__main__":
#     print(get_pizza_cost(farmhouse_cost))

from abc import ABCMeta, abstractmethod

class BasePizza(metaclass=ABCMeta):
    @abstractmethod
    def cost(self) -> int:
        '''Implement cost method'''

class Margherita(BasePizza):
    def cost(self):
        return 100

    def __str__(self) -> str:
        return 'Margherita'

class VegDelight(BasePizza):
    def cost(self):
        return 200
    
    def __str__(self) -> str:
        return 'VegDelight'


class CheeseTopping(BasePizza):
    def __init__(self, pizza: BasePizza) -> None:
        self.pizza: BasePizza = pizza

    def cost(self):
        return self.pizza.cost() + 10
    
    def __str__(self) -> str:
        return 'ChesseTopping'

class MushroomTopping(BasePizza):
    def __init__(self, pizza: BasePizza) -> None:
        self.pizza: BasePizza = pizza

    def cost(self):
        return self.pizza.cost() + 20

    def __str__(self) -> str:
        return 'MushroomTopping'

    

if __name__=='__main__':
    'runner'
    pizzas = [Margherita(), VegDelight()]
    toppings = [MushroomTopping, CheeseTopping]

    for pizza in pizzas:
        for topping in toppings:
            print(f'{pizza}, {topping}, {topping(pizza).cost()}')

