class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        
    def append(self, value: int) -> None:
        node = Node(value)
        last_node = self.tail.prev
        last_node.next = node
        node.next = self.tail
        node.prev = last_node
        self.tail.prev = node

    def appendleft(self, value: int) -> None:
        node = Node(value)
        first_node = self.head.next
        first_node.prev = node
        node.prev = self.head
        node.next = first_node
        self.head.next = node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last_node = self.tail.prev
        value = last_node.value
        prev_node = last_node.prev

        prev_node.next = self.tail
        self.tail.prev = prev_node

        return value
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first_node = self.head.next
        value = first_node.value
        next_node = first_node.next

        self.head.next = next_node
        next_node.prev = self.head

        return value
