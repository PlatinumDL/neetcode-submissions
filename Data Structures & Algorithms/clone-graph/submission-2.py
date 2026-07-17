"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        clone = {}
        
        #Edge Case
        if node == None:
            return None
        if node.neighbors == []:
            return Node(node.val, [])

        def dfs(node):
            for neighbour in node.neighbors:
                #If a node is not visited yet, dfs into neighbours
                if visited.get(neighbour) == None:
                    #Put neighbour into clone dict and set visited
                    clone[neighbour] = Node(neighbour.val, [])
                    visited[neighbour] = 1
                    dfs(neighbour)
        
        visited[node] = 1
        clone[node] = Node(node.val, [])
        dfs(node)
        
        #Now, loop through clone dict and update neighbours
        for key, value in clone.items():

            #key = original node
            #value = deep copy
            originalN = key.neighbors
            newN = value.neighbors

            for neighbour in originalN:
                copy = clone[neighbour]
                newN.append(copy)


        return clone[node]