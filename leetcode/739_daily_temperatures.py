class Solution(object):
    def dailyTemperatures(self, temperatures):
        temps = temperatures
        n = len(temps)
        res = [0] * n
        stack = []

        for i, t in enumerate(temps):
            while stack and stack[-1][0] < t:
                stack_t, stack_i = stack.pop()
                res[stack_i] = i - stack_i
            
            stack.append((t, i))
        
        return res