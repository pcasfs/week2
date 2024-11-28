class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item):
        if self.isFull():
            print("Queue is full!")
        else:
            self.queue[self.rear] = item
            self.rear = (self.rear + 1) % self.size

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty!")
            return None
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return item
