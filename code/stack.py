#Learn more at stack @ https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/tutorial/

class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == [] # or len(self.items == 0)

    def peek(self):
        if self.isEmpty():
            raise "Error peeking at empty stack"
        return self.items[self.size() - 1]

    def size(self):
        return len(self.items)


s = Stack()

print("Initializing stack")
print(s.isEmpty()) # True

s.push('L') #L
s.push('e') #Le
s.push('v') #Lev
s.push('e') #Leve
s.push('l') #Level
print(s.peek())
print(s.size())
print(s.isEmpty())

print(s.pop()) #Leve
print(s.pop()) #Lev
print(s.pop()) #Le
print(s.pop()) #L
print(s.pop()) #[]

print(s.size())
