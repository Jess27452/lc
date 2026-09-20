class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr,left,middle,right):
            leftp=arr[left:middle+1]
            rightp=arr[middle+1:right+1]
            i=left
            j=0
            k=0
            while j<len(leftp) and k <len(rightp):
                if leftp[j]<=rightp[k]:
                    arr[i]=leftp[j]
                    j+=1
                else:
                    arr[i]=rightp[k]
                    k+=1
                i+=1
            while j < len(leftp):
                arr[i] = leftp[j]
                j += 1
                i += 1

            # Copy any remaining values from the right half.
            while k < len(rightp):
                arr[i] = rightp[k]
                k += 1
                i += 1
        def mergesort(arr,left,right):
            if left>=right:
                return
            middle=(left+right)//2
            mergesort(arr,left,middle)
            mergesort(arr,middle+1,right)
            merge(arr,left,middle,right)
        mergesort(nums,0, len(nums)-1)
        return nums