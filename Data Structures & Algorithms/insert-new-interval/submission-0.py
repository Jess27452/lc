from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):

            # Case 1:
            # newInterval comes before current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
                #need to use [i:] because for example:intervals =[[1,2],[5,7],[8,10]]
                #newInterval =[3,4]
            # Case 2:
            # newInterval comes after current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # Case 3:
            # overlap, so merge
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        # If newInterval was never added, add it at the end
        res.append(newInterval)
        #That final line handles BOTH:

#interval belongs at end:[[1,2],[5,7],[10,12]]
#merged interval still needs insertion after loop ends
#intervals =[[1,2],[5,7]]newInterval =[6,10]

        return res