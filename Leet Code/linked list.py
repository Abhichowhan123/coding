class link:
    def __init__(self,data):
        self.data  =  data    # Assign data
        self.next  =None      # Initialize
                              # next as null
class linkedlist:
    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None
    def insertLast(self,value):
        newNode = link(value)
        if self.head ==None:
            self.head=newNode
        else:
            temp = self.head
            while temp.next!=None:
                temp = temp.next
            temp.next = newNode
    def deleteFirst(self):
        if self.head ==None:
            print("linked list is empty")
        else:
            temp = self.head
            self.head = self.head.next
    def viewList(self):
        if self.head ==None:
            print("List is empty" )
        else:
            temp = self.head
            while temp !=None:
                print(temp.data,end= " ")
                temp = temp.next

mylist = linkedlist()
mylist.insertLast(1)
mylist.insertLast(2)
mylist.insertLast(3)
mylist.insertLast(4)
mylist.insertLast(5)
mylist.viewList()
print()
mylist.deleteFirst()
mylist.viewList()
print()
mylist.deleteFirst()
mylist.viewList()