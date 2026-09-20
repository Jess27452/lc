from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:

            # A collision is possible only when:
            # 1. There is an asteroid already in the stack.
            # 2. The current asteroid moves left.
            # 3. The top asteroid moves right.
            while stack and asteroid < 0 and stack[-1] > 0:
                difference = asteroid + stack[-1]

                if difference < 0:
                    # Current left-moving asteroid is larger.
                    stack.pop()

                elif difference > 0:
                    # The top right-moving asteroid is larger.
                    asteroid = 0

                else:
                    # They have equal sizes, so both are destroyed.
                    asteroid = 0
                    stack.pop()

            # Add the current asteroid only if it survived.
            if asteroid:
                stack.append(asteroid)

        return stack