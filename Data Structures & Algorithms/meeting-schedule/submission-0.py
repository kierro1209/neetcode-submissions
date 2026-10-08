"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        schedule = []
        for interval in intervals:
            if not schedule or schedule[-1][1] <= interval.start:
                schedule.append([interval.start,interval.end])
            else:
                return False
        return True