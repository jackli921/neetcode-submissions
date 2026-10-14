class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [ [] for _ in range(len(nums)+1)]
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for item, freq in count.items():
            buckets[freq].append(item)

        res = []
        for i in range(len(buckets)-1, -1, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
                    
