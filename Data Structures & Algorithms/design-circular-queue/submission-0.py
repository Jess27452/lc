class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None


class MyCircularQueue:

    def __init__(self, k: int):
        # Dummy nodes marking the two ends.
        self.left = ListNode()
        self.right = ListNode()

        # Initially, there are no real nodes between them.
        self.left.next = self.right
        self.right.prev = self.left

        # Number of available positions.
        self.space = k

    def enQueue(self, value: int) -> bool:
        # Cannot add when the queue is full.
        if self.isFull():
            return False

        new_node = ListNode(value)

        # Insert new_node immediately before right.
        new_node.prev = self.right.prev
        new_node.next = self.right

        self.right.prev.next = new_node
        self.right.prev = new_node

        # One available position was used.
        self.space -= 1

        return True

    def deQueue(self) -> bool:
        # Cannot remove from an empty queue.
        if self.isEmpty():
            return False

        # Remove the first real node: left.next.
        first_node = self.left.next
        second_node = first_node.next

        self.left.next = second_node
        second_node.prev = self.left

        # One position becomes available.
        self.space += 1

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.space == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()