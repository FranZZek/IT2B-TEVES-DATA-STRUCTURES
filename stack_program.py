# stack_program.py
# Assessment 3.2: Linear Data Structure - Stack / LIFO (push each letter, then pop until empty)

class Stack:
    def __init__(self):
        # Step 1: empty Stack (LIFO)
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        # Step 2: put the item on top of the Stack
        self.items.append(item)

    def pop(self):
        # Step 3: remove the item at the top of the Stack
        return self.items.pop()

    def display(self):
        # leftmost = bottom, rightmost = top
        return f"{self.items}  (top = {self.items[-1] if self.items else 'none'})"


def main():
    name = input("Enter last name (press Enter for TEVES): ").strip().upper()
    if name == "":
        name = "TEVES"

    stack = Stack()
    print(f"\nStack: {stack.display()}")

    # Addition Phase / Push
    print("\n--- PUSH PHASE ---")
    for letter in name:
        stack.push(letter)
        print(f"Pushed '{letter}' -> {stack.display()}")

    # Removal Phase / Pop
    print("\n--- POP PHASE ---")
    removed_order = []
    while not stack.is_empty():
        removed = stack.pop()
        removed_order.append(removed)
        print(f"Popped '{removed}' -> {stack.display()}")

    # Step 4: stop when the Stack is empty
    print("\nStack is empty.")
    print("Letters removed in order:", ", ".join(removed_order))


if __name__ == "__main__":
    main()
