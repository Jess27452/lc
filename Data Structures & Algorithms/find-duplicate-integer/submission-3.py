from typing import List
#I use Floyd’s cycle detection algorithm with a slow and fast pointer. The key observation is that I can treat each array index as a node, and the value at that index tells me which index to visit next. So nums[i] works like the next pointer in a linked list.

#For example, with nums = [1,3,4,2,2], starting from index 0 gives 0 → 1 → 3 → 2 → 4 → 2 → 4..., so there is a cycle. The duplicate number corresponds to the entrance of that cycle.

#In the first phase, I move slow one step with slow = nums[slow] and fast two steps with fast = nums[nums[fast]]. Since there is a cycle, they will eventually meet somewhere inside it.

#In the second phase, I start another pointer at index 0. I move that pointer and the meeting pointer one step at a time. They will meet at the entrance of the cycle, which is the duplicate number.

#This gives O(n) time and O(1) extra space, and I don't modify the array.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1:
        # Find a position inside the cycle.
        slow = 0
        fast = 0
        while True:
            # Move slow one step.
            slow = nums[slow]
            # Move fast two steps.
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # Phase 2:
        # Find the entrance of the cycle.
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow