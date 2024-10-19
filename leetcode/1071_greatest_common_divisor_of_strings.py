class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1: return ""
        s1 = len(str1)
        s2 = len(str2)

        while s2:
            temp = s2
            s2 = s1 % s2
            s1 = temp
        
        return str1[:s1]