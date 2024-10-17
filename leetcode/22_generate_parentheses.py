class Solution(object):
    def generateParenthesis(self, n):
        # only add open paren if open < n
        # only add a closing paren if close < open
        # valid if open == close == n

        stack = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
        
        backtrack(0,0)
        return res