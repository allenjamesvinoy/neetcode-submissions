class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        
        link_map = {}
        for num in nums:
            link_map[num] = num

        res = 1
        for num in nums: 
            lower = num-1
            higher = num+1

            linked_higher = max(higher, link_map[higher]) if higher in link_map else num
            linked_lower = min(lower, link_map[lower]) if lower in link_map else num

            if linked_higher == linked_lower or linked_higher < num or linked_lower > num:
                continue

            link_map[linked_higher] = linked_lower
            link_map[linked_lower] = linked_higher

            res = max(res, linked_higher - linked_lower + 1)

        return res