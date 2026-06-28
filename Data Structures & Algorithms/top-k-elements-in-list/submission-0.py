class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num] += 1

        for num, c in count.items():
            freq[c].append(num)
        
        res = []
        idx = len(nums)
        while k:
            if len(freq[idx]) > 0:
                k -= len(freq[idx])
                for i in freq[idx]:
                    res.append(i)
            idx -= 1 

        return res
        