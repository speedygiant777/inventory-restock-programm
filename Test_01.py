.

class inventoryStock:
    def __init__(self, name, quantity, reorder_level):
        self.name = name
        self.quantity = quantity
        self.reorder_level = reorder_level

item1 = inventoryStock("Kinder Chocolate", 10, 20)
item2 = inventoryStock("Potato Chips", 11, 15)

items = [item1, item2]


for x in items:
    if x.quantity < x.reorder_level:
        print(f"{x.name} needs to be restocked. {x.name} needs {x.reorder_level} items restocked")
