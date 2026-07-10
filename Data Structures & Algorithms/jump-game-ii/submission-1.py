class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        j = 1
        jumps = 0
        val = nums[0]

        while j != len(nums):
            max_val = nums[j]
            while val and j < len(nums):
                val -= 1
                if nums[j] > max_val:
                    max_val = nums[j]
                j+=1
            val = max_val
            jumps += 1

        return jumps
