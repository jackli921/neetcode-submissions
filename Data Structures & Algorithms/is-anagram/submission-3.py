class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = len(s)
        l2 = len(t)
        if l1 != l2:
            return False
        c = Counter()
        for n in s:
            c[n] += 1
        print(c)
        for n in t:
            if not c[n]:
                return False
            else: 
                c[n] -= 1
            if c[n] < 0:
                return False
        return True
