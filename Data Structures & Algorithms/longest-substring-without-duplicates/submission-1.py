class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1

        left = 0
        right = 1

        freq = {}
        freq[s[left]] = True

        max_val = 1
        while right < len(s):
            if s[right] in freq and freq[s[right]]:
                freq[s[left]] = False
                left += 1
            else:
                max_val = max(max_val, right-left+1)
                freq[s[right]] = True
                right += 1

        return max_val
