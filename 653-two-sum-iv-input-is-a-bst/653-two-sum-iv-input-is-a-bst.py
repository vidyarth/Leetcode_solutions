# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []
        def inorder(root):
            nonlocal arr
            if root is None:
                return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        inorder(root)
        low = 0
        high = len(arr)-1
        while(low < high):
            t = arr[low] + arr[high]
            if t == k:
                return True
            if t > k:
                high -= 1
            else:
                low += 1
        return False