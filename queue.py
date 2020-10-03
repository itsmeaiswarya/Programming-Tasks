class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if len(self.items)==0:
            print("Queue is empty.")
        else:
            print("Queue isn't empty.")

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            print("Queue is empty.")
        else:
            return self.items.pop(0)

    def size(self):
        return print(len(self.items))

    def print_queue(self):
        print(self.items)

q = Queue()
q.enqueue("1")
q.enqueue("2")
q.enqueue("3")
q.print_queue()
q.dequeue()
q.print_queue()
q.size()
q.dequeue()
q.dequeue()
q.isEmpty()


