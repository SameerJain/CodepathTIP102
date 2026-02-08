
# Python Quick Reference Guide - CodePath TIP102 Unit 10

# ============= GRAPHS =============

# Graph - Data structure representing relationships between entities
# Components:
# - Nodes (vertices) - Represent entities
# - Edges - Connect two nodes, represent relationships

# Unlike trees:
# - No root node
# - Can start traversal from any node
# - Nodes can connect to ANY number of other nodes

# Graph Types:
# - Undirected: Two-way relationships (e.g., state borders)
# - Directed: One-way relationships (e.g., flights)
# - Weighted: Edges have costs/weights (e.g., flight prices)
# - Unweighted: All edges equal

# Neighbors - Nodes that share a direct edge
# Path - Sequence of edges connecting nodes
# Connected Component - Group of nodes where any two are connected by a path
# Cycle - Path that returns to starting node
# DAG (Directed Acyclic Graph) - Directed graph with no cycles


# ============= GRAPH REPRESENTATIONS =============

# 1. NODE CLASS (Uncommon for graphs)
class GraphNode:
    def __init__(self, value, edges=None):
        self.val = value
        if not edges:
            self.edges = []
        else:
            self.edges = edges
    
    def add_connection(self, new_node):
        self.edges.append(new_node)


# 2. LIST OF EDGES (Basic)
# 2D list where each inner list is [start_node, dest_node]
# Graph: 0---1---2---3

list_of_edges = [
    [0, 1],
    [1, 2],
    [2, 3]
]

# Weighted graph: [start_node, dest_node, weight]
weighted_edges = [
    [0, 1, 5],
    [1, 2, 3],
    [2, 3, 7]
]


# 3. ADJACENCY LIST (Most Common)
# Outer list indices = nodes
# adjacency_list[i] = list of node i's neighbors

# Graph: 0---1---2---3
adjacency_list = [
    [1],       # Node 0's neighbors
    [0, 2],    # Node 1's neighbors
    [1, 3],    # Node 2's neighbors
    [2]        # Node 3's neighbors
]

# Empty list = no neighbors
# Undirected graph: if j in adjacency_list[i], then i in adjacency_list[j]


# 4. ADJACENCY DICTIONARY (Very Common)
# Key = node, Value = list of neighbors
# Works for non-numerical nodes

# Graph: 0---1---2---3
adjacency_dict = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2]
}

# String nodes example (cities and flights)
city_graph = {
    "Mexico City": ["São Paulo", "Los Angeles"],
    "Los Angeles": ["Mexico City", "Atlanta"],
    "Atlanta": ["Los Angeles"],
    "São Paulo": []
}

# Weighted graph: use tuples (neighbor, weight)
weighted_dict = {
    "Mexico City": [("São Paulo", 200), ("Los Angeles", 110)],
    "Los Angeles": [("Mexico City", 300), ("Atlanta", 100)],
    "Atlanta": [("Los Angeles", 250)],
    "São Paulo": []
}


# 5. ADJACENCY MATRIX (Less Common)
# n x n matrix where n = number of nodes
# adjacency_matrix[i][j] = 1 if edge from i to j, else 0

# Graph: 0---1---2---3
adjacency_matrix = [
    [0, 1, 0, 0],  # Node 0
    [1, 0, 1, 0],  # Node 1
    [0, 1, 0, 1],  # Node 2
    [0, 0, 1, 0]   # Node 3
]

# Undirected: adjacency_matrix[i][j] = adjacency_matrix[j][i]
# Weighted: replace 1 with edge weight


# ============= BREADTH-FIRST SEARCH (BFS) =============

# BFS - Explores level by level (nearest neighbors first)
# Uses QUEUE (FIFO)
# Finds shortest path in unweighted graphs

from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque()
    
    # Add start node to queue and visited
    queue.append(start)
    visited.append(start)
    
    # While queue not empty
    while queue:
        # Dequeue node
        current = queue.popleft()
        
        # Loop through neighbors
        for neighbor in graph[current]:
            # If neighbor not visited
            if neighbor not in visited:
                # Add to queue and visited
                queue.append(neighbor)
                visited.append(neighbor)
    
    return visited

