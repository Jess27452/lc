from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, left_index, middle, right_index):
            # Copy the two already-sorted halves.
            left = arr[left_index : middle + 1]
            right = arr[middle + 1 : right_index + 1]

            # i writes into the original array.
            # j reads from the left list.
            # k reads from the right list.
            i = left_index
            j = 0
            k = 0

            # Compare the next values from both halves.
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1

                i += 1

            # Copy any remaining values from the left half.
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1

            # Copy any remaining values from the right half.
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        def merge_sort(arr, left_index, right_index):
            # One element is already sorted.
            if left_index >= right_index:
                return

            middle = (left_index + right_index) // 2

            # Sort the left half.
            merge_sort(arr, left_index, middle)

            # Sort the right half.
            merge_sort(arr, middle + 1, right_index)

            # Combine the two sorted halves.
            merge(arr, left_index, middle, right_index)

        merge_sort(nums, 0, len(nums) - 1)
        return nums

        #Time complexity:  O(n log n)
#Space complexity: O(n)