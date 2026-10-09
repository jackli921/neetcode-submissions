class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = Counter()
        for index, item in enumerate(nums):
            d[item] = index
        print(d)

        for i, n in enumerate(nums):
            diff = target - n
            if d[diff] > 0:
                if i != d[diff]:
                    return [i, d[diff]]