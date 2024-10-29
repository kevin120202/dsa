class Solution(object):
    def diameterOfBinaryTree(self, root):
        def dfs(node, res):
            if not node:
                return 0
            
            left = dfs(node.left, res)
            right = dfs(node.right, res)

            res[0] = max(res[0], left + right)
            return max(left, right) + 1
        
        res = [0]
        dfs(root, res)
        return res[0]