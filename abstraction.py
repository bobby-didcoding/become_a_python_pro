#Using python to manipulate tuples

'''
Abstraction in python is defined as a process of handling complexity by hiding unnecessary information from the user. This is one of the core concepts of object-oriented programming (OOP) languages. That enables the user to implement even more complex logic on top of the provided abstraction without understanding or even thinking about all the hidden background/back-end complexity.

That’s a very generic core topic not only limited to object-oriented programming. You can observe it everywhere in the real world or in our surroundings.

 An abstract method is a method that is declared, but does not contain implementation. An abstract method in a base class identifies the functionality that should be implemented by all its subclasses. However, since the implementation of an abstract method would differ from one subclass to another, often the method body comprises just a pass statement. Every subclass of the base class will ride this method with its implementation. A class containing abstract methods is called abstract class.Python provides the abc module to use the abstraction in the Python program, syntax as:

1
2
from abc import ABC,   
class ClassName(ABC):
'''

#The basics - tuple packing
from abc import ABCMeta, abstractmethod

class Shape:

    __metaclass__ = ABCMeta 

    def __init__ (self, shapeType):

        ”’Objective: To initialize object of class Shape Input Parameters:

        self (implicit parameter) – object of type Shape

        shapeType – string

        Return Value: None

        ”’

        self.shapeType = shape Type

    @abstractmethod 

    def area(self) :

        pass

    @abstractmethod

    def perimeter (self):

        pass

class Rectangle(Shape):

    def __init__(self, length, breadth):

        ”’Objective: To initialize object of class Rectangle Input Parameters: self (implicit parameter) – object of type Rectangle length, breadth – numeric value 

        Return Value: None ”’

        Shape.__init__(self, ‘Rectangle’)

        self.length = length 

        self.breadth = breadth

    def area (self):

        ”’Objective: To compute area of the Rectangle Input Parameter: 

        self (implicit parameter) object of type Rectangle

        Return Value: numeric value

        ”’

        return self.length * self.breadth

    def perimeter (self):

        return 2 * (self.lenght + self.breadth)

class Circle (Shape):

    pi = 3.14

    def __init__ (self, radius):

        ”’Objective: To initialize object of class Circle Input Parameters: self (implicit parameter) – object of type Circle 

            radius – numeric value 

            Return Value: None”’

        Shape.__init__(self, ‘Circle’)

        self.radius = radius

    def area (self):

        ”’Objective: To compute the area of the Circle

        Input Parameter:

        self (implicit parameter) – object of type Circle 

        Return Value: area – numeric value”’

        return round(Circle.pi * (self.radius ** 2), 2)

    def perimeter(self):

        ”’Objective: To compute the perimeter of the Circle

        Input Parameter:

        self (implicit parameter) – object of type Circle

        Return Value: perimeter – numeric value”’

        return round (2 * Circle.pi * self.radius, 2)