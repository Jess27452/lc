from typing import List


class Solution:
    def carFleet(
        self,
        target: int,
        position: List[int],
        speed: List[int]
    ) -> int:

        # Match each car's position with its speed.
        cars = list(zip(position, speed))

        # Store the arrival time of each fleet.
        stack = []

        # Process cars from closest to target to farthest.
        for p, s in sorted(cars, reverse=True):
            time = (target - p) / s
            stack.append(time)

            # If the car behind reaches the target no later
            # than the fleet ahead, it catches that fleet.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)