#Using python to manipulate tuples

'''
Magic methods in Python are the special methods that start and end with the double underscores. They are also called dunder methods. Magic methods are not meant to be invoked directly by you, but the invocation happens internally from the class on a certain action. For example, when you add two numbers using the + operator, internally, the __add__() method will be called.

Built-in classes in Python define many magic methods. Use the dir() function to see the number of magic methods inherited by a class. For example, the following lists all the attributes and methods defined in the int class.
'''

#The basics - tuple packing
t = 12345, 54321, 'hello!'
t[0]
t

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u

# Tuples are immutable:
t[0] = 88888

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v

#Indexing
'''
 +---+---+---+---+---+---+---+---+---+
 | D | i | d | C | o | d | i | n | g |
 +---+---+---+---+---+---+---+---+---+
 0   1   2   3   4   5   6   7   8   
-9  -8  -7  -6  -5  -4  -3  -2  -1
'''

t[0]  # indexing returns the item
t[-1]

#trailing comma
empty = ()
singleton = 'hello',
len(empty)
len(singleton)
singleton

#Unpacking a tuple
x, y, z = t
x
y
z

#built-in function tuple()
x = tuple(['bobby', 'at', 'didcoding','dot', 'com']) # creates a tuple object
x

#Tuple comprehension...Just use list comprehension with the tuple function
tuple([x**2 for x in range(10)])