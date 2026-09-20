from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # The answer starts with all zeros.
        # A zero means we have not found a warmer day yet.
        result = [0] * len(temperatures)

        # Each element is [temperature, index].
        # The stack stores days that are still waiting
        # for a warmer future temperature.
        stack = []

        for index, temperature in enumerate(temperatures):

            # The current day is warmer than the day
            # at the top of the stack.
            while stack and temperature > stack[-1][0]:
                previous_temperature, previous_index = stack.pop()

                # Number of days between the two days.
                result[previous_index] = index - previous_index

            # The current day now waits for its own warmer day.
            stack.append([temperature, index])

        return result