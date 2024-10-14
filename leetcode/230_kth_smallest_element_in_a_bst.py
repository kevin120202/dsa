class Solution(object):
    def kthSmallest(self, root, k):
        inordered_list = []
        def dfs(node):
            if node.left:
                dfs(node.left)
            inordered_list.append(node.val)
            if node.right:
                dfs(node.right)

        dfs(root)
        return inordered_list[k-1]   