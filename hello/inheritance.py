class A:
    def featurel1(self):
        print("featurel 1 working")
    def featurel2(self):
        print("featurel 2 working ")
class B(A) :
    def featurel3(self):
        print("featurel 3 working")
    def featurel4(self):
        print("featurel 4 working")

class C(B):
    def featurel5(self):
        print("featurel 5 working")

s1 = C()
s1.featurel1()

