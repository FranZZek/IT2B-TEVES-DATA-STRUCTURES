# queue_program.py
# Assessment 3.2: Linear Data Structure - Queue / FIFO (enqueue each letter, then dequeue until empty)

class Queue:
    def __init__(self):
        # Step 1: empty Queue (FIFO)
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        # Step 2: add the item to the rear of the Queue
        self.items.append(item)

    def dequeue(self):
        # Step 3: remove the item at the front of the Queue
        return self.items.pop(0)

    def display(self):
        # leftmost = front, rightmost = rear
        if self.is_empty():
            return "[]  (front = none, rear = none)"
        return f"{self.items}  (front = {self.items[0]}, rear = {self.items[-1]})"


def main():
    name = input("Enter last name (press Enter for TEVES): ").strip().upper()
    if name == "":
        name = "TEVES"

    queue = Queue()
    print(f"\nQueue: {queue.display()}")

    # Addition Phase / Enqueue
    print("\n--- ENQUEUE PHASE ---")
    for letter in name:
        queue.enqueue(letter)
        print(f"Enqueued '{letter}' -> {queue.display()}")

    # Removal Phase / Dequeue
    print("\n--- DEQUEUE PHASE ---")
    removed_order = []
    while not queue.is_empty():
        removed = queue.dequeue()
        removed_order.append(removed)
        print(f"Dequeued '{removed}' -> {queue.display()}")

    # Step 4: stop when the Queue is empty
    print("\nQueue is empty.")
    print("Letters removed in order:", ", ".join(removed_order))


if __name__ == "__main__":
    main()
