class CircularQueue():
    def __init__(self):
        """class to hold the positions for insertion & deletion"""
        self.start_ptr = 0
        self.end_ptr = -1
        self.cq_list = []

    def enqueue(self, value):
        """storing the elements in circular queue"""
        if len(self.cq_list) > 5:
            print("Circular Queue is full")
            return
        """checking for empty block in array & storing elements & resetting end pointer"""
        if 'None' in self.cq_list:
            self.cq_list[self.end_ptr] = value
            self.end_ptr+=1
        else:
            self.cq_list.append(value)
            self.end_ptr+=1

    def dequeue(self):
        """removing element in fifo order & resetting start end pointer"""
        self.cq_list=[str(sub).replace(str(self.cq_list[self.start_ptr]),'None') for sub in self.cq_list]
        self.start_ptr+=1
        for i,j in enumerate(self.cq_list):
            if j=='None':
                self.end_ptr=i
                break
        """for printing queue"""
    def print_cq(self):
        if len(self.cq_list) > 5:
            print("circular queue is full")
            return
        print(self.cq_list, self.start_ptr, self.end_ptr)

cq=CircularQueue()
cq.enqueue(0)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.print_cq()
cq.dequeue()
cq.dequeue()
cq.print_cq()
cq.enqueue(7)
cq.enqueue(9)
cq.print_cq()



