class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        top = 0
        bot = rows - 1
        row_found = float("inf")

        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                row_found = mid
                break

        if row_found == float("inf"):
            return False
        
        l = 0
        r = len(matrix[row_found]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row_found][mid]:
                l = mid + 1
            elif target < matrix[row_found][mid]:
                r = mid - 1
            else:
                return True
        
        return False