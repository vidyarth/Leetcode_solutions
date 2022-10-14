# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n =0
        curr = head
        while(curr is not None):
            curr = curr.next
            n += 1
        if n == 1:
            return None
        k = 1
        prev = head
        curr = head.next
        while(k<n//2):
            prev = curr
            curr = curr.next
            k += 1
        prev.next = curr.next
        return head