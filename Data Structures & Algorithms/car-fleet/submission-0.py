class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)  # front to back
        fleets = 0
        curr_time = 0.0

        for p, s in cars:
            t = (target - p) / s
            if t > curr_time:
                fleets += 1
                curr_time = t

        return fleets