class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def front(self):
        if not self.is_empty():
            return self.queue[0]

    def is_empty(self):
        if self.queue:
            return False
        return True

    def size(self):
        return len(self.queue)

    def __str__(self):
        import json

        return json.dumps(self.queue)


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue.dequeue())
    print(queue)
