class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # loop through each word
        # sort the string 
        # insert the word into the array owend by the sorted key in the response dict
        # return the array of keys from dict
        seen = {}
        for word in strs:
            s_word = ''.join(sorted(word))
            if s_word not in seen:
                seen[s_word] = []
            seen[s_word].append(word)
        
        return list(seen.values())