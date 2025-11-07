MAX = 100  # Max stack size

def push(stack, top, element):
    if top >= MAX - 1:
        print("Stack Overflow!")
        return top
    top += 1
    stack[top] = element
    return top

def pop(stack, top):
    if top == -1:
        print("Stack Underflow!")
        return None, top
    element = stack[top]
    top -= 1
    return element, top


# ----- Undo/Redo Text Editor -----
undo_stack = [None] * MAX
redo_stack = [None] * MAX
undo_top = -1
redo_top = -1
document = ""

while True:
    print("\n--- Text Editor ---")
    print("1. Make Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        # Save current state in undo stack
        undo_top = push(undo_stack, undo_top, document)
        new_text = input("Enter text to add: ")
        document += new_text
        redo_top = -1  # Clear redo history

    elif choice == "2":
        prev_state, undo_top = pop(undo_stack, undo_top)
        if prev_state is not None:
            redo_top = push(redo_stack, redo_top, document)
            document = prev_state

    elif choice == "3":
        next_state, redo_top = pop(redo_stack, redo_top)
        if next_state is not None:
            undo_top = push(undo_stack, undo_top, document)
            document = next_state

    elif choice == "4":
        print("Current Document State:", document)

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")
