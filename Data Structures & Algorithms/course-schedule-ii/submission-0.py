class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ordered = []
        visiting = {}
        visited = {}

        #Build adj list
        adjList = []
        for i in range(numCourses):
            adjList.append([])
        for course, prereq in prerequisites:
            adjList[course].append(prereq)

        def dfs(course):
            if visiting.get(course) != None:
                return False
            if visited.get(course) != None:
                return True

            #Set visiting
            visiting[course] = 1
            #Run DFS for each prereq
            for prereq in adjList[course]:
                if dfs(prereq) is False:
                    return False

            #Append to output list
            ordered.append(course)
            visiting[course] = None
            visited[course] = 1

        for i in range(numCourses):
            if dfs(i) is False:
                return []
        
        return ordered
        