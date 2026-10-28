class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for word in strs:
            s_word = ''.join(sorted(word))
            seen[s_word].append(word)
        res = []
        for index, (key, value) in enumerate(seen.items()):
            res.append(value)
        return res