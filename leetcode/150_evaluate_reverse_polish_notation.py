class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in "+-*/":
                val_1 = stack.pop()
                val_2 = stack.pop()
                if token == "+":
                    stack.append(val_1 + val_2)
                elif token == "/":
                    stack.append(int(float(val_2) / val_1))
                elif token == "*":
                    stack.append(val_2 * val_1)
                elif token == "-":
                    stack.append(val_2 - val_1)
            else:
                stack.append(int(token))

        return stack[0]