class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for asteroid in asteroids:
            while stack and asteroid<0 and stack[-1]>0:
                difference=stack[-1]+asteroid
                if difference>0:
                    asteroid =0
                elif difference<0:
                    stack.pop()
                else:
                    stack.pop()
                    asteroid=0
            if asteroid:
                stack.append(asteroid)       
        return stack 