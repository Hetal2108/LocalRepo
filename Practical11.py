# Define a class for tree nodes
class Node: 
    def __init__(self, val): 
        self.val = val      # Store value (operator or operand)
        self.left = None    # Left child
        self.right = None   # Right child

# Function to check if a character is an operator
def is_operator(c): 
    return c in "+-*/" 

# Function to construct an expression tree from prefix expression
def construct_tree(prefix): 
    stack = [] 
    # Traverse the prefix expression from right to left
    for ch in prefix[::-1]: 
        if not is_operator(ch): 
            # If it is an operand, create a node and push onto stack
            stack.append(Node(ch)) 
        else: 
            # If it is an operator, pop two nodes from stack to form a subtree
            if len(stack) < 2: 
                print("Invalid prefix expression! Not enough operands.") 
                return None 
            # Note: original code pops left first, then right (order reversed)
            left = stack.pop() 
            right = stack.pop() 
            node = Node(ch)      # Create a new node for the operator
            node.left = left     # Attach left child
            node.right = right   # Attach right child
            stack.append(node)   # Push the subtree back onto stack

    # After processing all characters, there should be exactly one node (root)
    if len(stack) != 1: 
        print("Invalid prefix expression! Too many operands.") 
        return None 
    return stack.pop()  # Return the root of the tree

# Function to perform post-order traversal without recursion
def postorder_non_recursive(root): 
    if root is None: 
        return 
    stack1 = [root]   # First stack for traversal
    stack2 = []       # Second stack to store nodes in post-order
    # Traverse tree
    while stack1: 
        node = stack1.pop() 
        stack2.append(node) 
        # Push left then right child so right is processed first (due to LIFO)
        if node.left: 
            stack1.append(node.left) 
        if node.right: 
            stack1.append(node.right) 

    # Pop all nodes from stack2 to print post-order traversal
    while stack2: 
        print(stack2.pop().val, end=' ') 
    print()  # Move to next line after traversal

# Function to delete tree (not necessary in Python due to garbage collection)
def delete_tree(root): 
    return None  # Remove reference to root, Python GC handles the rest

# ------------------- Main Program -------------------

# Take prefix expression input from user
prefix_exp = input("Enter prefix expression: ").strip() 

# Construct the expression tree
root = construct_tree(prefix_exp) 

# Perform non-recursive post-order traversal if tree is valid
if root: 
    print("Post-order traversal (non-recursive):") 
    postorder_non_recursive(root) 

# Delete tree (remove reference)
root = delete_tree(root) 
print("Tree deleted.")