class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache  = {}
        self.size = 0

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove_node(node)
        self._add_to_head(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove_node(node)
            node.val = value
            self._add_to_head(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            self.size += 1

            if self.size > self.capacity:
                lru_node = self.tail.prev
                self.cache.pop(lru_node.key)
                self._remove_node(lru_node)
                self.size -= 1
                

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node
        
