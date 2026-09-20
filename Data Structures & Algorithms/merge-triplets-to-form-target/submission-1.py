class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:

            # If ANY value in this triplet is larger
            # than the target at the same position,
            # we can NEVER use this triplet.
            if (
                t[0] > target[0]
                or t[1] > target[1]
                or t[2] > target[2]
            ):
                continue

            # Check which positions this triplet
            # can contribute exactly to the target.
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
#good stores which positions of the target we have successfully matched using valid triplets.
        # We need all 3 positions:
        # index 0, index 1, index 2
        return len(good) == 3 