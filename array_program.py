# array_program.py
# Assessment 3.2: Linear Data Structure - Array (add each letter, then remove until empty)

def main():
    name = input("Enter last name (press Enter for TEVES): ").strip().upper()
    if name == "":
        name = "TEVES"

    # Step 1: empty Array, size = 0
    array = []
    size = 0
    print(f"\nArray: {array} | size = {size}")

    # Step 2: Addition Phase - insert each letter at the next available index (the end)
    print("\n--- ADDITION PHASE ---")
    for letter in name:
        array.append(letter)
        size += 1
        print(f"Inserted '{letter}' at index {size - 1} -> {array} | size = {size}")

    # Step 3: Removal Phase - remove the element at the last index while size > 0
    print("\n--- REMOVAL PHASE ---")
    removed_order = []
    while size > 0:
        removed = array[size - 1]   # element at the last index
        array.pop()                 # remove it
        size -= 1
        removed_order.append(removed)
        print(f"Removed '{removed}' from index {size} -> {array} | size = {size}")

    # Step 4: stop when size = 0
    print(f"\nArray is empty (size = {size}).")
    print("Letters removed in order:", ", ".join(removed_order))


if __name__ == "__main__":
    main()
