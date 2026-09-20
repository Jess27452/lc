from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # freq[i] stores numbers that appear exactly i times.
        freq = [[] for _ in range(len(nums) + 1)]

        # Count how many times each number appears.
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Put each number into the bucket matching its frequency.
        for number, frequency in count.items():
            freq[frequency].append(number)

        result = []

        # Search frequencies from largest to smallest.
        for frequency in range(len(freq) - 1, 0, -1):
            for number in freq[frequency]:
                result.append(number)

                if len(result) == k:
                    return result
       # Time complexity: O(n)
       # Space complexity: O(n)