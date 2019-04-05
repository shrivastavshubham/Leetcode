class Solution(object):
    def trap(self, A):
        """
        :type height: List[int]
        :rtype: int"""
        l_wall = r_wall = 0
        l=0 ; r = len(A)-1 ; water = 0
        while l<r:
            if A[l]<A[r]:
                if A[l]>l_wall:l_wall = A[l]
                else:water += l_wall-A[l]
                l+=1
            else:
                if A[r]>r_wall:r_wall = A[r]
                else:water += r_wall - A[r]
                r-=1
        return water
    
    
    
    
            
        
