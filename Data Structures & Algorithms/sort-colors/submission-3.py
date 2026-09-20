class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=len(nums)-1
        i=0
        def swap(a,b):
            temp=nums[a]
            nums[a]=nums[b]
            nums[b]=temp
        while i<=right:
            if nums[i]==0:
                swap(i,left)
                left+=1
                i+=1
            elif nums[i]==2:
                swap(i,right)
                right-=1
            else:
                i+=1
        

        