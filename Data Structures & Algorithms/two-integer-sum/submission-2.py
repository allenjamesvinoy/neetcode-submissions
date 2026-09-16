class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_idx_map = {}
        for idx, num in enumerate(nums):
            value_idx_map[num] = idx

        for idx, num in enumerate(nums):
            search_val = target - num
            if search_val in value_idx_map and idx != value_idx_map[search_val]:
                return [idx, value_idx_map[search_val]]