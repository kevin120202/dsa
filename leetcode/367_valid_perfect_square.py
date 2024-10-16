class Solution(object):
    def isPerfectSquare(self, num):
        l = 1
        r = num
        while l <= r:
            mid = (l + r) // 2
            sqrt = mid * mid
            if sqrt > num:
                r = mid - 1
            elif sqrt < num:
                l = mid + 1
            else:
                return True
        
        return False