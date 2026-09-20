import heapq

class Solution:
    def isNStraightHand(self, hand, groupSize):
        
        # Total cards must be divisible by groupSize
        if len(hand) % groupSize:
            return False

        count = {}

        # Count how many of each card we have
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        # Put every UNIQUE number into a min-heap
        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            # Always start a group from the smallest card
            first = minH[0]

            # Need:
            # first, first+1, first+2, ...
            for i in range(first, first + groupSize):

                # Missing one required card
                if i not in count:
                    return False

                # Use one copy
                count[i] -= 1

                # No copies of i left
                if count[i] == 0:

                    # i MUST currently be the smallest remaining card
                    if i != minH[0]:
                        return False

                    heapq.heappop(minH)

        return True