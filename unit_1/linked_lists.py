"""
LinkedList Problems - Unit 1
Educational linked list problems for CodePath TIP102
"""


class Node:
    """Basic Node class for linked list"""

    def __init__(self, value):
        self.value = value
        self.next = None


class problem_1:
    """Create a linked list from a list of values"""

    def create_linked_list(self, values):
        """
        U- Given a list of values, create a linked list
        P- Create head node, iterate through remaining values, append each
        I- Use a current pointer to traverse and attach new nodes
        """
        if not values:
            return None

        head = Node(values[0])
        current = head

        for value in values[1:]:
            current.next = Node(value)
            current = current.next

        return head

    def print_list(self, head):
        """Helper to print linked list"""
        result = []
        current = head
        while current:
            result.append(str(current.value))
            current = current.next
        print(" -> ".join(result))

    def test_1(self):
        """Test: Create list [1, 2, 3]"""
        head = self.create_linked_list([1, 2, 3])
        self.print_list(head)  # Expected: 1 -> 2 -> 3

    def test_2(self):
        """Test: Create empty list"""
        head = self.create_linked_list([])
        print(head)  # Expected: None

    def test_3(self):
        """Test: Single element list"""
        head = self.create_linked_list([5])
        self.print_list(head)  # Expected: 5


class problem_2:
    """Find the length of a linked list"""

    def length(self, head):
        """
        U- Count the number of nodes in a linked list
        P- Traverse the list counting each node
        I- Use a current pointer and counter
        """
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count

    def test_1(self):
        """Test length of [1, 2, 3]"""
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        print(f"Length: {self.length(head)}")  # Expected: 3

    def test_2(self):
        """Test length of empty list"""
        print(f"Length: {self.length(None)}")  # Expected: 0


class problem_3:
    """Access node at given index"""

    def get_node_at_index(self, head, index):
        """
        U- Return the node at the given index (0-indexed)
        P- Traverse through index steps using current pointer
        I- Check bounds, iterate to index position
        """
        current = head
        for _ in range(index):
            if not current:
                return None
            current = current.next
        return current

    def test_1(self):
        """Test getting node at index 1"""
        head = Node(10)
        head.next = Node(20)
        head.next.next = Node(30)
        node = self.get_node_at_index(head, 1)
        print(f"Value at index 1: {node.value if node else None}")  # Expected: 20

    def test_2(self):
        """Test out of bounds index"""
        head = Node(10)
        node = self.get_node_at_index(head, 5)
        print(f"Value at index 5: {node}")  # Expected: None


class problem_4:
    """Reverse a linked list"""

    def reverse(self, head):
        """
        U- Reverse the direction of all node pointers
        P- Use three pointers: prev, current, next to reverse links
        I- Iterate through list, reverse each node's next pointer
        """
        prev = None
        current = head

        while current:
            next_temp = current.next  # Save next node
            current.next = prev  # Reverse the link
            prev = current  # Move prev forward
            current = next_temp  # Move current forward

        return prev

    def print_list(self, head):
        """Helper to print linked list"""
        result = []
        current = head
        while current:
            result.append(str(current.value))
            current = current.next
        print(" -> ".join(result) if result else "Empty")

    def test_1(self):
        """Test reversing [1, 2, 3]"""
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        print("Original:")
        self.print_list(head)
        reversed_head = self.reverse(head)
        print("Reversed:")
        self.print_list(reversed_head)  # Expected: 3 -> 2 -> 1


class problem_5:
    """Find if value exists in linked list"""

    def contains(self, head, target):
        """
        U- Check if a target value exists in the linked list
        P- Traverse list checking each node's value
        I- Return True on match, False if reach end
        """
        current = head
        while current:
            if current.value == target:
                return True
            current = current.next
        return False

    def test_1(self):
        """Test finding existing value"""
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        print(f"Contains 2: {self.contains(head, 2)}")  # Expected: True

    def test_2(self):
        """Test finding non-existing value"""
        head = Node(1)
        head.next = Node(2)
        print(f"Contains 5: {self.contains(head, 5)}")  # Expected: False


