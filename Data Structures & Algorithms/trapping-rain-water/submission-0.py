class Solution:
    def trap(self, height: List[int]) -> int:
        if height is None: 
            return 0

        if len(height) <= 1:
            return 0

        l = len(height)
        
        left_max = [0] * l
        right_max = [0] * l

        left_max[0] = height[0]
        for i in range(1, l):
            left_max[i] = max(left_max[i-1], height[i])

        right_max[-1] = height[-1]
        for i in range(l-2, -1,-1):
            right_max[i] = max(right_max[i+1], height[i])

        trapped_water = 0
        for i in range(1, l-1):
            left_val = left_max[i]
            right_val = right_max[i]
            trapped_water += max(min(right_val, left_val) - height[i], 0)

        return trapped_water

        
