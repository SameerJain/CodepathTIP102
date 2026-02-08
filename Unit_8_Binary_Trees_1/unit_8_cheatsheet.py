# Python Quick Reference Guide - CodePath TIP102 Unit 8

# ============= BINARY TREES =============

# Binary Tree - Non-linear data structure
# Each node can point to up to 2 other nodes (left and right children)


# TreeNode Class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left  # Left child pointer
        self.right = right  # Right child pointer


# Creating a tree:
#   1
#  / \
# 2   3

node_one = TreeNode(1)
node_two = TreeNode(2)
node_three = TreeNode(3)

node_one.left = node_two  # Node 2 is left child of node 1
node_one.right = node_three  # Node 3 is right child of node 1


# ============= TREE TERMINOLOGY =============

# root - Top-most node in tree
# leaf - Node with no children
# edge - Reference/pointer between parent and child
# height - Max edges from leaf to root
# level - All nodes at same height
# subtree - Tree formed by node + its descendants (not root)
# ancestor - Node closer to root on path to root
# descendant - Node in current node's subtree
# siblings - Nodes that share a parent


# ============= BALANCED TREES =============

# Balanced Tree:
# - Height difference between left/right subtrees ≤ 1
# - Both subtrees also balanced
# - Nodes spread fairly evenly

# Balanced trees → faster algorithms
# Easier to reach bottom or find specific node


# ============= TREE TRAVERSAL =============

# Depth First Search (DFS) - Three types:
# 1. Preorder: Current, Left, Right
# 2. Inorder: Left, Current, Right
# 3. Postorder: Left, Right, Current


# PREORDER TRAVERSAL
# Visit order: Current → Left subtree → Right subtree
# Use case: Save tree structure, copy tree


def preorder(node):
    if node is None:
        return

    print(node.value)  # Visit current
    preorder(node.left)  # Traverse left
    preorder(node.right)  # Traverse right


# Example tree:      7
#                   / \
#                  4   9
#                 / \   \
#                2   5   11
#               / \
#              1   3
# Output: 7, 4, 2, 1, 3, 5, 9, 11


# INORDER TRAVERSAL
# Visit order: Left subtree → Current → Right subtree
# Use case: Print BST nodes in sorted order (smallest to largest)


def inorder(node):
    if node is None:
        return

    inorder(node.left)  # Traverse left
    print(node.value)  # Visit current
    inorder(node.right)  # Traverse right


# Same tree as above
# Output: 1, 2, 3, 4, 5, 7, 9, 11


# POSTORDER TRAVERSAL
# Visit order: Left subtree → Right subtree → Current
# Use case: Delete tree (process children before parent)


def postorder(node):
    if node is None:
        return

    postorder(node.left)  # Traverse left
    postorder(node.right)  # Traverse right
    print(node.value)  # Visit current


# Same tree as above
# Output: 1, 3, 2, 5, 4, 11, 9, 7


# ============= BINARY SEARCH TREES (BST) =============

# Binary Search Tree rules:
# - All nodes in LEFT subtree < node's value
# - All nodes in RIGHT subtree > node's value

# BST Example:       19
#                   /  \
#                  7    25
#                 / \   / \
#                3  11 22  27


# TreeNode with key property for BST
class TreeNode:
    def __init__(self, key, value=0, left=None, right=None):
        self.key = key  # Integer for sorted order
        self.value = value  # Any data
        self.left = left
        self.right = right


# Example:
# By Key:        By Value:
#     1              Yoda
#    / \            /   \
#   2   3         Luke  R2D2

z = TreeNode(2, "Yoda")
x = TreeNode(1, "Luke")
y = TreeNode(3, "R2D2")


# ============= BST OPERATIONS =============

# BST operations: insert, delete, search
# Time Complexity: O(log n) for balanced tree

# Search BST
# - Compare target key with current node's key
# - If target < current, go left
# - If target > current, go right
# - Cut search space in half each time (like binary search!)


class TreeNode:
    def __init__(self, key, value=0, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


def search_bst(node, key):
    # Base case: node is None or found the key
    if node is None or node.key == key:
        return node

    # If key < current key, search left subtree
    if key < node.key:
        return search_bst(node.left, key)

    # If key > current key, search right subtree
    return search_bst(node.right, key)


# ============= TRAVERSAL PATTERNS SUMMARY =============

# Preorder (Current, Left, Right):
# - Save/copy tree structure
# - Visit nodes in order they were added

# Inorder (Left, Current, Right):
# - BST: prints values in sorted order
# - Left → Right traversal

# Postorder (Left, Right, Current):
# - Delete tree (children before parent)
# - Process all descendants before root


# ============= BONUS: THROWAWAY VARIABLE =============

# _ (underscore) - Ignore values not needed


# Example 1: Function returns multiple values, only need one
def get_coordinates():
    return (10, 20, 30)


x, _, _ = get_coordinates()  # Only care about x

# Example 2: Loop variable not needed
for _ in range(5):
    print("Hello")  # Don't need loop counter
