from typing import List
class Solution:
    def numRescueBoats(
        self,
        people: List[int],
        limit: int
    ) -> int:
        people.sort()

        left = 0
        right = len(people) - 1
        boats = 0

        while left <= right:
            # The heaviest remaining person always takes a boat.
            remaining_capacity = limit - people[right]
            right -= 1
            boats += 1

            # Try to put the lightest person on the same boat.
            if left <= right and people[left] <= remaining_capacity:
                left += 1

        return boats