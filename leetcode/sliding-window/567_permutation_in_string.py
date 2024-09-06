class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_c = {}
        s2_c = {}

        for char in s1:
            if char in s1_c:
                s1_c[char] += 1
            else:
                s1_c[char] = 1

        for i in range(len(s1)):
            if s2[i] in s2_c:
                s2_c[s2[i]] += 1
            else:
                s2_c[s2[i]] = 1

        if s1_c == s2_c:
            return True

        for r in range(len(s1), len(s2)):
            s2_c[s2[r - len(s1)]] -= 1
            if s2_c[s2[r - len(s1)]] <= 0:
                del s2_c[s2[r - len(s1)]]

            if s2[r] in s2_c:
                s2_c[s2[r]] += 1
            else:
                s2_c[s2[r]] = 1

            if s1_c == s2_c:
                return True

        return False
