from typing import List
import collections
import copy


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        table = collections.defaultdict(list)
        for _from, to in tickets:
            table[_from].append(to)
        for key in table.keys():
            table[key].sort()

        length = len(tickets) + 1
        result = []

        def dfs(table, departure='JFK', discovered=['JFK']):
            if result:
                return
                
            if length == len(discovered):
                result.append(discovered)
                return
            
            if length < len(discovered):
                return
                
            for arrival in table[departure]:
                new_table = copy.deepcopy(table)
                new_table[departure].remove(arrival)
                dfs(new_table, arrival, discovered + [arrival])
        
        dfs(table)
        return result[0]

'''
* 책에 나온 풀이
'''
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for _from, to in sorted(tickets, reverse=True):
            graph[_from].append(to)

        route = []
        def dfs(a):
            while graph[a]: # *
                dfs(graph[a].pop())
            route.append(a)
        
        dfs('JFK')
        return route[::-1]

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for _from, to in sorted(tickets, reverse=True):
            graph[_from].append(to)

        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            route.append(stack.pop())
        return route[::-1]