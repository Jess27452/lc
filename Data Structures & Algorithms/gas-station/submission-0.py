class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0#gas tank amount if we start from start and travel to current station.
        start = 0#current possible starting station.

        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                start = i + 1

        return start

        #######If starting earlier already failed,
##starting later is even worse because:

#you skip some earlier gas gains
#but still must pay the same later costs
#eg: if first one is negtaive, immedietly return 0
# then later when we reach a starting at A fails before B
#if we lose a which is a postive one, we lose the gain, and need to 
# take the same loss, which is evenr worse
#so everything between A and B also fails