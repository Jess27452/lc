from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.count = n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]

        return x

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            px, py = py, px

        self.parent[py] = px
        self.rank[px] += self.rank[py]
        self.count -= 1

        return True


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        # Special case:
        # If there is only one number, we can trivially reach it.
        if len(nums) == 1:
            return True

        # If nums contains 1 and there is more than one number,
        # gcd(1, anything) = 1, so 1 cannot connect to anyone.
        if 1 in nums:
            return False

        uf = UnionFind(len(nums))

        # prime factor -> index of a number that contains this factor
        factor_index = {}

        for i, n in enumerate(nums):

            # Try possible prime factors starting from 2
            f = 2

            while f * f <= n:

                if n % f == 0:

                    # If another number already had factor f,
                    # connect current number with that number.
                    if f in factor_index:
                        uf.union(i, factor_index[f])

                    # Otherwise remember this index.
                    else:
                        factor_index[f] = i

                    # Remove all copies of factor f
                    while n % f == 0:
                        n //= f

                f += 1

            # If n > 1, then n itself is a remaining prime factor
            if n > 1:

                if n in factor_index:
                    uf.union(i, factor_index[n])

                else:
                    factor_index[n] = i

        # All numbers must belong to one connected component
        return uf.count == 1