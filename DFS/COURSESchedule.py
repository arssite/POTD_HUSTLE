https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        coursemap={i:[] for i in range(numCourses)}
        for v,j in prerequisites:
            coursemap[v].append(j)
        visited=set()
        def dfs(v):
            if v in visited:
                return False
            if coursemap[v]==[]:
                return True
            visited.add(v)
            for j in coursemap[v]:
                if not dfs(j):
                    return False
            visited.remove(v)
            coursemap[v]=[]
            return True
        for v in range(numCourses):
            if not dfs(v): 
                return False
        return True
