class Solution(object):
    def searchMatrix(self, nums, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(nums)-1
        if n < 0:
            return False
        m = len(nums[0])-1
        rstart = 0 ; rend=n
        cstart = 0 ; cend=m
        while rstart<=rend and cstart<=cend:
            rmid =((rend+rstart)/2); 
            cmid =((cend+cstart)/2); 
            #print "rmid =",rmid;print "rstart=",rstart; print "rend=",rend
            #print "cmid =",cmid;print "cstart=",cstart; print "cend=",cend
            #print ""
            if (nums[rmid][cmid] == target):
                return True
                # found
            elif (target < nums[rmid][cmid]):
                if (target >=nums[rmid][0]):
                    cend = cmid-1
                    rstart = rend = rmid
                else:
                    rend = rmid-1

            else:    #target >  nums[rmid][cmid]
                if target<=nums[rmid][m]:
                    rstart = rend = rmid
                    cstart = cmid +1
                else:
                    rstart = rmid+1
        return False
    
                
        
