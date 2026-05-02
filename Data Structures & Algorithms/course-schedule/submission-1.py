from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prerequisite[i] = [a, b] indicates must take course b before course a
        # total of numCourses to take, labeled 0 to numCourses - 1
        # return true if possible to finish all courses

        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()

        def dfs(crs):

            if crs in visitSet:
                return False
            
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre): return False

            visitSet.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
