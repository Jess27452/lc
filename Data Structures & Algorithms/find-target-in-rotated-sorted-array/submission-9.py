class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if target ==nums[mid]:
                return mid
            #lef sorted portion
            if nums[l]<=nums[mid]:
                if target >nums[mid] or target< nums[l]:# we dont need euqal sgn here because we 
                #want to change the left posistion only when targte smaller than nums[l]
                    l=mid+1
                else:
                    r=mid-1
            else:
                if target <nums[mid] or target>nums[r]:
                    r=mid-1 
                else:
                    l=mid+1
        return -1

        