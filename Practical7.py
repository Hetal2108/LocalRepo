class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = []
        for i in range(size):   # create empty buckets
            self.table.append([])

    def hash_function(self, key):
        # Use Python's built-in hash (works for int, str, etc.)
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:  # key already exists → update
                pair[1] = value
                print(f"Updated key {key} with new value '{value}' at index {index}")
                return
        self.table[index].append([key, value])  # new key → insert
        print(f"Inserted key {key} with value '{value}' at index {index}")

    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                print(f"Found key {key} with value '{pair[1]}' at index {index}")
                return pair[1]
        print(f"Key {key} not found.")
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                print(f"Deleted key {key} from index {index}")
                return
        print(f"Key {key} not found. Cannot delete.")

    def display(self):
        print("\nHash Table:")
        for i, chain in enumerate(self.table):
            print(f"Index {i}: {chain}")


# -------------------------
# Menu-driven interface
# -------------------------
ht = HashTable()

while True:
    print("\n=== Hash Table Menu ===")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display Table")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        key = input("Enter key (can be number or word): ")
        try:
            key = int(key)
        except ValueError:
            pass  # keep as string

        value = input("Enter value: ")
        ht.insert(key, value)

    elif choice == "2":
        key = input("Enter key to search: ")
        try:
            key = int(key)
        except ValueError:
            pass
        ht.search(key)

    elif choice == "3":
        key = input("Enter key to delete: ")
        try:
            key = int(key)
        except ValueError:
            pass
        ht.delete(key)

    elif choice == "4":
        ht.display()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
