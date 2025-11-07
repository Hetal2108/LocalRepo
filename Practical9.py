# Input number of locations  
n = int(input("Enter number of locations: "))

# Input location names  
locations = []
print("Enter location names:")
for i in range(n):
    loc = input().strip()
    locations.append(loc)

# Map each location to an index 
index = {}
for i in range(n):
    index[locations[i]] = i

# Initialize adjacency matrix with zeros 
adj_matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    adj_matrix.append(row)

# Initialize adjacency list with empty lists 
adj_list = {}
for i in range(n):
    adj_list[locations[i]] = []

# Input number of connections 
e = int(input("Enter number of connections/routes: "))
print("Enter connections (format: location1 location2):")
for i in range(e):
    n1, n2 = input().split()
    i1 = index[n1]
    i2 = index[n2]

    # Undirected connection 
    adj_matrix[i1][i2] = 1
    adj_matrix[i2][i1] = 1

    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

# DFS using adjacency matrix 
def dfs_matrix(matrix, curr, visited, locations):
    print(locations[curr], end=" ")
    visited[curr] = True

    for i in range(len(matrix)):
        if matrix[curr][i] == 1 and not visited[i]:
            dfs_matrix(matrix, i, visited, locations)

# BFS using adjacency list 
def bfs(adj_list, start):
    visited = {}
    for loc in adj_list:
        visited[loc] = False

    queue = []
    queue.append(start)
    visited[start] = True

    while len(queue) > 0:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# Input start location 
start_node = input("Enter start location: ").strip()

# Run DFS 
print("\nDFS traversal starting from", start_node + ":")
visited_dfs = [False] * n
dfs_matrix(adj_matrix, index[start_node], visited_dfs, locations)

# Run BFS 
print("\nBFS traversal starting from", start_node + ":")
bfs(adj_list, start_node)
