class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def isFull(self):
        return (self.front == 0 and self.rear == self.size - 1) or (self.rear + 1) % self.size == self.front

    def isEmpty(self):
        return self.front == -1

    def enQueue(self, value):
        if self.isFull():
            print("Queue is full.")
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
            print("Enqueued:", value)

    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty.")
            return -1
        value = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print("Dequeued:", value)
        return value

    def display(self):
        if self.isEmpty():
            print("Queue is empty.")
        else:
            print("Elements:", end=" ")
            i = self.front
            while i != self.rear:
                print(self.queue[i], end=" ")
                i = (i + 1) % self.size
            print(self.queue[i])

q = CircularQueue(10)
q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
q.enQueue(40)
q.display()
q.deQueue()
q.deQueue()
q.display()
q.enQueue(50)
q.enQueue(60)
q.display()
