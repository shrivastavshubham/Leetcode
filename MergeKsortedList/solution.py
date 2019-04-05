from heapq import heappush, heappop
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        i = 1
        while i < amount:
            for j in range(0, amount - i, i * 2):
                lists[j] = self.merge2List(lists[j], lists[j + i])
            i *= 2
        return lists[0] if amount > 0 else lists
            
    def merge2List(self,node1,node2):
        head = point = ListNode(0)
        while node1 != None and node2 != None:
            if node1.val<node2.val:point.next = node1 ; node1 = node1.next
            else:point.next = node2 ; node2 = node2.next
            point = point.next
        if node1:point.next = node1
        if node2:point.next = node2
        return head.next