# Example usage:
graph = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2]
}
print(bfs(graph, 0))  # [0, 1, 2, 3]


# BFS Pseudocode:
"""
- Initialize empty list of visited nodes
- Initialize empty queue
- Add start node to queue
- Add start node to visited
- While queue not empty:
    - Remove element from queue → current
    - Loop through current's neighbors:
        - If neighbor not visited:
            - Add neighbor to queue
            - Add neighbor to visited
- Return visited nodes
"""


# ============= DEPTH-FIRST SEARCH (DFS) =============

# DFS - Explores one path as far as possible before backtracking
# Uses STACK (LIFO) or recursion
# Like exploring a maze

# Iterative DFS (using stack)
def dfs_iterative(graph, start):
    visited = []
    stack = [start]
    
    while stack:
        # Pop node from stack
        current = stack.pop()
        
        # If not visited
        if current not in visited:
            # Mark as visited
            visited.append(current)
            
            # Add unvisited neighbors to stack
            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return visited


# Recursive DFS (more common)
def dfs(graph, start):
    visited = []
    dfs_helper(graph, start, visited)
    return visited

def dfs_helper(graph, start, visited):
    # If not visited
    if start not in visited:
        # Mark as visited
        visited.append(start)
        
        # Recursively visit neighbors
        for neighbor in graph[start]:
            dfs_helper(graph, neighbor, visited)

# Example usage:
graph = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2]
}
print(dfs(graph, 0))  # [0, 1, 2, 3]


# DFS Pseudocode (Recursive):
"""
Main function:
- Create empty visited list
- Call dfs_helper with start node and visited
- Return visited

Helper function:
- If start not in visited:
    - Add start to visited
    - Loop through start's neighbors:
        - Call dfs_helper with neighbor
"""


# ============= BFS vs DFS =============

# Both:
# - Time Complexity: O(V + E) where V=vertices, E=edges
# - Space Complexity: O(V)
# - Find connected nodes, find paths, traverse graph

# BFS Special Use Cases:
# - Shortest path in unweighted graph (visits closest first)
# - Node likely close to start
# - Level-by-level traversal

# DFS Special Use Cases:
# - Backtracking problems
# - Cycle detection (especially in directed graphs)
# - Topological sorting of DAGs
# - When solution is likely deep in graph


# ============= BFS vs DFS COMPARISON =============

# BFS:
# - Uses QUEUE
# - Visits level by level
# - Finds shortest path (unweighted)
# - Good for nearby solutions

# DFS:
# - Uses STACK (or recursion)
# - Goes deep before wide
# - Good for backtracking
# - Good for cycle detection


# ============= GRAPH REPRESENTATION BIG O =============

# List of Edges:
# - Check if edge exists: O(E)
# - Get neighbors: O(E)
# - Space: O(E)

# Adjacency List/Dictionary:
# - Check if edge exists: O(D) where D = degree of node
# - Get neighbors: O(1)
# - Space: O(E)

# Adjacency Matrix:
# - Check if edge exists: O(1)
# - Get neighbors: O(N) where N = number of nodes
# - Space: O(N²)


# ============= TRAVERSING DISCONNECTED GRAPHS =============

# BFS/DFS only finds nodes reachable from start
# To traverse ALL nodes (including disconnected):

def traverse_all_components(graph):
    visited = set()
    components = []
    
    for node in graph:
        if node not in visited:
            # Run BFS/DFS from unvisited node
            component = bfs_component(graph, node, visited)
            components.append(component)
    
    return components

def bfs_component(graph, start, visited):
    component = []
    queue = deque([start])
    visited.add(start)
    
    while queue:
        current = queue.popleft()
        component.append(current)
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    
    return component


# ============= BONUS CONCEPTS (NOT ON ASSESSMENT) =============

# Backtracking - Build solutions incrementally, backtrack when stuck
# Topological Sorting - Order nodes in DAG respecting dependencies
# Dijkstra's Algorithm - Shortest path in weighted graph
# Minimum Spanning Tree - Connect all nodes with minimum total weight
# Prim's Algorithm - Find minimum spanning tree
# Kruskal's Algorithm - Find minimum spanning tree
