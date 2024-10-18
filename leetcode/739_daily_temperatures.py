class Solution(object):
    def dailyTemperatures(self, temperatures):
        temps = temperatures
        res = [0] * len(temps)
        stack = []

        for i in range(len(temps)):
            while stack and temps[stack[-1]] < temps[i]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        
        return res