class MyQueue:

    def __init__(self):
        # s1 receives newly pushed elements.
        self.s1 = []

        # s2 stores elements in queue-removal order.
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        # Only transfer when s2 is empty.
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2.pop()

    def peek(self) -> int:
        # Make sure the oldest element is available in s2.
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2    


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()