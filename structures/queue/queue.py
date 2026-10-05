class Queue:
    def __init__(self, limit, queue=[]):
        self.limit = limit
        self.queue = queue

    def is_empty(self):
        return not self.size()

    def is_full(self):
        return self.size() == self.limit

    def enqueue(self, element):
        if not self.is_full():
            self.queue = self.queue + [element]
            return self.queue

    def dequeue(self):
        if not self.is_empty():
            self.queue = self.queue[1:]
            return self.queue

    def show(self):
        print(self.queue)

    def peek(self):
        return self.queue[0]  # Returns the front of the queue (this is the first element)

    def size(self):
        return len(self.queue)


queue = Queue(limit=5)
queue.enqueue(2)
queue.enqueue(5)
queue.show()  # [2, 5]
queue.dequeue()
queue.show()  # [5]
