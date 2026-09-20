class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda i: i[0])
        # it means take i, return i[0]
        #this equals to def func(i):return i[1]
        output = [intervals[0]]
        for start, end in intervals[1:]:
            #last one lastend in that interval
            lastEnd = output[-1][1]
            #this means the current inetrval is overlallping with the interval
            # in the output
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)

            else:
                output.append([start, end])

        return output