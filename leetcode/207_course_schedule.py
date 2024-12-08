from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the adj list graph
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        
        for pre in prerequisites:
            course, prereq = pre
            graph[prereq].append(course)
        
        # 0 = unvisited, 1 = currently in path visiting, 2 = visited
        visited = [0] * numCourses

        def dfs(course):
            # If the course is currently in the path that means there is a cycle
            if visited[course] == 1:
                return False
            # Already been visited
            if visited[course] == 2:
                return True
            
            # Visit all neighboring nodes
            visited[course] = 1
            for n in graph[course]:
                # Return False if base case of visiting is hit
                if not dfs(n):
                    return False
            
            visited[course] = 2
            return True

        # Perform dfs for each
        for course in graph:
            if not dfs(course):
                return False
        
        return True