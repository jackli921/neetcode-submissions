class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # put item in set
        # loop and check if current item -1 is in set
            # if no, smallest number found
                # set longest = 1
                # while cur + longest in set
                # longest += 1
            # if yes, go to next one
        found = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in found:
                length = 1
                while (n + length) in found:
                    length += 1
                longest = max(length, longest)        
        return longest