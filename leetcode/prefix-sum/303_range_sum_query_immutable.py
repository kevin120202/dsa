class NumArray(object):

    def __init__(self, nums):
        self.my_list = []
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            self.my_list.append(curr)

    def sumRange(self, left, right):
        leftSum = self.my_list[left-1] if left > 0 else 0
        return self.my_list[right] - leftSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
