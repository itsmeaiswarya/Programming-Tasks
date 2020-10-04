class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.size() == 0

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            print("Stack is empty.")
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)

    def show(self):
        return self.items

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.show())
