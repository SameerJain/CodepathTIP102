# Python Quick Reference Guide - CodePath TIP102 Unit 5

# ============= OBJECT ORIENTED PROGRAMMING (OOP) =============

# Classes - Blueprint for custom data types
# Properties - Variables that describe object characteristics
# Methods - Functions that define object behaviors


# Defining a Class
class Dog:
    # Constructor (__init__) - Builds new instance of class
    def __init__(self, name, breed, owner):
        self.name = name  # Property
        self.breed = breed  # Property
        self.owner = owner  # Property

    # Method - Function attached to object
    def call_dog(self):
        print(f"Here {self.name}!")

    # Method with parameters
    def command_trick(self, trick):
        print(f"{self.name}, {trick}!")


# Instantiating a Class (creating an object/instance)
my_dog = Dog("Fido", "Cocker Spaniel", "Ada Lovelace")

# Accessing Properties (dot notation)
print(my_dog.name)  # Prints 'Fido'
print(my_dog.breed)  # Prints 'Cocker Spaniel'

# Calling Methods (dot notation)
my_dog.call_dog()  # Prints 'Here Fido!'
my_dog.command_trick("roll over")  # Prints 'Fido, roll over!'

# self parameter:
# - Refers to current instance of class
# - First parameter in all class methods
# - Don't pass value for self when calling methods


# ============= LINKED LISTS =============

# Linked Lists vs Arrays:
# - Arrays: Elements stored consecutively in memory
# - Linked Lists: Elements stored in non-consecutive memory locations
# - Each node stores data AND reference to next node


# Node Class - Basic building block of linked list
class Node:
    def __init__(self, value, next=None):
        self.value = value  # Data stored in node
        self.next = next  # Reference to next node (or None)


# LinkedList Class - Optional wrapper for linked list operations
class LinkedList:
    def __init__(self):
        self.head = None  # First node in list (or None if empty)

    def add_first(self, value):
        pass  # Add node to beginning

    def append(self, value):
        pass  # Add node to end

    def length(self):
        pass  # Return length of list

    def get_at_index(self, index):
        pass  # Return value at index


# ============= LINKED LIST TRAVERSAL =============

# Standard traversal pattern:
# 1. Create pointer 'current' at head
# 2. Loop while current is not None
# 3. Perform operations on current node
# 4. Move current to next node


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def traverse(head):
    current = head
    while current:
        # Perform operations (e.g., print value)
        print(current.value)
        current = current.next  # Move to next node


# ============= ADVANCED: MULTIPLE PASS TECHNIQUE =============

# Traverse list multiple times to extract info before manipulating
# Time complexity NOT affected: O(n + n) = O(2n) => O(n)

# Example: Pair nodes in linked list
# Input: 1->2->3->4 returns [(1,2), (3,4)]
# Input: 1->2->3 returns None (odd length)


class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next


def pair_nodes(head):
    # Check if empty
    if not head:
        return None

    # Pass 1: Get length
    current = head
    length = 0
    while current:
        length += 1
        current = current.next

    # If odd length, return None
    if length % 2 != 0:
        return None

    # Pass 2: Create pairs
    pairs = []
    current = head
    while current:
        pairs.append((current.value, current.next.value))
        current = current.next.next  # Skip by 2

    return pairs


# With Helper Function
def get_length(head):
    current = head
    length = 0
    while current:
        length += 1
        current = current.next
    return length


def pair_nodes_v2(head):
    if not head:
        return None

    if get_length(head) % 2 != 0:  # Call helper
        return None

    pairs = []
    current = head
    while current:
        pairs.append((current.value, current.next.value))
        current = current.next.next

    return pairs


# ============= ADVANCED: TEMPORARY HEAD TECHNIQUE =============

# Create temp head to handle edge cases involving actual head:
# - Deleting head node
# - Adding to empty list
# - Adding to front of list
# - List with only one node

# Example: Delete first node with specific value
# Input: 1->2->4, val=2 returns 1->4


class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next


def delete_node(head, val):
    temp_head = Node("temp")  # Create temporary head
    temp_head.next = head  # Point temp head at input list

    # Traverse the list
    previous = temp_head
    current = head
    while current:
        if current.value == val:
            previous.next = current.next  # Delete node
            break

        previous = current
        current = current.next

    return temp_head.next  # Return actual head


# ============= ADVANCED: SLOW-FAST POINTER TECHNIQUE =============

# Also called Tortoise and Hare algorithm
# Two pointers moving at different speeds
# Slow pointer: moves 1 step at a time
# Fast pointer: moves 2 steps at a time

# Common uses:
# - Cycle detection
# - Finding middle of list
# - Finding meeting point in cycle

# Example: Detect if linked list has a cycle


class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next


def has_cycle(head):
    if not head:
        return False

    slow = head  # Slow pointer (walker)
    fast = head  # Fast pointer (runner)

    while fast and fast.next:
        slow = slow.next  # Move 1 step
        fast = fast.next.next  # Move 2 steps

        if slow == fast:  # If they meet, there's a cycle
            return True

    return False  # Fast reached end, no cycle


# Think: Runner laps walker on a track = cycle exists
#        Runner never sees walker again on straight path = no cycle


# ============= BONUS SYNTAX (NOT ON ASSESSMENT) =============

# List Methods
lst.extend(x)  # Append all elements from iterable x to list
lst.reverse()  # Reverse list in place
