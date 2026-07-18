class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Valid tree means there is only 1 valid path from a node to another node
        #If something is already inside visited, return false
        visited = {}
        adjList = []

        #Build adjList
        for i in range(n):
            adjList.append([])
        for prevNode, nextNode in edges:
            adjList[prevNode].append(nextNode)
            adjList[nextNode].append(prevNode)

        def dfs(node,parent):
            if visited.get(node) != None:
                return False
            
            visited[node] = 1

            for nextNode in adjList[node]:
                if nextNode == parent:
                    continue
                if dfs(nextNode,node) is False:
                    return False
            return True

        if dfs(0,-1) is False:
            return False

        if len(visited) != n:
            print(len(visited))
            return False
        
        return True

        