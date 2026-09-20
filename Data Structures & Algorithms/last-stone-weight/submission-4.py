class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-s for s in stones]
        heapq.heapify(stones)
        #Python heapq is a MIN heapBUT we need:largest stones
        #So we simulate a max heap using NEGATIVE numbers.
        while len(stones)>1:
            #while len(stones) > 1:

#Keep smashing while at least 2 stones exist.
            first =heapq.heappop(stones)
            second =heapq.heappop(stones)
            if second >first:
                heapq.heappush(stones, first-second)
                #the orignila value should be second - first
                # however, we want to push negative value inside the heap

        stones.append(0)#if heap is empty:stones[0] would crash, which will
        #give IndexError
        #this line guarantees heap always has something.
        return abs(stones[0])
