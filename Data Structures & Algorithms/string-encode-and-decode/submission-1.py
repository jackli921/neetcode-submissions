class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        #find # mark
        #slice i to j to get step 
        #move i to j
        # slice from i to i + step
        # move i to end of step

        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                print(s[j], i, j)
                j+= 1
            step = int(s[i:j])
            i = j + 1
            res.append(s[i:i+step])
            i += step

        return res