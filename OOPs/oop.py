class Item:
    def calculate_total_price(self,x,y):   # Method
        return x * y

    pass

item1 = Item()
item1.price = 100
item1.quantity = 5


item2 = Item()
item2.price = 500
item2.quantity = 5

print(item1.calculate_total_price(item1.price,item1.quantity))
print(item2.calculate_total_price(item2.price,item2.quantity))
