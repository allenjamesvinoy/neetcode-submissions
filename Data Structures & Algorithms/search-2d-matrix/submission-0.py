class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS-1
        while top <= bot:
            vertical_mid = (top + bot) // 2
            if target > matrix[vertical_mid][-1]:
                top = vertical_mid+1
            elif target < matrix[vertical_mid][0]:
                bot = vertical_mid-1
            else:
                break

        if not (top <= bot): return False

        vertical_mid = (top + bot) // 2
        left, right = 0, COLS-1
        while left <= right:
            horizontal_mid = (left + right) // 2
            if target > matrix[vertical_mid][horizontal_mid]:
                left = horizontal_mid+1
            elif target < matrix[vertical_mid][horizontal_mid]:
                right = horizontal_mid-1
            else:
                return True

        return False
                    