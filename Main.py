from abc import ABC , abstractmethod
class fruit(ABC):
    def display(self):
        print("Inside display fruit")
    @abstractmethod
    def display2(self):
        print("Inside display 2 fruit")
class colour(fruit):
    def display2(self):
        print("Inside display2 colour")
    def displaynumber(self,number):
        print(f"the number is {number}")
a = colour()
a.display2()
a.displaynumber(10)
a.display()