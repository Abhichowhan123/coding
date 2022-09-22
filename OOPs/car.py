class Car:

    # __init__(self):
    # self is add for the first argument of this method
    # init method serve as a constructor of the class
    # usually it is used to initialization for attribute or some functions
    # this is the first method is called when we create an instance of a class

    # constructor
    def __init__(self):
        print("__init__is called")

"""
# A class have multiple  object

ford = Car()  # ford is a (object || instance)  of a Car
honda = Car()
audi = Car()

# associate data
ford.speed = 200  # speed is a attribute
honda.speed = 220
audi.speed = 250

ford.colour = "red"
honda.colour = "blue"
audi.colour = "black"

print(ford.speed)
print(honda.colour)
"""