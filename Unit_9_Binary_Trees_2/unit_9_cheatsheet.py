
# Python Quick Reference Guide - CodePath TIP102 Unit 9

# ============= BREADTH FIRST SEARCH (BFS) =============

# BFS / Level Order Traversal
# Visit nodes level by level, left to right
# Root → Root's children → Root's grandchildren → etc.

# Example tree:         19
#                      /  \
#                     7    25
#                    / \   / \
#                   5  22 71  
#                  /      \
#                 6        30
#                           \
#                            96

# BFS Order: [19, 7, 25, 5, 22, 71, 6, 30, 96]
# Level 1: 19
# Level 2: 7, 25
# Level 3: 5, 22, 71
# Level 4: 6, 30
# Level 5: 96


# ============= BFS IMPLEMENTATION =============

# BFS uses a QUEUE (FIFO - First In First Out)
# Implemented ITERATIVELY (not recursively)

from collections import deque

class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def bfs(root):
    # If tree is empty, return empty list
    if not root:
        return []
    
    # Create queue and visited list
    queue = deque()
    visited = []
    
    # Add root to queue
    queue.append(root)
    
    # While queue is not empty
    while queue:
        # Pop next node from queue (from front)
        node = queue.popleft()
        
        # Add node to visited list
        visited.append(node.value)
        
        # Add left child to queue (if exists)
        if node.left:
            queue.append(node.left)
        
        # Add right child to queue (if exists)
        if node.right:
            queue.append(node.right)
    
    return visited


# ============= BFS PSEUDOCODE =============

"""
If the tree is empty:
    return an empty list

Create an empty queue
Create an empty list to store visited nodes

Add the root into the queue

While the queue is not empty:
    Pop the next node off the queue 
    Add the popped node to the list of visited nodes

    Add the popped node's left child to the queue
    Add the popped node's right child to the queue
"""


# ============= HOW TO PICK A TRAVERSAL METHOD =============

# Four standard traversals:
# - Preorder (DFS): Current, Left, Right
# - Inorder (DFS): Left, Current, Right
# - Postorder (DFS): Left, Right, Current
# - BFS: Level by level, left to right


# DEPTH FIRST SEARCH (DFS)
# Use when: Solution expected deeper in tree
# - Follows one branch as far as possible before backtracking

# INORDER (Left, Current, Right)
# Use for:
# - Binary Search Trees → traverses in sorted order
# - Finding leaves
# - Finding height of tree
# - Finding diameter of tree
# - Converting BST to sorted list

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.value)
    inorder(node.right)


# PREORDER (Current, Left, Right)
# Use for:
# - Tree copying
# - Expression tree evaluation
# - Serializing a tree
# - Processing root before subtrees
# - Nodes in insertion order

def preorder(node):
    if node is None:
        return
    print(node.value)
    preorder(node.left)
    preorder(node.right)


# POSTORDER (Left, Right, Current)
# Use for:
# - Deleting a tree
# - Expression tree evaluation
# - Processing subtrees before root

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value)


# BREADTH FIRST SEARCH (BFS)
# Use when:
# - Solution expected closer to root
# - Need to traverse level by level
# - Problems requiring level-order traversal
# - Finding shortest path in unweighted tree

from collections import deque

def bfs_traversal(root):
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node.value)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result


# ============= DFS vs BFS COMPARISON =============

# DFS (Depth First Search):
# - Uses STACK (recursion or explicit stack)
# - Goes deep before going wide
# - Memory: O(h) where h = height
# - Preferred when solution is deep in tree

# BFS (Breadth First Search):
# - Uses QUEUE
# - Goes wide before going deep
# - Memory: O(w) where w = max width of tree
# - Preferred when solution is near root


# ============= TRAVERSAL SELECTION GUIDE =============

"""
Problem Type                    → Traversal
--------------------------------------------------
BST in sorted order             → Inorder
Find height/diameter/leaves     → Inorder
Copy tree                       → Preorder
Serialize tree                  → Preorder
Delete tree                     → Postorder
Level-by-level problems         → BFS
Solution near root              → BFS
Solution deep in tree           → DFS (any)
"""


# ============= EXAMPLE: LEVEL ORDER TRAVERSAL =============

# Return list of lists, where each sublist is one level

from collections import deque

def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

# Example tree:    1
#                 / \
#                2   3
#               / \
#              4   5
# Output: [[1], [2, 3], [4, 5]]
