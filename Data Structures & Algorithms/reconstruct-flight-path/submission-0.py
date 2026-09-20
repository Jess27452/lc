from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # Create a list of destinations for every source airport.
        adj = {src: [] for src, dst in tickets}

        # Alphabetical ordering.
        tickets.sort()

        # Build the graph.
        for src, dst in tickets:
            adj[src].append(dst)

        # The route must begin at JFK.
        res = ["JFK"]

        def dfs(src):
            # If there are N tickets, the route needs N + 1 airports.
            if len(res) == len(tickets) + 1:
                return True

            # No tickets leave this airport.
            if src not in adj:
                return False

            # Copy the available destinations.
            temp = list(adj[src])

            for i, destination in enumerate(temp):

                # Temporarily use this ticket.
                adj[src].pop(i)
                res.append(destination)

                # Continue traveling from the destination.
                if dfs(destination):
                    return True

                # This choice failed, so undo it.
                adj[src].insert(i, destination)
                res.pop()

            return False

        dfs("JFK")
        return res    