class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        j = 1
        jumps = 0
        val = nums[0]
        max_val = j + nums[j]

        while j < len(nums):
            while val>0 and j < len(nums):
                if (j + nums[j]) > max_val:
                    max_val = j + nums[j]
                j+=1
                val -= 1
            
            val = max_val - j + 1
            jumps += 1

        return jumps
