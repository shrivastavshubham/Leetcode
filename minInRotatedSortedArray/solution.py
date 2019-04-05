class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while (low<=high):
            mid = (high+low)/2
            if (nums[low]<=nums[high]):
                return nums[low]
            if (nums[mid]<nums[mid-1] and nums[mid]<nums[(mid+1)%len(nums)]):
                return nums[mid]
            if (nums[mid] >= nums[low]):
                low  = mid + 1
            if (nums[mid] <= nums[high]):
                high = mid -1
        return None
