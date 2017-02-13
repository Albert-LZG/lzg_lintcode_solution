intervals = [[1,5]]
newInterval = [2,3]
# # write your code here
# num = len(intervals)
# head = 0
# tail = num
# _insert = [newInterval[0], newInterval[1]]
# if num == 0:
#     results.append(newInterval)
# for i in range(num):
#     if newInterval[0] > intervals[i][1]:
#         head += 1
#     if newInterval[1] < intervals[num-1-i][0]:
#         tail -= 1
# if head == tail:
#     intervals.insert(head, newInterval)
#     results =  intervals[:]
# else:
#     left = min(newInterval[0], intervals[head][0])
#     right = max(newInterval[1], intervals[tail-1][1])
#     newInterval = [left, right]
#     for i in range(head, tail):
#         del intervals[i]
#     intervals.insert(head, newInterval)
#     results =  intervals[:]
# print results

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self[0] = start
        self[1] = end
"""


class Solution:
    """
    Insert a new interval into a sorted non-overlapping interval list.
    @param intevals: Sorted non-overlapping interval list
    @param newInterval: The new interval.
    @return: A new sorted non-overlapping interval list with the new interval.
    """
    def insert(self, intervals, newInterval):
        results = []
        # write your code here
        num = len(intervals)
        head = 0
        tail = num
        _insert = [newInterval[0], newInterval[1]]
        if num == 0:
            results.append(newInterval)
            return results
            
        for i in range(num):
            if newInterval[0] > intervals[i][1]:
                head += 1
            if newInterval[1] < intervals[num-1-i][0]:
                tail -= 1
                
        if head == tail:
            intervals.insert(head, newInterval)
            results =  intervals[:]
            return results
            
        else:
            left = min(newInterval[0], intervals[head][0])
            right = max(newInterval[1], intervals[tail-1][1])
            newInterval = [left, right]
            for i in range(head, tail):
                del intervals[i]
            intervals.insert(head, newInterval)
            results =  intervals[:]
            return results

a = Solution()
print a.insert( intervals, newInterval)

