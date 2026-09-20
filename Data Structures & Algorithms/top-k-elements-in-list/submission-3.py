from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for number in nums:
            count[number] = count.get(number, 0) + 1

        sorted_numbers = sorted(
            count.keys(),
            key=lambda number: count[number],
            reverse=True
        )

        return sorted_numbers[:k]