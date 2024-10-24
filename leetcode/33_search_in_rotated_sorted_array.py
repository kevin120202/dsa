class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1


# class Solution(object):
#     def search(self, nums, target):
#         l = 0
#         r = len(nums) - 1
#         while l <= r:
#             mid = (l + r) // 2
#             if nums[mid] == target:
#                 return mid
            
#             if nums[mid] >= nums[l]:
#                 if target >= nums[l] and target < nums[mid]:
#                     r = mid - 1
#                 else:
#                     l = mid + 1
#             else:
#                 if target > nums[mid] and target <= nums[r]:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
        
#         return -1