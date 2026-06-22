class Solution:
    def get_index(self, char) -> int:
        return ord(char) - ord('a')

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_dict = [0] * 26
        s2_dict = [0] * 26
        matches = 0

        for i in range(len(s1)):
            s1_dict[self.get_index(s1[i])] += 1
            s2_dict[self.get_index(s2[i])] += 1

        for i in range(26):
            if s1_dict[i] == s2_dict[i]:
                matches += 1

        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            char_index = self.get_index(s2[i])
            s2_dict[char_index] += 1
            if s2_dict[char_index] == s1_dict[char_index]:
                matches += 1
            elif s1_dict[char_index] + 1 == s2_dict[char_index]:
                matches -= 1
            
            char_index = self.get_index(s2[i-len(s1)])
            s2_dict[char_index] -= 1
            if s2_dict[char_index] == s1_dict[char_index]:
                matches += 1
            elif s1_dict[char_index]-1 == s2_dict[char_index]:
                matches -= 1

        return True if matches == 26 else False
