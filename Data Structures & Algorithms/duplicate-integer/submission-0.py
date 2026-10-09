class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        same_len = len(s) == len(nums)
        return not same_len