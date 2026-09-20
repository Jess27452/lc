class Solution:
    def findInMountainArray(
        self,
        target: int,
        mountain_arr: "MountainArray"
    ) -> int:

        length = mountain_arr.length()

        # -----------------------------------
        # Step 1: Find the mountain peak
        # -----------------------------------

        left = 1
        right = length - 2

        while left <= right:
            middle = left + (right - left) // 2

            left_value = mountain_arr.get(middle - 1)
            middle_value = mountain_arr.get(middle)
            right_value = mountain_arr.get(middle + 1)

            # We are on the increasing slope.
            if left_value < middle_value < right_value:
                left = middle + 1

            # We are on the decreasing slope.
            elif left_value > middle_value > right_value:
                right = middle - 1

            # middle is greater than both neighbors,
            # so middle is the peak.
            else:
                peak = middle
                break

        # -----------------------------------
        # Step 2: Search increasing section
        # -----------------------------------

        left = 0
        right = peak

        while left <= right:
            middle = left + (right - left) // 2
            value = mountain_arr.get(middle)

            if value == target:
                return middle

            elif value < target:
                # Normal ascending binary search.
                left = middle + 1

            else:
                right = middle - 1

        # -----------------------------------
        # Step 3: Search decreasing section
        # -----------------------------------

        left = peak + 1
        right = length - 1

        while left <= right:
            middle = left + (right - left) // 2
            value = mountain_arr.get(middle)

            if value == target:
                return middle

            elif value < target:
                # This section is decreasing.
                # Larger values are to the left.
                right = middle - 1

            else:
                # value > target
                # Smaller values are to the right.
                left = middle + 1

        return -1