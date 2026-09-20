"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start)

        for i in range(1, len(intervals)):
            previous_end = intervals[i - 1].end
            current_start = intervals[i].start

            if current_start < previous_end:
                return False

        return True