class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = {}
        self.components = n
        adjList = []
        
        for i in range(n):
            adjList.append([])
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        def dfs(node):
            #Idea: Everytime a NEW node is visited, number of components - 1.
            if visited.get(node) != None:
                return False
            else:
                visited[node] = 1

            for nextNode in adjList[node]:
                if dfs(nextNode):
                    self.components -= 1

            return True

        for i in range(n):
            dfs(i)

        return self.components