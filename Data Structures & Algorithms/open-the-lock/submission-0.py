from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)

        if "0000" in dead:
            return -1

        q = deque()
        q.append(("0000", 0))

        visit = set()
        visit.add("0000")

        def children(lock):
            res = []

            for i in range(4):
                # turn wheel up
                digit = str((int(lock[i]) + 1) % 10)
                child = lock[:i] + digit + lock[i + 1:]
                res.append(child)

                # turn wheel down
                digit = str((int(lock[i]) - 1 + 10) % 10)
                child = lock[:i] + digit + lock[i + 1:]
                res.append(child)

            return res

        while q:
            lock, turns = q.popleft()

            if lock == target:
                return turns

            for child in children(lock):
                if child not in dead and child not in visit:
                    visit.add(child)
                    q.append((child, turns + 1))

        return -1