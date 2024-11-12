class Solution(object):
    def hasPathSum(self, root, targetSum):
        def dfs(root, curr_sum):
            if not root:
                return False
            
            curr_sum += root.val
            if not root.left and not root.right:
                return curr_sum == targetSum

            left = dfs(root.left, curr_sum)
            right = dfs(root.right, curr_sum)

            return left or right
        
        return dfs(root, 0)