# Python Quick Reference Guide - CodePath TIP102 Unit 6

# ============= CHAINED ASSIGNMENT =============

# Assign multiple variables to same value in one line
x = y = z = 3
print(x)  # Prints 3
print(y)  # Prints 3
print(z)  # Prints 3

# Useful for initializing multiple variables


# ============= BREAK STATEMENTS =============

# Break keyword - Exit loop early

# Example 1: While Loop
count = 1
while count <= 10:
    if count == 5:
        break  # Exit loop when count reaches 5
    print(count)
    count += 1
# Output: 1, 2, 3, 4

# Example 2: For Loop
numbers = [1, 3, 5, 7, 9, 2, 4]
for number in numbers:
    if number % 2 == 0:
        print(f"First even number found: {number}")
        break  # Exit loop after finding first even number
# Output: First even number found: 2


# ============= LINKED LIST: MULTIPLE PASS TECHNIQUE =============

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


# ============= LINKED LIST: TEMPORARY HEAD TECHNIQUE =============

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


# ============= LINKED LIST: SLOW-FAST POINTER TECHNIQUE =============

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
