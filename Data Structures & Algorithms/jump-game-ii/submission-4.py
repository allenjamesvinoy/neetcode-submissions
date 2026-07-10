class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        j = 1
        jumps = 0
        scans = nums[0]
        max_reach = j + nums[j]

        while j < len(nums):
            while scans>0 and j < len(nums):
                reach = j + nums[j]
                if reach > max_reach:
                    max_reach = reach
                j+=1
                scans -= 1
            
            scans = max_reach - j + 1
            jumps += 1

        return jumps
