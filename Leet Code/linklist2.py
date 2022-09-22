class link:
    def __init__(self,data):
        self.data = data
        self.next = None
class linklist:
    def __init__(self):
        self.head = None

    def insertLast(self,data):
        newnode = link(data)
        if self.head ==None:
            self.head = newnode
        else:
            temp = self.head
            while temp.next !=None:
                temp = temp.next
            temp.next = newnode
    def viewList(self):
        if self.head ==None:
            print("empty list")
        else:
            temp = self.head
            while temp.next!=None:
                print(temp.data,end=" ")
                temp = temp.next
                if temp.next ==None:
                    print(temp.data, end=" ")
    def deleteLast(self):
        if self.head ==None:
            print("empty list")
        else:
            temp = self.head
            while temp.next.next !=None:
                temp = temp.next
            dele = temp.next
            temp.next  =None
            print(dele.data)

mylist = linklist()
mylist.insertLast(1)
mylist.insertLast(2)
mylist.insertLast(3)
mylist.insertLast(4)
mylist.insertLast(5)
mylist.viewList()
print()
mylist.deleteLast()
mylist.viewList()
print()















