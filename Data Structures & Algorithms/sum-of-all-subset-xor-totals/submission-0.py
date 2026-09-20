class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            res = res | n

        return res * 2**(len(nums) - 1)    
        #res = which binary bits can possibly contribute?
#2^(n-1) = how many subset XORs contain each contributing bit?