class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[]
        for p,s in zip(position, speed):
            time =(target-p)/s
            cars.append((p,time))
        cars.sort(reverse=True)
        fleet=0
        stime=0.0
        for p, time in cars:
            if time>stime:
                fleet +=1
                stime =time
        return fleet