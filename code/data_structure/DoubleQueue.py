class DoubleQ:
    def __init__(self):
        self.items = []

    def insert_at_front(self,item):
        self.items.insert(0,item)

    def remove_from_front(self):
        return self.items.pop(0)

    def insert_at_back(self,item):
        self.items.append(item)

    def remove_from_back(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def printQ(self):
        print(self.items)

d = DoubleQ()
d.printQ()
d.insert_at_front(1)
d.insert_at_front(2)
d.printQ()
d.insert_at_back(3)
d.insert_at_back(4)
d.printQ()

d.remove_from_front()
d.printQ()
d.remove_from_back()
d.printQ()
d.remove_from_front()
d.printQ()
d.remove_from_back()
d.printQ()

'''
[]
[2, 1]
[2, 1, 3, 4]
[1, 3, 4]
[1, 3]
[3]
[]

'''
