class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums is None or len(nums) == 0:
            return []

        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == num:
                continue

            l = i+1
            r = len(nums) - 1

            while l < r:
                curr_sum = num + nums[l] + nums[r]

                if curr_sum == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1 
                elif curr_sum > 0:
                    r -= 1
                else:
                    l += 1

        return res