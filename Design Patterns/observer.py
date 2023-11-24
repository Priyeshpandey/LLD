# Observer design pattern

from abc import ABCMeta, abstractmethod
from typing import List, Optional

# Problem statement
# 1. A weather station keeps updating current temp and notifies the observers, TV Display and Mobile Display
class ObserverInterface(metaclass=ABCMeta):
    @abstractmethod
    def update(self, obj: 'WeatherStationInterface'):
        '''Implement update method in concrete Observer class'''

class TVDisplay(ObserverInterface):
    def __init__(self) -> None:
        self.today_temp : int
    
    def update(self, obj: 'WeatherStationInterface'):
        self.today_temp = obj.get_temp()
    
    def display(self):
        print(f'Temperature Today: {self.today_temp}')

class MobileDisplay(ObserverInterface):
    def __init__(self) -> None:
        self.today_temp : int
    
    def update(self, obj: 'WeatherStationInterface'):
        self.today_temp = obj.get_temp()
    
    def display(self):
        print(f'Weather Today: {self.today_temp}')


class WeatherStationInterface(metaclass=ABCMeta):
    @abstractmethod
    def add(self, obj: ObserverInterface):
        '''Implement add method in concrete class'''
    
    @abstractmethod
    def remove(self, obj: ObserverInterface):
        '''Implement remove method in concrete class'''
    
    @abstractmethod
    def notify(self):
        '''Implement notify method in concrete class'''
    
    @abstractmethod
    def set_temp(self, temp: int):
        '''Implement set_temp method in concrete class'''
    
    @abstractmethod
    def get_temp(self):
        '''Implement get_temp method in concrete class'''



class WeatherStationDelhi(WeatherStationInterface):
    def __init__(self) -> None:
        self.observers : List[ObserverInterface] = []
        self.temp: int
    
    def add(self, obj: ObserverInterface):
        self.observers.append(obj)
    
    def remove(self, obj: ObserverInterface):
        self.observers.remove(obj)
    
    def set_temp(self, temp: int):
        self.temp = temp
    
    def notify(self):
        for obj in self.observers:
            obj.update(self)
    
    def get_temp(self):
        return self.temp
    

    
if __name__ == '__main__':
    WTDelhi = WeatherStationDelhi()
    tv = TVDisplay()
    mobile = MobileDisplay()
    WTDelhi.add(tv)
    WTDelhi.add(mobile)
    WTDelhi.set_temp(10)
    WTDelhi.notify()
    tv.display()
    mobile.display()
    WTDelhi.set_temp(100)
    WTDelhi.notify()
    tv.display()
    mobile.display()
