class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals):
        # Sort meetings by start time
        intervals.sort(key=lambda i: i.start)

        # Compare each meeting with the previous meeting
        for i in range(1, len(intervals)):
            prev = intervals[i - 1]
            curr = intervals[i]

            # If previous meeting ends after current meeting starts,
            # they overlap, so cannot attend all meetings
            if prev.end > curr.start:
                return False

        # No overlaps found
        return True