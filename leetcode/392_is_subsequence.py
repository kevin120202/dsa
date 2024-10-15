class Solution(object):
    def isSubsequence(self, s, t):
        s_ptr = 0
        t_ptr = 0
        while t_ptr < len(t):
            if s_ptr < len(s) and s[s_ptr] == t[t_ptr]:
                s_ptr += 1
            t_ptr += 1

        return s_ptr == len(s)  