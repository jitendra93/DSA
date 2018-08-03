
class CQ:

    MAX_SIZE = 4
    front = 0
    back = 0
    count = 0

    def __init__(self):
        self.items = [None] * self.MAX_SIZE

    def enqueue(self,item):
        if self.count == self.MAX_SIZE :
            raise Exception("Overflow")
        else:
            self.items[self.back] = item
            self.back = (self.back + 1 )% self.MAX_SIZE
            self.count = self.count + 1

    def dequeue(self):
        if(self.count == 0):
            raise Exception("Underflow")
        else:
            self.items[self.front] = None
            self.count = self.count  - 1
            self.front = (self.front + 1 )% self.MAX_SIZE

    def printQ(self):
        print ( self.items)

c = CQ()
c.printQ()
c.enqueue(1)
c.printQ()
c.enqueue(2)
c.printQ()
c.enqueue(3)
c.printQ()
c.enqueue(4)
c.printQ()

c.dequeue()
c.printQ()
c.dequeue()
c.printQ()

c.enqueue(5)
c.printQ()
c.enqueue(6)
c.printQ()


'''
[None, None, None, None]
[1, None, None, None]
[1, 2, None, None]
[1, 2, 3, None]
[1, 2, 3, 4]
[None, 2, 3, 4]
[None, None, 3, 4]
[5, None, 3, 4]
[5, 6, 3, 4]
'''
