class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            st = ''.join(sorted(word))
            if st in d:
                d[st].append(word)
            else:
                d[st] = [word]
        return list(d.values())