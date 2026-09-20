from collections import defaultdict
from typing import List


# Union Find / Disjoint Set Union
class UnionFind:
    def __init__(self, n):
        # Initially, every account is its own parent
        # Example with 4 accounts:
        # par = [0, 1, 2, 3]
        self.par = list(range(n))
        # rank here represents the size of each group
        self.rank = [1] * n
    def find(self, x):
        # Find the leader/root of x
        # Also uses path compression to make future searches faster
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x1, x2):
        # Find the leaders of both accounts
        p1 = self.find(x1)
        p2 = self.find(x2)

        # Already in the same group
        if p1 == p2:
            return False

        # Attach the smaller group under the larger group
        if self.rank[p1] > self.rank[p2]:

            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]

        else:

            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]

        return True


class Solution:
    def accountsMerge(
        self,
        accounts: List[List[str]]
    ) -> List[List[str]]:
        # Create Union Find for all account indices
        uf = UnionFind(len(accounts))
        # emailToAcc:
        #
        # email -> account index where we first saw this email
        #
        # Example:
        # {
        #     "a@mail.com": 0,
        #     "b@mail.com": 0
        # }
        emailToAcc = {}
        # --------------------------------------------------
        # Step 1:
        # Look through every account and connect accounts
        # that share the same email
        # --------------------------------------------------
        for i, account in enumerate(accounts):

            # account looks like:
            #
            # ["John", "a@mail.com", "b@mail.com"]
            #
            # account[0] = name
            # account[1:] = emails

            for email in account[1:]:

                # If we saw this email before,
                # then the current account and old account
                # belong to the same person
                if email in emailToAcc:

                    # Example:
                    #
                    # current account = 1
                    # emailToAcc[email] = 0
                    #
                    # union(1, 0)
                    uf.union(i, emailToAcc[email])

                else:

                    # First time seeing this email
                    # remember which account it belongs to
                    emailToAcc[email] = i


        # --------------------------------------------------
        # Step 2:
        # Group emails according to their final Union Find leader
        # --------------------------------------------------
        # leader account index -> list of emails
        #
        # Example:
        #
        # {
        #     0: ["a@mail.com", "b@mail.com", "c@mail.com"],
        #     2: ["x@mail.com"]
        # }
        emailGroup = defaultdict(list)
        for email, accountIndex in emailToAcc.items():

            # Find the final group leader
            #
            # Example:
            #
            # account 1 may have been merged with account 0
            #
            # uf.find(1) -> 0
            leader = uf.find(accountIndex)
            # Put this email into that leader's group
            emailGroup[leader].append(email)
        # --------------------------------------------------
        # Step 3:
        # Build final result
        # --------------------------------------------------
        res = []
        for leader, emails in emailGroup.items():
            # Get the person's name
            #
            # accounts[leader][0]
            #
            # Example:
            # accounts[0][0] = "John"
            name = accounts[leader][0]
            # Sort emails alphabetically
            emails.sort()
            # Final format:
            #
            # ["John", "a@mail.com", "b@mail.com", ...]
            mergedAccount = [name] + emails
            res.append(mergedAccount)
        return res