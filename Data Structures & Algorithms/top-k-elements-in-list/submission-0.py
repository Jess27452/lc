class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for a in nums:
            freq[a] = freq.get(a, 0) + 1
        
        # 2) Bucket sort by frequency
        # buckets[i] = list of numbers that appear exactly i times
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)
        
        # 3) Collect from highest frequency down until we have k
        res = []
        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                res.append(num)
                if len(res) == k:
                    return res