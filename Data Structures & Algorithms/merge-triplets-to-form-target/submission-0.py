class Solution:
    def mergeTriplets(self, triplets, target):
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)

        return len(good) == 3

    #    Skip triplets that are too large.
#From safe triplets, collect positions that equal target.
#If we can collect index 0, 1, and 2, return True.