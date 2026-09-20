class ListNode:
    def __init__(self, key=-1, value=-1, next_node=None):
        self.key = key
        self.value = value
        self.next = next_node




class MyHashMap:

    def __init__(self):
        self.map=[ListNode() for _ in range(1000)]
    def hash(self, key: int) -> int:
        # Decide which bucket the key belongs to.
        return key % len(self.map)
    def put(self, key: int, value: int) -> None:
        # Start at the dummy node of the correct bucket.
        cur = self.map[self.hash(key)]

        # Search every node in this bucket.
        while cur.next:
            # If the key already exists, update its value.
            if cur.next.key == key:
                cur.next.value = value
                return

            cur = cur.next

        # The key does not exist, so add a new node.
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.map[self.hash(key)]

        # Search every node in this bucket.
        while cur:
            if cur.key == key:
                return cur.value

            cur = cur.next

        # The key does not exist.
        return -1

    def remove(self, key: int) -> None:
        
        # Start at the dummy node so that we can access
        # the node before the node we may remove.
        cur = self.map[self.hash(key)]

        while cur.next:
            if cur.next.key == key:
                # Skip the node containing the key.
                cur.next = cur.next.next
                return

            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)