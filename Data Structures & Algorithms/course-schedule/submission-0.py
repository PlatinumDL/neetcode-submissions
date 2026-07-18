class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visiting = {}
        visited = {}

        #Create adjacency list
        adjList = []
        for i in range(numCourses):
            adjList.append([])
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        def dfs(course):
            if visited.get(course) != None:
                return True
            if visiting.get(course) != None:
                return False
            
            #Set visiting
            visiting[course] = 1
            #Do dfs into prereqs
            for prereq in adjList[course]:
                if dfs(prereq) is False:
                    return False
                
            #Remove from visiting
            visiting[course] = 1
            #Add to visited 
            visited[course] = 1

        #Idea: for every course, do dfs into its prerequisites. Add it to visiting dict, and if DFS finds a course inside visiting, return false
        for i in range(len(adjList)):
            if dfs(i) is False:
                return False
        
        return True


        