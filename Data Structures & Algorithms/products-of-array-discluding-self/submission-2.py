class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # calculate all products to the left using prefix
        # multiply allr ight witht he existing array

        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]

        return res