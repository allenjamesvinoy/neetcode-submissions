class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        i = 0
        j = i+1
        jumps = 0
        val = nums[i]

        while j != len(nums):
            max_val = nums[j]
            while val and j < len(nums):
                val -= 1
                if nums[j] > max_val:
                    i = j
                    max_val = nums[j]
                j+=1
            val = max_val
            jumps += 1

        return jumps
