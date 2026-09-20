class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
          s = set(nums)
          best = 0

          for num in s:
            if num - 1 not in s:        # start of a sequence
                cur = num
                length = 1

                while cur + 1 in s:     # grow the sequence
                    cur += 1
                    length += 1

                best = max(best, length)

          return best
        