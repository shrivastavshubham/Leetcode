class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        if K%2 ==0:return -1
        a = 1
        resDict = {}
        while True:
            temp = a%K
            if temp==0:return len(str(a))
            else:
                if temp in resDict:return -1
                resDict[temp]=1
                a = 10*a +1
        return -1
        
