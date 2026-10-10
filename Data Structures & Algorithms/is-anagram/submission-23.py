class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1, t1 = len(s), len(t)
        if s1 != t1:
            return False
        
        d = {}
        for i in range(s1):
            d[s[i]] = d.get(s[i], 0) + 1
            d[t[i]] = d.get(t[i], 0) - 1
        return all(v == 0 for v in d.values())