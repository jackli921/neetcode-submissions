class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # output must index into original input to get string;
        # or whenever two matches during a comparison

        # anagrams are words with chars that have same frequency
        # dictionary captures the frequency
        # each word gets its own dict
        # array of dicts
        # two pointer compare the dicts 
        # if two matches, add the output string, but there can be more than two anagram
        # continue to scan the whole array until end
        
        # anagrams have same length
        # can group items into words of diff length
        # ["act", "cats"]
        # ["pots", "tops", "stops"]
    
        # loop through input to create array of dict
        # each dict is key by strign, value is dict

        d = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in d:
                d[sorted_word].append(word)
            else:
                d[sorted_word] = [word]

        return list(d.values())