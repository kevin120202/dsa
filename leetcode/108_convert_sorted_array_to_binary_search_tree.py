from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def createBST(l, r):
            # Base case: for when the range is out of bounds
            if l > r:
                return None
            
            # Find the middle index to use as the root
            mid = (l + r) // 2

            # Initializing the root with the middle index
            root = TreeNode(nums[mid])

            # Setting the left child of the root and the right child of the root
            root.left = createBST(l, mid - 1)
            root.right = createBST(mid + 1, r)

            return root
        
        return createBST(0, len(nums)-1)