# Time Limit Exceeded in case 12/80.

from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = []

        def dfs(tickets, start, path):
            if not tickets:
                result.append(path)
                return
            
            for ticket in tickets:
                if ticket[0] == start:
                    remaining_tickets = tickets[:]
                    remaining_tickets.remove(ticket)
                    dfs(remaining_tickets, ticket[1], path + [ticket[1]])

        dfs(tickets, "JFK", ["JFK"])

        return min(result)
