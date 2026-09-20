from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        # Find possible candidates.
        for number in nums:
            count[number] += 1

            # There can be at most two majority elements.
            if len(count) <= 2:
                continue

            # Three different candidates currently exist,
            # so subtract one occurrence from each candidate.
            new_count = defaultdict(int)

            for candidate, frequency in count.items():
                if frequency > 1:
                    new_count[candidate] = frequency - 1

            count = new_count

        # Verify the remaining candidates.
        result = []

        for candidate in count:
            if nums.count(candidate) > len(nums) // 3:
                result.append(candidate)

        return result