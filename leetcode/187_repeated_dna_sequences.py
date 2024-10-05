class Solution(object):
    def findRepeatedDnaSequences(self, s):
        seen, res = set(), set()
        for l in range(len(s) - 9):
            curr = s[l:l + 10]
            if curr in seen:
                res.add(curr)
            seen.add(curr)
        
        return list(res)


        # if len(s) < 10:
        #     return 

        # l = 0
        # res = []
        # hash_count = {}

        # char_arr = []
        # for r in range(10):
        #     char_arr.append(s[r])

        # hash_count["".join(char_arr)] = ["".join(char_arr)]
        
        # for r in range(10, len(s)):
        #     char_arr.remove(s[l])
        #     char_arr.append(s[r])
        #     l += 1
        #     joined_str = "".join(char_arr)
        #     if joined_str in hash_count:
        #         hash_count[joined_str].append(joined_str)
        #     else:
        #         hash_count[joined_str] = [joined_str]

        # for key in hash_count:
        #     if len(hash_count[key]) > 1:
        #         res.append(hash_count[key][0])

        
        # return res
    