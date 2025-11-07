
SIZE = 10  # Fixed size of the hash table 
 
hash_table = [None] * SIZE 
 
def hash_function(key): 
    return key % SIZE 
 
def insert(key): 
    idx = hash_function(key) 
    start_idx = idx 
    while hash_table[idx] is not None: 
        if hash_table[idx] == key: 
            print(f"Key {key} already exists.") 
            return 
        idx = (idx + 1) % SIZE 
        if idx == start_idx: 
            print("Hash table is full!") 
            return 
    hash_table[idx] = key 
    print(f"Inserted {key} at index {idx}.") 
 
def search(key): 
    idx = hash_function(key) 
    start_idx = idx 
    while hash_table[idx] is not None: 
        if hash_table[idx] == key: 
            print(f"Key {key} found at index {idx}.") 
            return 
        idx = (idx + 1) % SIZE 
        if idx == start_idx: 
            break 
    print(f"Key {key} not found.") 
 
def delete(key): 
    idx = hash_function(key) 
    start_idx = idx 
    while hash_table[idx] is not None: 
        if hash_table[idx] == key: 
            hash_table[idx] = None 
            print(f"Key {key} deleted from index {idx}.") 
            return 
        idx = (idx + 1) % SIZE 
        if idx == start_idx: 
            break 
    print(f"Key {key} not found, cannot delete.") 
 
def display(): 
    print("Hash Table:") 
    for i, val in enumerate(hash_table): 
        print(f"Index {i}: {val}") 
 
# Simple menu-driven interface 
while True: 
    print("\n1. Insert\n2. Search\n3. Delete\n4. Display\n5. Exit") 
    choice = input("Enter choice: ") 
 
    if choice == '1': 
        key = int(input("Enter key to insert: ")) 
        insert(key) 
    elif choice == '2': 
        key = int(input("Enter key to search: ")) 
        search(key) 
    elif choice == '3': 
        key = int(input("Enter key to delete: ")) 
        delete(key) 
    elif choice == '4': 
        display() 
    elif choice == '5': 
        print("Exiting...") 
        break 
    else: 
        print("Invalid choice. Try again.")