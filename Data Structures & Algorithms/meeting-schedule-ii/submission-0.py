"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:


        heap = []

        for i in range(len(intervals)):
            heapq.heappush(heap, (intervals[i].start, 1))
            heapq.heappush(heap, (intervals[i].end, -1))

        ans = count = 0

        while heap:
            time, val = heapq.heappop(heap)
            count += val
            ans = max(ans, count)

        return ans


        