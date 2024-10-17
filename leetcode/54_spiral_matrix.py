class Solution(object):
    def spiralOrder(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, -1
        direction = 1
        res = []

        while rows > 0 and cols > 0:
            for _ in range(cols):
                col += direction
                res.append(matrix[row][col])
            rows -= 1

            for _ in range(rows):
                row += direction
                res.append(matrix[row][col])
            cols -= 1

            direction *= -1
        
        return res



        # m, n = len(matrix), len(matrix[0])
        # res = []
        # i, j = 0, 0
        # UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
        # direction = RIGHT

        # UP_WALL = 0
        # RIGHT_WALL = n
        # DOWN_WALL = m
        # LEFT_WALL = -1

        # while len(res) != m*n:
        #     if direction == RIGHT:
        #         while j < RIGHT_WALL:
        #             res.append(matrix[i][j])
        #             j += 1
        #         i, j = i+1, j-1
        #         RIGHT_WALL -= 1
        #         direction = DOWN
        #     elif direction == DOWN:
        #         while i < DOWN_WALL:
        #             res.append(matrix[i][j])
        #             i += 1
        #         i, j = i-1, j-1
        #         DOWN_WALL -= 1
        #         direction = LEFT
        #     elif direction == LEFT:
        #         while j > LEFT_WALL:
        #             res.append(matrix[i][j])
        #             j -= 1
        #         i, j = i-1, j+1
        #         LEFT_WALL += 1
        #         direction = UP
        #     else:
        #         while i > UP_WALL:
        #             res.append(matrix[i][j])
        #             i -= 1
        #         i, j = i+1, j+1
        #         UP_WALL += 1
        #         direction = RIGHT
            
        # return res