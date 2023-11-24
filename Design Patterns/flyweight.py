# from abc import ABCMeta, abstractmethod

# class IRobot(metaclass=ABCMeta):
#     @abstractmethod
#     def display(self, x:int, y:int):
#         pass

# class HumanoidRobot(IRobot):
#     def __init__(self) -> None:
#         self.type = 'humanoid'
    
#     def display(self, x: int, y: int) -> None:
#         print(f'{self.type} | HUMANOID - {x},{y}')
    
#     def __repr__(self) -> str:
#         return f'{self.type} | HUMANOID'
    
# class DogRobot(IRobot):
#     def __init__(self) -> None:
#         self.type = 'dogrobot'
    
#     def display(self, x: int, y: int) -> None:
#         print(f'{self.type} | DOGGY - {x},{y}')
    
#     def __repr__(self) -> str:
#         return f'{self.type} | DOGGY'

# class RobotFactory(object):
#     _instances = {}

#     def __new__(cls, type: str, sprite: IRobot):
#         self = cls._instances.get(type)
#         if not self:
#             self = cls._instances[type] = object.__new__(RobotFactory)
#             self.sprite = sprite
#             self.type = type
#         return self


# if __name__=="__main__":
#     '''Driver code here'''
#     humanoid1 = RobotFactory('humanoid', HumanoidRobot())
#     humanoid2 = RobotFactory('humanoid', HumanoidRobot())
#     dog1 = RobotFactory('dogrobot', DogRobot())
#     dog2 = RobotFactory('dogrobot', DogRobot())

#     if dog1 != dog2:
#         print("Bawal")
#     else:
#         print("Nooo")
#     if humanoid1.sprite is humanoid2.sprite:
#         print("Correct")
#         humanoid2.sprite.display(10,2)
#         humanoid1.sprite.display(1,2)
#     else:
#         print("Noo")


# More simpler Flyweight Design Pattern
'''
FlyWeight Design Pattern allows to extract part of data which can be shared to reduce memory.
We cache the same object so that we can use it again and again whenever caller needs it, and avoid
creating copy of same object.

'''

class Grade(object):
    _instances = {}

    def __new__(cls, percent) -> 'Grade':
        percent = max(40, min(99, percent))
        letter = 'FEDCBA'[(percent - 40)//10]
        self = cls._instances.get(letter)
        if not self:
            self = cls._instances[letter] = object.__new__(Grade)
            self.letter = letter
        return self

    def __repr__(self) -> str:
        return f'Grade : {self.letter}'


if __name__=="__main__":

    print(Grade(55), Grade(85), Grade(95), Grade(100))
    print(len(Grade._instances))    # number of instances
    print(Grade(95) is Grade(100))  # ask for ‘A’ two more times
    print(len(Grade._instances))    # number stayed the same?