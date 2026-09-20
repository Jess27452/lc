class Solution:
    #the tiome compelxity is O(n) because the ranges never overlap.
    def jump(self, nums: List[int]) -> int:
        res = 0#number of jumps used.
        l = r = 0#current range of indexes you can reach using res jumps

        while r < len(nums) - 1:
            farthest = 0

            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
                #the farthest index you can reach using one more jump.

# change to next window
            l = r + 1
            r = farthest
            res += 1

        return res

    #[l, r]all indexes reachable using exactly res jumps.
    #at each layer: we choose the farthest reachable next boundary
    #We do NOT try all paths individually.

#That’s why time complexity becomes:

#O(n)