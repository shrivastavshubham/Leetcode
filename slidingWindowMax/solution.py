from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        deq = deque();res = []
        for i in range(k):
            while deq and nums[deq[-1]] <= nums[i]:
                deq.pop()
            deq.append(i)
        for i in range(k,len(nums)):
            res.append(nums[deq[0]])
            while deq and deq[0]<= i-k:
                deq.popleft()
            while deq and nums[deq[-1]]<=nums[i]:
                deq.pop()
            deq.append(i)
        if deq:res.append(nums[deq[0]])
        return res
                
            
        
        
