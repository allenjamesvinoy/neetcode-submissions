class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix_prod = [1] * l
        suffix_prod = [1] * l

        for i in range(1, l):
            prefix_prod[i] = prefix_prod[i-1] * nums[i-1]

        for i in range(l-2, -1, -1):
            suffix_prod[i] = suffix_prod[i+1] * nums[i+1]

        print(prefix_prod)
        print(suffix_prod)
        out = [1] * l

        for i in range(l):
            out[i] = prefix_prod[i] * suffix_prod[i]

        return out