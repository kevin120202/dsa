from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        res = 0
        while l <= r:
            remaining = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remaining - people[l] >= 0:
                l += 1

        return res