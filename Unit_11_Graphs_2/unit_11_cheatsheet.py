# Python Quick Reference Guide - CodePath TIP102 Unit 11

# ============= MATRICES AS GRAPHS =============

# Matrix cells can be treated as graph nodes
# Edges exist between horizontally/vertically adjacent cells

# Matrix:
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Becomes graph where:
# - Each cell is a node
# - Adjacent cells (up, down, left, right) are connected by edges

# Binary Matrix with constraints:
# Only cells with value 1 are connected
grid = [
    [1, 1, 1],
    [0, 1, 0],
    [0, 1, 1]
]
# Edges only between adjacent cells that both have value 1


# BFS on Matrix Pseudocode:
"""
- Start from cell, add to queue, mark visited
- While queue not empty:
    - Take cell from front of queue
    - Check neighbors (up, down, left, right)
    - For each neighbor:
        - If not visited, add to queue and mark visited
- Repeat until all reachable cells visited
"""

# DFS on Matrix Pseudocode:
"""
- Start from cell, mark visited
- Recursively move to neighbors (up, down, left, right) if not visited
- If no unvisited neighbors, backtrack
- Repeat until all reachable cells visited
"""


# ============= FLOOD FILL =============

# Algorithm to fill connected area starting from specific point
# "Floods" area with new color/value based on conditions
# Common in: Graphics (bucket tool), games, puzzles

# Flood Fill Pseudocode:
"""
1. Start from given cell (row, column)
2. Check if cell meets condition (same color/value)
3. Fill cell with new value
4. Move to neighbors (up, right, down, left) that meet condition
5. Repeat until entire region filled
"""

# Can use BFS or DFS implementation


# ============= BACKTRACKING =============

# Build solution incrementally
# Make choice → Continue → Hit dead end → Backtrack → Try different choice
# Example: Finding path through maze

# Backtracking involves:
# - Making choices at each step
# - Exploring multiple paths
# - Meeting constraints

# DFS is a form of backtracking!
# - Explore one path deeply
# - When stuck, back up and try different path
# - Continue until all options exhausted or solution found


# ============= PRIORITY QUEUES =============

# Priority Queue - Removes items by priority, not FIFO
# Types:
# - Min Priority Queue: smallest priority first
# - Max Priority Queue: largest priority first

import heapq

# Create empty heap (min priority queue)
heap = []

# Add items: heapq.heappush(heap, item)
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 4)
print(heap)  # Output: [1, 3, 4]

# Remove smallest: heapq.heappop(heap)
smallest = heapq.heappop(heap)
print(smallest)  # Output: 1

# Add with different priority: (priority, item)
heap_2 = []
heapq.heappush(heap_2, (3, 'a'))
heapq.heappush(heap_2, (1, 'b'))
heapq.heappush(heap_2, (4, 'c'))
print(heap_2)  # Output: [(1, 'b'), (3, 'a'), (4, 'c')]

smallest = heapq.heappop(heap_2)
print(smallest)  # Output: (1, 'b')

# Simulate max heap with negative values
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -4)
max_value = -heapq.heappop(max_heap)  # Output: 4


# ============= TOPOLOGICAL SORT =============

# Sort tasks/events based on dependencies
# Only works on DAGs (Directed Acyclic Graphs)
# Result: Ordering where for every edge u → v, u comes before v

# Two approaches: BFS (Kahn's Algorithm) and DFS


# BFS APPROACH (Kahn's Algorithm)
# Uses in-degree (number of incoming edges)

"""
Kahn's Algorithm Pseudocode:
1. Calculate in-degree of each node
2. Start with nodes having in-degree 0 (no dependencies)
3. Remove processed node from graph
4. For each neighbor, reduce in-degree by 1
5. Add new nodes with in-degree 0 to queue
6. Repeat until all nodes processed
"""


# DFS APPROACH
# Process nodes after all descendants visited

"""
DFS Topological Sort Pseudocode:
1. Perform DFS on graph
2. When visiting node, recursively visit all neighbors
3. After visiting all neighbors, add node to stack
4. Continue until all nodes visited
5. Reverse stack to get topological order
"""


# Comparison:
# Kahn's (BFS): Better for cycle detection, processes in levels
# DFS: More memory efficient, explores dependencies deeply


# ============= DIJKSTRA'S ALGORITHM =============

# Find shortest path in WEIGHTED graph
# BFS finds shortest path in UNWEIGHTED graph
# Dijkstra's uses priority queue to explore lowest cost paths first

"""
Dijkstra's Algorithm Pseudocode:

1. Initialize distances list (length = num nodes)
   - Set all to infinity
   - Set distances[start] = 0

2. Initialize previous list (length = num nodes)
   - Set all to None
   - Tracks shortest path

3. Initialize visited list

4. Initialize priority queue, add start node

5. While queue not empty:
   a. Get node with minimum cost from queue
   b. Mark as visited
   c. For each neighbor:
      i. If not visited:
         1. Calculate distance via current node
         2. If distance < distances[neighbor]:
            - Update distances[neighbor]
            - Update previous[neighbor] = current
         3. Add neighbor to queue

6. Return previous and distances lists
"""

# Example: Shortest path from A to G
# Updates distances as it explores, keeps track of minimum cost path


# ============= UNION FIND (DISJOINT SET UNION) =============

# Data structure for grouping objects into non-overlapping sets
# Two key operations:
# - Find: Which set does element belong to?
# - Union: Combine two sets into one

# Common uses:
# - Finding connected components
# - Detecting cycles in undirected graphs
# - Minimum Spanning Tree (Kruskal's Algorithm)

# Each set represented as tree
# Root node = representative node


# UNION FIND IMPLEMENTATION

class DSU:
    def __init__(self, n):
        # Each element is ow