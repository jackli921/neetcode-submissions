class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = len(s)
        l2 = len(t)
        if l1 != l2:
            return False

        s1 = sorted(s)
        s2 = sorted(t)

        for i in range(l1):
            if s1[i] != s2[i]:
                return False
        return True
