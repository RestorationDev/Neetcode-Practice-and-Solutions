class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        visitSet = set()

        for crs, prq in prerequisites:
            preMap[crs].append(prq)
        
        def dfs(crs):
            if crs in visitSet: #any sort of graph loop renders false
                return False
            if preMap[crs] == []: #a prereq-less crs means we can forsure take it
                return True
            
            visitSet.add(crs) #visit set grows as we recurse through the courses
            for pre in preMap[crs]:
                if not dfs(pre): return False #recursive step to all prereqs
            visitSet.remove(crs) #visit set shrinks as we confirm depth as true
            preMap[crs] = [] #if it is confirmed and survives dfs runs, we set the premap for that course to []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        
