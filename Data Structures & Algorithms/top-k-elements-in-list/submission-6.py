class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
        freq=[[] for _ in range(len(nums)+1)]
        for number,frequency in count.items():
            freq[frequency].append(number)
        result=[]
        for i in range(len(freq)-1,0,-1):
            for m in freq[i]:
                result.append(m)
            if len(result)==k:
                return result
            