class problem_6:
    """Delete a node at given index"""

    def delete_at_index(self, head, index):
        """
        U- Remove the node at the given index
        P- Find the node before target, adjust pointers
        I- Handle edge cases (index 0, out of bounds)
        """
        if index == 0 and head:
            return head.next

        current = head
        for _ in range(index - 1):
            if not current or not current.next:
                return head
            current = current.next

        if current and current.next:
            current.next = current.next.next

        return head

    def print_list(self, head):
        """Helper to print linked list"""
        result = []
        current = head
        while current:
            result.append(str(current.value))
            current = current.next
        print(" -> ".join(result) if result else "Empty")

    def test_1(self):
        """Test deleting index 1 from [1, 2, 3]"""
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        print("Before deletion:")
        self.print_list(head)
        head = self.delete_at_index(head, 1)
        print("After deleting index 1:")
        self.print_list(head)  # Expected: 1 -> 3


class problem_7:
    """Insert a node at given index"""

    def insert_at_index(self, head, index, value):
        """
        U- Insert a new node with given value at specified index
        P- Find position before insertion point, create node, adjust pointers
        I- Handle edge cases (index 0, out of bounds)
        """
        new_node = Node(value)

        if index == 0:
            new_node.next = head
            return new_node

        current = head
        for _ in range(index - 1):
            if not current:
                return head
            current = current.next

        if current:
            new_node.next = current.next
            current.next = new_node

        return head

    def print_list(self, head):
        """Helper to print linked list"""
        result = []
        current = head
        while current:
            result.append(str(current.value))
            current = current.next
        print(" -> ".join(result) if result else "Empty")

    def test_1(self):
        """Test inserting 99 at index 1"""
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        print("Before insertion:")
        self.print_list(head)
        head = self.insert_at_index(head, 1, 99)
        print("After inserting 99 at index 1:")
        self.print_list(head)  # Expected: 1 -> 99 -> 2 -> 3


class problem_8:
    """Find the middle node of a linked list"""

    def find_middle(self, head):
        """
        U- Find the middle node of a linked list
        P- Use slow and fast pointers (tortoise and hare)
        I- Fast moves 2 steps, slow moves 1 step; when fast reaches end, slow is at middle
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def test_1(self):
        """Test middle of [1, 2, 3, 4, 5]"""
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        middle = self.find_middle(head)
        print(f"Middle value: {middle.value}")  # Expected: 3

    def test_2(self):
        """Test middle of [1, 2, 3, 4]"""
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        middle = self.find_middle(head)
        print(f"Middle value: {middle.value}")  # Expected: 3


class problem_9:
    """Detect cycle in linked list"""

    def has_cycle(self, head):
        """
        U- Determine if a linked list contains a cycle
        P- Use slow and fast pointers (tortoise and hare)
        I- If they meet, there's a cycle; if fast reaches None, no cycle
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    def test_1(self):
        """Test list without cycle"""
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        print(f"Has cycle: {self.has_cycle(head)}")  # Expected: False

    def test_2(self):
        """Test list with cycle"""
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = head.next  # Create cycle
        print(f"Has cycle: {self.has_cycle(head)}")  # Expected: True


class problem_10:
    """Merge two sorted linked lists"""

    def merge_sorted(self, head1, head2):
        """
        U- Merge two sorted linked lists into one sorted list
        P- Compare nodes from each list, attach smaller node to result
        I- Use two pointers to traverse both lists, create new list with sorted nodes
        """
        dummy = Node(0)
        current = dummy

        while head1 and head2:
            if head1.value <= head2.value:
                current.next = head1
                head1 = head1.next
            else:
                current.next = head2
                head2 = head2.next
            current = current.next

        # Attach remaining nodes
        current.next = head1 if head1 else head2

        return dummy.next

    def print_list(self, head):
        """Helper to print linked list"""
        result = []
        current = head
        while current:
            result.append(str(current.value))
            current = current.next
        print(" -> ".join(result) if result else "Empty")

    def test_1(self):
        """Test merging [1, 3, 5] and [2, 4, 6]"""
        head1 = Node(1)
        head1.next = Node(3)
        head1.next.next = Node(5)

        head2 = Node(2)
        head2.next = Node(4)
        head2.next.next = Node(6)

        print("List 1:")
        self.print_list(head1)
        print("List 2:")
        self.print_list(head2)

        merged = self.merge_sorted(head1, head2)
        print("Merged:")
        self.print_list(merged)  # Expected: 1 -> 2 -> 3 -> 4 -> 5 -> 6
