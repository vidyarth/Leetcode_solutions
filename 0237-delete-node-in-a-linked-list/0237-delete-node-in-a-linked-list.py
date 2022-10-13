# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = node
        node = node.next
        while(node is not None):
            prev.val = node.val
            if node.next == None:
                prev.next = None
            else:
                prev = node;
            node = node.next