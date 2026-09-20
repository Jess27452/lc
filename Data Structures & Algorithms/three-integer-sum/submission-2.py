from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:#skip first element if they are duplicated
                continue
                #if not wirting i>0 when first element When i = 0, Python checks if nums[0] == nums[-1].
                #contunies measn skip everything inside the loop
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    l += 1#need to check next working pair we can use use r-=1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res