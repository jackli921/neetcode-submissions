class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1, t1 = len(s), len(t)
        if s1 != t1:
            return False
        
        d = {}
        for i in range(s1):
            if s[i] in d:
                d[s[i]] = d[s[i]]+1
            else:
                d[s[i]] = 1
            if t[i] in d:
                d[t[i]] = d[t[i]]-1
            else:
                d[t[i]] = -1
        return all(v == 0 for v in d.values())