class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        r = 0
        res = nums[0]
        curr_sum = 0
        while r < len(nums):
            if curr_sum >= 0:
                curr_sum += nums[r]
            else:
                curr_sum = nums[r]

            r += 1
            res = max(res, curr_sum)

        return res


