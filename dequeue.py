class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Add item to the end of the queue."""
        if len(self.queue) < 5:  # Limiting queue size to 5
            self.queue.append(item)
        else:
            print("Queue is full!")

    def dequeue(self):
        """Remove the item from the front of the queue."""
        if not self.is_empty():
            removed_item = self.queue.pop(0)  # Remove the first item
            return removed_item
        else:
            print("Queue is empty!")
            return None

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0


# example
queue = Queue()

# Enqueue some items to the queue
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

# Dequeue an item
dequeued_item = queue.dequeue()
if dequeued_item is not None:
    print(f"Dequeued item: {dequeued_item}")
