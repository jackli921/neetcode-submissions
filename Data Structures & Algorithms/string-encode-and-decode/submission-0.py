class Solution:

    def encode(self, strs: List[str]) -> str:
        # use length and # to delimit the word
        # create string by appending char to the output string
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i= 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+= 1
            length = int(s[i:j])
            i = j + 1
            res.append(s[i:i+length])
            i += length
        print(res)
        return res