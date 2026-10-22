class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # intuition: the samller the value, the longer the potential chain
        # check if a lower number exists in the list
            # if so, add to cur len; repeat
        # update longest record

        seen = set(nums)
        longest = 0

        for n in seen:
            if n - 1 not in seen:
                length = 1
                while n + length in seen:
                    length += 1
                longest = max(longest, length)
        return longest