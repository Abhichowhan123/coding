class student:
    def __init__(self,name ,rollno):
        self.name = name
        self.rollno = rollno
        self.lab = self.laptop()


    def show(self):
        print(self.name,self.rollno)
        self.lab.show()

    class laptop:
        def __init__(self):
            self.brand = "HP"
            self.CPU = "i5"
            self.RAM = 8

        def show(self):
            print(self.brand,self.CPU,self.RAM)



s1 = student("abhi",8)
s2 = student("avik",4)

s1.show()