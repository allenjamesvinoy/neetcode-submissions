class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c:set() for word in words for c in word }

        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]
            min_len = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:min_len] == word2:
                return ""

            for i in range(0, min_len):
                if word1[i] != word2[i]:
                    adj[word1[i]].add(word2[i])
                    break

        
        in_path = {}

        res = []
        def dfs(c):
            if c in in_path:
                return in_path[c] #cycle

            in_path[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True

            in_path[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)