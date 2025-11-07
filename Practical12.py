# Node class to represent each city in the Binary Search Tree
class Node:
    def __init__(self, city, pop):
        self.city = city
        self.pop = pop
        self.left = None
        self.right = None


# Function to insert a new city into the BST
def insert(root, city, pop):
    if not root:
        return Node(city, pop)
    if city < root.city:
        root.left = insert(root.left, city, pop)
    elif city > root.city:
        root.right = insert(root.right, city, pop)
    else:
        print(f"City '{city}' already exists.")
    return root


# Function to search for a city and count number of comparisons
def search(root, city):
    comps = 0
    current = root
    while current:
        comps += 1
        if city == current.city:
            return current, comps
        elif city < current.city:
            current = current.left
        else:
            current = current.right
    return None,   


# Function to update population of an existing city
def update(root, city, pop):
    node, _ = search(root, city)
    if node:
        node.pop = pop
        print(f"Population of '{city}' updated to {pop}.")
    else:
        print(f"City '{city}' not found.")


# Function to find the smallest (minimum) city node
def find_min(root):
    while root.left:
        root = root.left
    return root


# Function to delete a city from the BST
def delete(root, city):
    if not root:
        print(f"City '{city}' not found.")
        return None

    if city < root.city:
        root.left = delete(root.left, city)
    elif city > root.city:
        root.right = delete(root.right, city)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        temp = find_min(root.right)
        root.city, root.pop = temp.city, temp.pop
        root.right = delete(root.right, temp.city)

    return root


# Display cities in ascending order (inorder traversal)
def inorder(root):
    if root:
        inorder(root.left)
        print(f"{root.city} - Population: {root.pop}")
        inorder(root.right)


# Display cities in descending order (reverse inorder traversal)
def reverse_inorder(root):
    if root:
        reverse_inorder(root.right)
        print(f"{root.city} - Population: {root.pop}")
        reverse_inorder(root.left)


# -----------------------------
#       MENU-DRIVEN PROGRAM
# -----------------------------
root = None

while True:
    print("\n======= City Management Menu =======")
    print("1. Add City")
    print("2. Delete City")
    print("3. Update Population")
    print("4. Display Cities (Ascending)")
    print("5. Display Cities (Descending)")
    print("6. Search City")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice (1-7): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        city = input("Enter city name: ").strip()
        try:
            pop = int(input("Enter population: "))
            root = insert(root, city, pop)
        except ValueError:
            print("Invalid population value.")

    elif choice == 2:
        city = input("Enter city name to delete: ").strip()
        root = delete(root, city)

    elif choice == 3:
        city = input("Enter city name to update: ").strip()
        try:
            pop = int(input("Enter new population: "))
            update(root, city, pop)
        except ValueError:
            print("Invalid population value.")

    elif choice == 4:
        if root:
            print("\nCities in Ascending Order:")
            inorder(root)
        else:
            print("No cities to display.")

    elif choice == 5:
        if root:
            print("\nCities in Descending Order:")
            reverse_inorder(root)
        else:
            print("No cities to display.")

    elif choice == 6:
        city = input("Enter city name to search: ").strip()
        node, comps = search(root, city)
        if node:
            print(f"Found '{node.city}' with population {node.pop}. Comparisons: {comps}")
        else:
            print(f"City '{city}' not found. Comparisons: {comps}")

    elif choice == 7:
        print("Exiting program.!")  
        break

    else:
        print("Invalid choice. Please select between 1 and 7.")
