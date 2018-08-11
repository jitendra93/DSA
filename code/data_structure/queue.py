class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def deque(self):
        return self.items.pop(0)

    def show(self):
        print(self.items)


q = Queue()
q.show()
q.enqueue(1)
q.show()
q.enqueue(2)
q.show()
q.enqueue(3)
q.show()

q.deque()
q.show()
q.deque()
q.show()
q.deque()
q.show()

'''
output
[]
[1]
[1, 2]
[1, 2, 3]
[2, 3]
[3]
[]
'''
