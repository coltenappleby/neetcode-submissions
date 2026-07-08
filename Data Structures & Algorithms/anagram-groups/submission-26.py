class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for s in strs:
            sorted_word = ''.join(sorted(s))
            if sorted_word not in words:
                words[sorted_word] = [s]
            else:
                words[sorted_word].append(s)
        return list(words.values())
