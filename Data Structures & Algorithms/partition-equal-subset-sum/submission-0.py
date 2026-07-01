class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
    
        target = sum_nums // 2

        sum_set = set()
        sum_set.add(0)
        sum_set.add(nums[-1])
        for i in range(len(nums)-2, -1, -1):
            new_sum_set = set()
            for sum_val in sum_set:
                if sum_val == target:
                    return True
                if nums[i] + sum_val == target:
                    return True
                
                new_sum_set.add(sum_val)
                new_sum_set.add(sum_val + nums[i])

            sum_set = new_sum_set

        return True if target in sum_set else False