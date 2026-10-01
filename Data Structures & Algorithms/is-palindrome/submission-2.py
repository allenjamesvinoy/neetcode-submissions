class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_str = ""
        for c in s:
            if c.isalnum():
                alnum_str+=c

        s = alnum_str.lower()
        print(s)
        l = 0
        r = len(s)-1

        if len(s) == 0:
            return True
        if len(s) == 1:
            return True

        while s[l]==s[r] and l<r:
            print(l, " ", r)
            l += 1
            r -= 1

        print(l, " ", r)
        return l>=r
        