# linked_list_program.py
# Assessment 3.2: Linear Data Structure - Linked List (add each letter, then remove until empty)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # Step 1: empty Linked List -> Head = null, Tail = null
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add_last(self, data):
        # Step 2: create a new node, then link it after Tail
        new_node = Node(data)
        if self.head is None:          # list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # link after Tail
            self.tail = new_node       # move Tail to the new node

    def remove_first(self):
        # Step 3: remove the node at Head by moving Head to the next node
        removed = self.head.data
        self.head = self.head.next
        if self.head is None:          # list became empty
            self.tail = None
        return removed

    def display(self):
        parts = []
        current = self.head
        while current is not None:
            parts.append(current.data)
            current = current.next
        parts.append("null")
        return " -> ".join(parts)


def main():
    name = input("Enter last name (press Enter for TEVES): ").strip().upper()
    if name == "":
        name = "TEVES"

    linked_list = LinkedList()
    print(f"\nLinked List: {linked_list.display()}")

    # Addition Phase
    print("\n--- ADDITION PHASE ---")
    for letter in name:
        linked_list.add_last(letter)
        print(f"Added '{letter}' -> {linked_list.display()}")

    # Removal Phase
    print("\n--- REMOVAL PHASE ---")
    removed_order = []
    while not linked_list.is_empty():
        removed = linked_list.remove_first()
        removed_order.append(removed)
        print(f"Removed '{removed}' -> {linked_list.display()}")

    # Step 4: stop when all nodes are deleted
    print("\nLinked List is empty (Head = null, Tail = null).")
    print("Letters removed in order:", ", ".join(removed_order))


if __name__ == "__main__":
    main()
