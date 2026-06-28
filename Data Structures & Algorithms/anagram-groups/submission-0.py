class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count_key = [0] * 26

            for c in s:
                count_key[ord(c) - ord('a')] += 1

            res[tuple(count_key)].append(s)

        return list(res.values())