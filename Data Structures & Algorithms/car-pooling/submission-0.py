from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Locations are between 0 and 1000.
        # pass_change[i] stores how the number of passengers
        # changes at location i.
        pass_change = [0] * 1001

        for trip in trips:
            num_passengers, start, end = trip

            # Pick up passengers at start.
            pass_change[start] += num_passengers

            # Drop off passengers at end.
            pass_change[end] -= num_passengers

        current_passengers = 0

        # Move from location 0 to location 1000.
        for location in range(1001):
            current_passengers += pass_change[location]

            if current_passengers > capacity:
                return False

        return True