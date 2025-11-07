
# Node class 
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Insert a node 
def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

# Search a node 
def search(node, key):
    if node is None or node.key == key:
        return node
    if key < node.key:
        return search(node.left, key)
    else:
        return search(node.right, key)

# Inorder traversal 
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)

# Preorder traversal 
def preorder(root):
    if root is not None:
        print(root.key, end=' ')
        preorder(root.left)
        preorder(root.right)

# Postorder traversal 
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=' ')

# Find minimum value node 
def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# Delete a node 
def deleteNode(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root

# Start interactive BST operations 
root = None

while True:
    print("\n--- Binary Search Tree Menu ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        val = int(input("Enter value to insert: "))
        root = insert(root, val)
        print(f"{val} inserted.")

    elif choice == '2':
        val = int(input("Enter value to delete: "))
        root = deleteNode(root, val)
        print(f"{val} deleted (if it existed).")

    elif choice == '3':
        val = int(input("Enter value to search: "))
        result = search(root, val)
        if result:
            print(f"{val} found in the BST.")
        else:
            print(f"{val} not found in the BST.")

    elif choice == '4':
        print("\nDisplay Options:")
        print("1. Inorder Traversal")
        print("2. Preorder Traversal")
        print("3. Postorder Traversal")

        display_choice = input("Enter your choice (1-3): ")

        if display_choice == '1':
            print("Inorder traversal: ", end='')
            inorder(root)
            print()

        elif display_choice == '2':
            print("Preorder traversal: ", end='')
            preorder(root)
            print()

        elif display_choice == '3':
            print("Postorder traversal: ", end='')
            postorder(root)
            print()

        else:
            print("Invalid display choice.")

    elif choice == '5':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter 1-5.")
