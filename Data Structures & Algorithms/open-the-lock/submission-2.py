from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)

        if "0000" in deadends:
            return -1

        q = deque([("0000", 0)])
        visit = set(["0000"])

        def children(lock):
            res = []

            for i in range(4):
                # turn up
                digit = str((int(lock[i]) + 1) % 10)
                a = lock[:i] + digit + lock[i + 1:]
                res.append(a)

                # turn down
                digit = str((int(lock[i]) - 1 + 10) % 10)
                b = lock[:i] + digit + lock[i + 1:]
                res.append(b)

            return res

        while q:
            lock, turns = q.popleft()

            if lock == target:
                return turns

            for child in children(lock):
                if child not in visit and child not in dead:
                    visit.add(child)
                    q.append((child, turns + 1))

        return -1