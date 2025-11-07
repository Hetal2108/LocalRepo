# --------- LINEAR SEARCH FUNCTION ---------
def lin_search(cust_ids, target):
    for i in range(len(cust_ids)):
        if cust_ids[i] == target:
            return i  # Return the index
    return -1

# --------- BINARY SEARCH FUNCTION ---------
def bin_search(sorted_ids, target):
    left = 0
    right = len(sorted_ids) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_ids[mid] == target:
            return mid
        elif sorted_ids[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# --------- MAIN PROGRAM ---------
print("  E-commerce Customer Account ID Search  ")

# Get input list of customer IDs
print("\nEnter number of customer account IDs:")
n = int(input())

cust_ids = []
print(f"Enter {n} customer account IDs (numeric):")
for i in range(n):
    print(f"  ID {i+1}: ", end='')
    cust_ids.append(int(input()))

# Ask for the ID to search
print("\nEnter customer account ID to search:")
target_id = int(input())

# Perform Linear Search
lin_result = lin_search(cust_ids, target_id)

# Perform Binary Search (requires sorted list)
sorted_ids = cust_ids[:]  # Make a copy
# Sort manually without using sort()
for i in range(len(sorted_ids)):
    for j in range(i + 1, len(sorted_ids)):
        if sorted_ids[i] > sorted_ids[j]:
            # Swap
            temp = sorted_ids[i]
            sorted_ids[i] = sorted_ids[j]
            sorted_ids[j] = temp

bin_result = bin_search(sorted_ids, target_id)

# --------- OUTPUT RESULTS ---------
print("\n  Search Results:\n")

if lin_result != -1:
    print(f"Linear Search: ID found at position {lin_result} (index in original list).")
else:
    print("Linear Search: ID not found.")

if bin_result != -1:
    print(f"Binary Search: ID found at position {bin_result} (index in sorted list).")
else:
    print("Binary Search: ID not found.")
