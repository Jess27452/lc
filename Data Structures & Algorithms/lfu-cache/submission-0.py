from collections import defaultdict


class Node:
    def __init__(self, key: int):
        self.key = key
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        # Dummy boundary nodes
        self.left = Node(0)
        self.right = Node(0)

        self.left.next = self.right
        self.right.prev = self.left

        # Maps a key to its node in this linked list.
        self.nodes = {}

    def length(self) -> int:
        return len(self.nodes)

    def pushRight(self, key: int) -> None:
        """
        Insert key at the right side.
        Right side = most recently used.
        """
        node = Node(key)
        previous = self.right.prev

        previous.next = node
        node.prev = previous

        node.next = self.right
        self.right.prev = node

        self.nodes[key] = node

    def pop(self, key: int) -> int:
        """
        Remove a specific key from this linked list.
        """
        node = self.nodes[key]

        previous = node.prev
        next_node = node.next

        previous.next = next_node
        next_node.prev = previous

        del self.nodes[key]

        return key

    def popLeft(self) -> int:
        """
        Remove the least recently used key.
        """
        key = self.left.next.key
        return self.pop(key)


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity

        # key -> value
        self.valMap = {}

        # key -> frequency
        self.countMap = {}

        # frequency -> linked list of keys
        self.listMap = defaultdict(LinkedList)#class

        # Current minimum frequency
        self.lfuCnt = 0

    def counter(self, key: int) -> None:
        """
        Increase key's frequency by 1 and move it
        into the corresponding frequency list.
        """
        count = self.countMap[key]

        # Increase the stored frequency.
        self.countMap[key] += 1

        # Remove key from its old frequency list.
        self.listMap[count].pop(key)

        # Add key to its new frequency list.
        self.listMap[count + 1].pushRight(key)

        # If the old minimum-frequency list became empty,
        # the new minimum frequency is count + 1.
        if (
            count == self.lfuCnt
            and self.listMap[count].length() == 0
        ):
            self.lfuCnt += 1

    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1

        # Accessing this key increases its frequency.
        self.counter(key)

        return self.valMap[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        # Key already exists:
        # update its value and frequency.
        if key in self.valMap:
            self.valMap[key] = value
            self.counter(key)
            return

        # New key, but cache is full:
        # remove the LFU key.
        if len(self.valMap) == self.cap:
            least_frequent_key = (
                self.listMap[self.lfuCnt].popLeft()
            )

            del self.valMap[least_frequent_key]
            del self.countMap[least_frequent_key]

        # Add a new key with frequency 1.
        self.valMap[key] = value
        self.countMap[key] = 1
        self.listMap[1].pushRight(key)

        # A newly inserted key always has frequency 1.
        self.lfuCnt = 1    


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)