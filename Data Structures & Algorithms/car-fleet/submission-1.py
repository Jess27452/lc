class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = []

        for p, s in zip(position, speed):
            time = (target - p) / s
            cars.append((p, time))

        cars.sort(reverse=True)

        fleets = 0
        slowest_time = 0

        for p, time in cars:
            if time > slowest_time:
                fleets += 1
                slowest_time = time

        return fleets