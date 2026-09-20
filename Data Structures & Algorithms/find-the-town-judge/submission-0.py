class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = [0] * (n + 1)
        outgoing = [0] * (n + 1)

        for src, dst in trust:
            outgoing[src] += 1
            incoming[dst] += 1

        for i in range(1, n + 1):
            if outgoing[i] == 0 and incoming[i] == n - 1:
                return i

        return -1