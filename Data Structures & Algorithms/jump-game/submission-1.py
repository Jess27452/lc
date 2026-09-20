class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # Goal starts at the last index
        goal = len(nums) - 1

        # Loop backwards through the array
        for i in range(len(nums) - 1, -1, -1):#range(start, stop, step)
        # stop is -1 because it EXCLUDES the stop value.

            # If current position can reach the goal
            if i + nums[i] >= goal:#########we only need to reach AT LEAST the goal.
                #eg:#4+nums[4]=4
                # Move goal to current position
                goal = i
                #If current index can reach the goal,
####then THIS index becomes the new goal.
        # If we can move goal all the way to index 0
        return goal == 0
        #Because index 0 is the STARTING position.
        #0 → some reachable position
#→ another reachable position
#→ ...
#→ last index

#So starting position CAN reach the end.#