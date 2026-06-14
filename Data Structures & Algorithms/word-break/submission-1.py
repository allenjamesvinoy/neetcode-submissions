class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s is None:
            return False
        
        if wordDict is None or len(wordDict) == 0: 
            return False

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i : i + len(word)] == word: 
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break

        return dp[0]