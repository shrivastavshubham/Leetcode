"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        return self.dfs(node,{})
        
    def dfs (self,A,resDict):
        if A in resDict:return resDict[A]
        a = A.val
        res = Node(a,[])
        resDict[A]=res
        for nei in A.neighbors:
            res.neighbors.append(self.dfs(nei,resDict))
        return res
            
        
        
