class Queue:
    def __init__(self, max_size=5):
        self.max_size = max_size  # Maximum size of the queue
        self.queue = []  # The queue will be stored in this list

    def enqueue(self, char):
        """Add a character to the queue."""
        if len(self.queue) < self.max_size:
            self.queue.append(char)
            print(f"Character '{char}' enqueued.")
        else:
            print("Queue is full. Cannot enqueue more characters.")

    def display(self):
        """Display the current state of the queue."""
        if self.queue:
            print("Current queue:", self.queue)
        else:
            print("Queue is empty.")

queue = Queue()  # Initialize the queue with default max size of 5

# Enqueue characters
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
queue.enqueue('D')
queue.enqueue('E')

# Try to enqueue a sixth character (should fail)
queue.enqueue('F')

# Display the queue
queue.display()
