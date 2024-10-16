class Solution(object):
    def sortArray(self, nums):
        if len(nums) == 1:
            return nums
        mid = int(len(nums) / 2)
        sorted_left = self.sortArray(nums[:mid])
        sorted_right = self.sortArray(nums[mid:])
        return self.merge(sorted_left, sorted_right)

    def merge(self, first, second):
        res = []
        i = 0
        j = 0
        while i < len(first) and j < len(second):
            if first[i] < second[j]:
                res.append(first[i])
                i += 1
            else:
                res.append(second[j])
                j += 1
        while i < len(first):
            res.append(first[i])
            i += 1
        while j < len(second):
            res.append(second[j])
            j += 1
        return res
    