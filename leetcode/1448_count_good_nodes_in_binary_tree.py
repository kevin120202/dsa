class Solution(object):
    def goodNodes(self, root):
        def dfs(root, max_num):
            if not root:
                return 0
            
            good = 1 if root.val >= max_num else 0 # 1
            max_num = max(max_num, root.val)
            good += dfs(root.left, max_num) # 1
            good += dfs(root.right, max_num) # 2

            return good # 4
        
        return dfs(root, root.val)