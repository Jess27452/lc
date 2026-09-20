class Solution:
    def candy(self, ratings):
        # Start by giving every child 1 candy.
        arr = [1] * len(ratings)

        # LEFT → RIGHT
        for i in range(1, len(ratings)):
            # If current child has higher rating than LEFT neighbor
            if ratings[i - 1] < ratings[i]:
                arr[i] = arr[i - 1] + 1

        # RIGHT → LEFT
        for i in range(len(ratings) - 2, -1, -1):
            # If current child has higher rating than RIGHT neighbor
            if ratings[i] > ratings[i + 1]:
                arr[i] = max(arr[i], arr[i + 1] + 1)
#"Give me enough for the right-neighbor rule, but don't reduce what I already earned from the left-neighbor rule."
        return sum(arr)