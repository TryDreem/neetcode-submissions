class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.res = []
        self.resCheck = set()
        visited = set()
        preMap = { i: [] for i in range(numCourses) }

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                if crs not in self.resCheck:
                    self.res.append(crs)
                    self.resCheck.add(crs)

                return True
            
            visited.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)
            if crs not in self.resCheck:
                self.res.append(crs)
                self.resCheck.add(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return self.res