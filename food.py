from abc import ABC, abstractmethod
class MenuItem(ABC):
    @abstractmethod
    def display(self):
        pass
class FoodItem(MenuItem):
    def __init__(self,name,price):
            self.name=name
            self.price=price
    def display(self):
        print(f"{self.name}-${self.price}")
class BeverageItem(MenuItem):
    def __init__(self,name,price):
            self.name=name
            self.price=price
    def display(self):
         print(f"{self.name}-${self.price}")
items=[FoodItem("pizza",250), BeverageItem ("cold coffee",90)]
for item in  items:
     item.display()
           
    
    