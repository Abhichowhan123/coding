class student:
    # protected data member
    _name = None
    _roll =None
    _branch = None

    #constructor
    def __init__(self,name,roll,branch):
        self._name = name
        self._roll =  roll
        self._branch = branch

    def displayRollAndBranch(self):

        #accessing protected data members
        print("Roll : ",self._roll)
        print("branch:",self._branch)

#derived class
class abhi(student):

    #constrctor
    def __init__(self,name,roll,branch):
        student.__init__(self,name ,roll,branch)

    #public member function
    def displayDetails(self):
        #accessing protected data members of super class
        print("Name :",self._name)

        # accessing protected member functions of super class
        self.displayRollAndBranch()

# creating objects of the derived class
obj = abhi("abhishek",1256,"information technology")

# calling public member functions of the class
obj.displayDetails()
