class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numDict = {}
        for i in range(0,len(nums)):
            if target-nums[i] in numDict:
                return [i,numDict[target-nums[i]]]
            else:
                numDict[nums[i]]=i
        
