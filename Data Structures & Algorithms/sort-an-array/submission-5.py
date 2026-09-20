from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, left, middle, right):
            left_part = arr[left:middle]
            right_part = arr[middle:right]

            i = left
            j = 0
            k = 0

            while j < len(left_part) and k < len(right_part):
                if left_part[j] <= right_part[k]:
                    arr[i] = left_part[j]
                    j += 1
                else:
                    arr[i] = right_part[k]
                    k += 1

                i += 1

            while j < len(left_part):
                arr[i] = left_part[j]
                j += 1
                i += 1

            while k < len(right_part):
                arr[i] = right_part[k]
                k += 1
                i += 1

        def merge_sort(arr, left, right):
            # [left, right)
            # 0 or 1 element
            if right - left <= 1:
                return

            middle = (left + right) // 2

            merge_sort(arr, left, middle)
            merge_sort(arr, middle, right)

            merge(arr, left, middle, right)

        merge_sort(nums, 0, len(nums))

        return nums