class Solution:
    def insert(
        self,
        intervals: List[List[int]],
        newInterval: List[int]
    ) -> List[List[int]]:

        res = []

        for i in range(len(intervals)):

            # Case 1: newInterval is completely before intervals[i]
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            # Case 2: newInterval is completely after intervals[i]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # Case 3: they overlap
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]

        res.append(newInterval)
        return res