class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #Connected graph with n-1 edges -> it is a tree
        #Added one extra edge, makes it cyclic
        #Find the edge that makes it a cycle, and return it
        visited = {}
        adjList = []
        #Create empty adjList
        for i in range(len(edges)+1):
            adjList.append([])
        
        def dfs(node, parent):
            if visited.get(node) != None: #If current node is already visited -> creates cycle, return False
                return False
            visited[node] = 1 #Set current node visited

            for nextNode in adjList[node]: #For each adj node, do DFS if it is not parent
                if nextNode == parent:
                    continue
                
                if dfs(nextNode,node) is False: #If any adj node DFS return False, return false
                    return False
            
            return True
            
        for a,b in edges:
            #Add edge to adj list
            adjList[a].append(b)
            adjList[b].append(a)
            visited = {}
            if dfs(a,-1) is False:
                return [a,b]

        return []
        