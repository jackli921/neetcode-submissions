class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        # get freq of num in a dict
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # insert num and freq into bucket
        # key = num; value = freq
        # loop through key, value 
        for item, freq in freq.items():
            buckets[freq].append(item)

        res = []
        # return the top k 
        for i in range(len(buckets)-1,-1,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return []