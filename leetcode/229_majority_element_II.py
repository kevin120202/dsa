from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

            if len(counter) <= 2:
                continue

            new_counter = defaultdict(int)
            for num, count in counter.items():
                if count > 1:
                    new_counter[num] = count - 1
            counter = new_counter
        
        res = []
        for key in counter:
            if nums.count(key) > len(nums) // 3:
                res.append(key)
        
        return res