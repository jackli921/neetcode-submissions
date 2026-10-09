class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        s = set()
        for i,n in enumerate(nums):
            d[n] = i
        for i,n in enumerate(nums):
            diff = target - n
            other = d.get(diff, -1)
            if other >= 0 and i != other:
                return [i, other]