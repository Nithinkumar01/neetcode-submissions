class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.left = Node(0, 0)   # LRU side
        self.right = Node(0, 0)  # MRU side

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def insert(self, node):
        # Insert node just before right
        prev = self.right.prev
        next = self.right

        prev.next = node
        node.prev = prev

        node.next = next
        next.prev = node

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move this node to MRU position
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            # Remove old node
            self.remove(self.cache[key])

        # Create new node
        node = Node(key, value)

        # Store in hashmap
        self.cache[key] = node

        # Put at MRU position
        self.insert(node)

        # Check capacity
        if len(self.cache) > self.capacity:

            # Remove LRU node
            lru = self.left.next

            self.remove(lru)

            # Remove from hashmap
            del self.cache[lru.key]