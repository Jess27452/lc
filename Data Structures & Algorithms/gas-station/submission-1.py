class Solution:
    def canCompleteCircuit(self, gas, cost):
        # If total gas is less than total cost,
        # completing the circle is impossible.
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0

        for i in range(len(gas)):
            # Gas gained - gas needed to leave this station
            total += gas[i] - cost[i]

            # If total becomes negative, our current
            # starting station cannot work.
            if total < 0:
                total = 0

                # Try starting at the NEXT station.
                res = i + 1

        return res