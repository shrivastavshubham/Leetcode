# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals,key=lambda x:x.start)
        #print intervals [0].start
        stack = []
        for  elem in intervals:
            if not len(stack):stack.append([elem.start,elem.end]);continue
            if stack[-1][1]<elem.start:stack.append ([elem.start,elem.end])
            else:
                if elem.end<stack[-1][1]:continue
                stack[-1][1]=elem.end
        return stack
                
        
        
                
            
        
