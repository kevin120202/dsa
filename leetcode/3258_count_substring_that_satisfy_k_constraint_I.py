class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        l = 0
        res = 0
        count_one = 0
        count_zero = 0

        for r in range(len(s)):
            if s[r] == "0":
                count_zero += 1
            else: count_one += 1        

            while count_one > k and count_zero > k:
                if s[l] == "0":
                    count_zero -= 1
                else: count_one -= 1
                l += 1
            
            res += (r - l) + 1
        
        return res