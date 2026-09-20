from collections import defaultdict
import heapq
from typing import List


class Twitter:

    def __init__(self):
        # Smaller count = newer tweet
        self.count = 0

        # userId -> list of [count, tweetId]
        self.tweetMap = defaultdict(list)

        # followerId -> set of followeeIds
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])

        # Make the next tweet have an even smaller number.
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        minHeap = []

        # A user should always see their own tweets.
        self.followMap[userId].add(userId)

        # Add the newest tweet from every followed user.
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:#Check whether they have tweets
                index = len(self.tweetMap[followeeId]) - 1

                count, tweetId = self.tweetMap[followeeId][index]

                minHeap.append([
                    count,
                    tweetId,
                    followeeId,
                    index - 1
                ])

        heapq.heapify(minHeap)

        # Get at most 10 newest tweets.
        while minHeap and len(result) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)

            result.append(tweetId)

            # Add this user's next-earlier tweet.
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]

                heapq.heappush(minHeap, [
                    count,
                    tweetId,
                    followeeId,
                    index - 1
                ])

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
