class Solution:

    def encode(self, strs: List[str]) -> str:
        #handle empty and null cases
        res = []
        for string in strs:
            res.append(str(len(string)))
            res.append('#')
            res.append(string)

        return "".join(res)
        
    def decode(self, s: str) -> List[str]:
        res = []
        num_str = ""
        idx = 0
        while idx < len(s):
            char = s[idx]
            idx += 1
            if char == '#':
                num = int(num_str)
                res.append(s[idx:idx+num])
                idx += num
                num_str = ""
            else:
                num_str += char

        return res