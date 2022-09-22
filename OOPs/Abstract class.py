from abc import ABC,abstractmethod # first import abstract class and abstractmethod

class father(ABC):
    @abstractmethod
    def disp(self):
        pass

    def show(self):
        print("concrete method")

"""obj = father()"""        #can't make object of the class becouse of abstract class
                            # so we have to make chile of this class using inheritance
class child(father):
    def disp(self):
        print("child of father class")

obj  = child()
obj.disp()
obj.show()

