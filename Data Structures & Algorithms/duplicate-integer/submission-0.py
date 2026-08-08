class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = defaultdict(bool)

        for i in nums:
            if i in nums_dict and nums_dict[i]:
                return True
            
            nums_dict[i] = True

        return False

