class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create buckets of len + 1
        buckets = [ [] for _ in range(len(nums)+1)]
        freq = {}

        # put input in a dict with count
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] = freq.get(n) + 1

        # count is index of bucket, insert the key (number) into the array

        for key, value in freq.items():
            buckets[value].append(key)
        

        res = []
        for i in range(len(buckets)-1, -1, -1):
                for n in buckets[i]:
                    res.append(n)
                    if len(res) == k:
                        return res

        # reverse loop k times to return the values in output