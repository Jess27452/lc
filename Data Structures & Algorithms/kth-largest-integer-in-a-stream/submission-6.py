class KthLargest:
# for minheap, min is o(1)
#pop is logn
#turn an array into heap costs o(n)


    def __init__(self, k: int, nums: List[int]):
        #time complexityfor pop:O((n-k) log n)
        #intotal:O(n + (n-k)log n)
        #written as:O(n log n)
        self.minHeap, self.k=nums,k
        heapq.heapify(self.minHeap)
        while len(self.minHeap)>k:
            heapq.heappop(self.minHeap)
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap)>self.k:
             heapq.heappop(self.minHeap)
        return self.minHeap[0]
#We ALWAYS maintain:heap size = k
#and heap stores:k largest elements seen so far
#Therefore:smallest element in heap=kth largest overall
#Each add:

#O(log k)

#since Because heap NEVER grows beyond size k.
        
