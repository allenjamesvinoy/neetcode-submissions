class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        res = False
        l = len(nums)

        jump_target = l-1
        for i in range(l-2, -1, -1):
            if nums[i] >= (jump_target - i):
                jump_target = i
                res = True
            else:
                res = False

        return res
