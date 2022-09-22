class computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def configer(self):
        print("congig is ","CPU {} RAM {}".format(self.cpu,self.ram))
f = 0
while (f != 2):
    f = input("want to create  obj press y if not then 2 ")
    i = input("for cpu :-")
    j = input("for ram:-")
    com1 = computer(i,j )
    #com2 = computer("i9",32)

    com1.configer()
    #com2.configer()



"""class computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def configer(self):
        print("congig is ","CPU {} RAM {}".format(self.cpu,self.ram))


com1 = computer("i5",16 )
com2 = computer("i9",32)

com1.configer()
com2.configer()
"""
"""
class employee:
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary = int(self.salary * 1.5)


harry = employee("harry", "potter",44000)
rohan = employee("rohan", "das",50000 )

harry.increase()
print(harry.salary,rohan.salary)
"""