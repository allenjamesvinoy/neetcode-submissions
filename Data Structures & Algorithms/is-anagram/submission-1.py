class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
            
        dict_s = defaultdict(int)
        dict_t = defaultdict(int)

        for c in s:
            dict_s[c] += 1

        for c in t:
            dict_t[c] += 1

        res = True
        for k,v in dict_s.items():
            if not (k in dict_t and v == dict_t[k]):
                res = False
                break

        return res

