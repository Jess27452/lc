from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):

        # followMap:
        # userId -> set of followees
        #
        # Example:
        # {
        #   1: {1,2,3}
        # }
        #
        # Means:
        # user 1 follows:
        # themselves, 2, and 3

        self.followMap = defaultdict(set)

        # tweetMap:
        # userId -> list of tweets
        #
        # Each tweet stored as:
        # [count, tweetId]
        #
        # Example:
        # {
        #   1: [[0,5],[-1,7]]
        # }
        #
        # Means:
        # user 1 posted tweet 5 at time 0
        # user 1 posted tweet 7 at time -1

        self.tweetMap = defaultdict(list)

        # count works like timestamp
        #
        # We decrease it so newer tweets
        # become SMALLER numbers.
        #
        # Why?
        #
        # Because Python heapq is MIN HEAP.
        #
        # Smaller number pops first.

        self.count = 0


    def postTweet(self, userId: int, tweetId: int) -> None:

        # Store:
        # [timestamp, tweetId]

        self.tweetMap[userId].append([self.count, tweetId])

        # decrease timestamp
        #
        # newer tweet => smaller number

        self.count -= 1


    def getNewsFeed(self, userId: int) -> List[int]:

        res = []

        # minHeap stores:
        #
        # [count, tweetId, followeeId, nextIndex]
        #
        # count      -> timestamp
        # tweetId    -> tweet id
        # followeeId -> whose tweet
        # nextIndex  -> next older tweet index

        minHeap = []

        # IMPORTANT:
        #
        # User should see THEIR OWN tweets too.
        #
        # So make user follow themselves.

        self.followMap[userId].add(userId)

        # go through every followed user

        for followeeId in self.followMap[userId]:

            # if user has tweets

            if followeeId in self.tweetMap:

                # newest tweet is at END of list

                index = len(self.tweetMap[followeeId]) - 1

                count, tweetId = self.tweetMap[followeeId][index]

                # push newest tweet into heap

                minHeap.append([
                    count,
                    tweetId,
                    followeeId,
                    index - 1
                ])

        # turn list into heap

        heapq.heapify(minHeap)

        # keep getting newest tweets
        # until:
        #
        # heap empty
        # OR already have 10 tweets

        while minHeap and len(res) < 10:

            # pop MOST RECENT tweet
            #
            # because smallest count = newest

            count, tweetId, followeeId, index = heapq.heappop(minHeap)

            # add tweet to result

            res.append(tweetId)

            # if older tweet exists
            # from SAME user

            if index >= 0:

                count, tweetId = self.tweetMap[followeeId][index]

                # push next older tweet
                # into heap

                heapq.heappush(
                    minHeap,
                    [
                        count,
                        tweetId,
                        followeeId,
                        index - 1
                    ]
                )

        return res
################Adding User1’s next tweet:

#does NOT mean it gets chosen next

#It ONLY means:

#it becomes eligible for comparison

#Then heap decides globally.

    def follow(self, followerId: int, followeeId: int) -> None:

        # set uses {}
        #
        # Example:
        # {1,2,3}

        self.followMap[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:

        # remove followee if exists

        if followeeId in self.followMap[followerId]:

            self.followMap[followerId].remove(followeeId)