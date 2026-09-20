class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars =sorted(zip(position,speed),reverse=True)
        fleets=0
        stime=0.0
        for p,s in cars:
            time=(target-p)/s
            if time>stime:
                fleets+=1
                stime=time
        return fleets


