class ListNode:
    def __init__(self, key=-1, next=None):
        self.key = key
        self.next = next


class MyHashSet:

    def __init__(self):
        self.set = [ListNode() for _ in range(10**4)]

    def add(self, key: int) -> None:
        cur = self.set[key % len(self.set)]

        while cur.next:
            if cur.next.key == key:# it checks every key
                return
            cur = cur.next

        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.set[key % len(self.set)]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.set[key % len(self.set)]

        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next

        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)