class Solution(object):
    def longestCommonPrefix(self, strs):
        # min_length_str = strs[0]
        # common_prefix = ""
        # for i in range(1, len(strs)):
        #     if len(strs[i]) < len(min_length_str):
        #         min_length_str = strs[i]
        # for i in range(len(min_length_str)):
        #     for strr in strs:
        #         if strr[i] != min_length_str[i]:
        #             return common_prefix
        #     common_prefix += min_length_str[i]
        # return common_prefix

        res = ""
        for i in range(len(strs[0])):
            for strr in strs:
                if i == len(strr) or strr[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
