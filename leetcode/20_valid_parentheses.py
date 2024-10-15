class Solution(object):
    def isValid(self, s):
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif char == ")":
                if len(stack) == 0 or stack.pop() != "(":
                    return False
            elif char == "}":
                if len(stack) == 0 or stack.pop() != "{":
                    return False
            elif char == "]":
                if len(stack) == 0 or stack.pop() != "[":
                    return False
        return len(stack) == 0
