class abhi:
    #constructou
    def __init__(self,name,age):
        self.abhiName= name
        self.abhiAge  = age

    # public member function
    def displayAge(self):
        print("Age :",self.abhiAge)

# creating objectof a class
obj = abhi("abhi",25)

#accessing public data member
print("Name:",obj.abhiName)

#calling public member function of the class
obj.displayAge()