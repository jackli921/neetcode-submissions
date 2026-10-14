class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # must iterate to count freq of all numbers
        d = Counter(nums)
        
        return sorted(d, key=d.get, reverse=True)[:k]