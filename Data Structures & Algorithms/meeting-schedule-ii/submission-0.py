class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals):

        # Get all start times and sort them
        start = sorted([i.start for i in intervals])
        #eg [0,5,15]

        # Get all end times and sort them
        end = sorted([i.end for i in intervals])

        # res = maximum rooms needed
        # count = current rooms being used
        res = 0
        count = 0

        # s pointer for start array
        # e pointer for end array
        s = 0
        e = 0

        # Process all meetings
        while s < len(intervals):

            # If next meeting starts BEFORE
            # earliest meeting ends,
            # need another room
            if start[s] < end[e]:
                count += 1
                s += 1
#########once all meetings have started,
###no NEW rooms can ever be needed
#######so we can stop after processing all time in the start, even tehre
# are remainings in the end array
            # Otherwise a meeting ended,
            # so free one room
            else:
                count -= 1
                e += 1

            # Update maximum rooms needed
            res = max(res, count)

        return res