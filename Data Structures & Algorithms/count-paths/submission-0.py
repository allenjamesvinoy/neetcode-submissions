class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total = m + n - 2
        k = min(m, n) - 1

        res = 1
        for i in range(1, k+1):
            res = (res * (total - i + 1)) // i

        return res