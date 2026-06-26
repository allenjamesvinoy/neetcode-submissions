class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums is None:
            return -1000

        l = 0
        r = len(nums)-1

        if nums[l] < nums[r]:
            return nums[l]

        while nums[l] > nums[r]:
            mid = (l+r)//2
            if nums[l] <= nums[r]:
                return nums[l]
            elif nums[mid] > nums[r]:
                l = mid+1
            elif nums[l] > nums[mid]:
                r = mid

        
        return nums[l]

