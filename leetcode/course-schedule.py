from typing import List
import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        schedule = collections.defaultdict(list)
        for a, b in prerequisites:
            schedule[b].append(a)

        courses = list(schedule.keys())
        result = [True]
        visited = {}
        def dfs(course, discovered={}):
            if not result[0]:
                return
            
            if course in visited:
                return

            for next_course in schedule[course]:
                if next_course in discovered:
                    result[0] = False
                    return
                
                discovered[next_course] = 1
                dfs(next_course, discovered)
                del discovered[next_course]

            visited[course] = 1

        for course in courses:
            dfs(course, {course: 1})
            if not result[0]:
                return result[0]
        return result[0]

'''
* 책에 나온 풀이
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
        
        traced = set()
        visited = set()
        
        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False
            # 이미 방문했던 노드이면 True
            if i in visited:
                return True
            
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)
            # 탐색 종료 후 방문 노드 추가
            visited.add(i)
            
            return True
        
        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False
        
        return True